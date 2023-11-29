from typing import Dict, List, Union, ClassVar, Optional
from typing_extensions import Annotated
from pydantic import BaseModel, Field
from flask import Flask

from .info import Info
from .namespace import Namespace
from .view import View
from .tag import Tag
from .external_documentation import ExternalDocumentation

class API(BaseModel):
    OPENAPI_VERSION: ClassVar[str] = "3.1.0"
    info: Annotated[Info, Field(description="REQUIRED. Provides metadata about the API. The metadata MAY be used by tooling as required.")]
    tags: Annotated[Optional[List[Tag]], Field(default=[], description="A list of tags used by the document with additional metadata. The order of the tags can be used to reflect on their order by the parsing tools. Not all tags that are used by the Operation Object must be declared. The tags that are not declared MAY be organized randomly or based on the tools’ logic. Each tag name in the list MUST be unique.")] = []
    namespaces: ClassVar[Dict[str, Namespace]] = {}
    views: ClassVar[List[type[View]]] = []
    external_documentation: Annotated[Optional[ExternalDocumentation], Field(default=None, description="Additional external documentation.")]
    
    def init_app(self) -> Flask:
        pass

    def register_namespace(self, namespace: Namespace):
        if namespace.name in self.namespaces:
            raise KeyError(f"A namespace with the name {namespace.name} is already registered")
        self.namespaces[namespace.name] = namespace

    def register_view(self, view: View, route: str):
        full_route = self._parse_route(route)
        if full_route in self.views:
            raise RouteInUseError(f"Route {full_route} already in use by {self.views[full_route].__class__.__name__}")
        self.views[full_route] = view

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'OpenAPI Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#openapi-object
        
        Returns:
            dict: The Open API schema
        """        
        schema = {
            "openapi": self.OPENAPI_VERSION,
            "info": self.info.oa3_schema(),
            "jsonSchemaDialect": "https://spec.openapis.org/oas/3.1/dialect/base",
            "tags": {}
        }
        if self.tags is not None and len(self.tags) > 0:
            schema["tags"].update({tag.name: tag.oa3_schema() for tag in self.tags})
        if self.namespaces is not None and len(self.namespaces) > 0:
            schema["tags"].update({namespace.name: namespace._get_tag().oa3_schema() for namespace in self.namespaces})
        if len(schema["tags"]) == 0:
            schema.pop("tags") #not used remove it
        else:
            schema["tags"] = list(schema["tags"].values()) #ensures that all tags have unique names
        if self.external_documentation is not None:
            schema["externalDocs"] = self.external_documentation.oa3_schema()
        return schema
