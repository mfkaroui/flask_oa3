from typing import Dict, List, Union, ClassVar, Optional
from typing_extensions import Annotated
from pydantic import BaseModel, Field, computed_field, AnyUrl
from flask import Flask

from .api_provider import APIProvider
from .info import Info
from .namespace import Namespace
from .view import View
from .tag import Tag
from .external_documentation import ExternalDocumentation
from .components import Components
from .server import Server

class API(BaseModel):
    OPENAPI_VERSION: ClassVar[str] = "3.1.0"
    JSON_SCHEMA_DIALECT: ClassVar[AnyUrl] = "https://spec.openapis.org/oas/3.1/dialect/base"

    namespaces: ClassVar[Dict[str, Namespace]] = {}
    views: ClassVar[List[type[View]]] = []


    @computed_field(alias="openapi", return_type=str, description="REQUIRED. This string MUST be the version number of the OpenAPI Specification that the OpenAPI document uses. The openapi field SHOULD be used by tooling to interpret the OpenAPI document. This is not related to the API info.version string.")
    @property
    def openapi_version(self) -> str:
        return self.OPENAPI_VERSION
    info: Annotated[Info, Field(description="REQUIRED. Provides metadata about the API. The metadata MAY be used by tooling as required.")]
    @computed_field(alias="jsonSchemaDialect", return_type=AnyUrl, description="REQUIRED. This string MUST be the version number of the OpenAPI Specification that the OpenAPI document uses. The openapi field SHOULD be used by tooling to interpret the OpenAPI document. This is not related to the API info.version string.")
    @property
    def json_schema_dialect(self) -> AnyUrl:
        return self.JSON_SCHEMA_DIALECT
    servers: Annotated[Optional[List[Server]], Field(default=None, description="An array of Server Objects, which provide connectivity information to a target server. If the servers property is not provided, or is an empty array, the default value would be a Server Object with a url value of /.")]
    components: Annotated[Optional[Components], Field(default=None, description="An element to hold various schemas for the document.")]
    tags: Annotated[Optional[List[Tag]], Field(default=None, description="A list of tags used by the document with additional metadata. The order of the tags can be used to reflect on their order by the parsing tools. Not all tags that are used by the Operation Object must be declared. The tags that are not declared MAY be organized randomly or based on the tools’ logic. Each tag name in the list MUST be unique.")] = []
    external_documentation: Annotated[Optional[ExternalDocumentation], Field(alias="externalDocs", default=None, description="Additional external documentation.")]
    api_provider: Annotated[APIProvider, Field(default=APIProvider.FLASK, alias="x-api-provider", description="The provider that is serving the API")]

    def init_app(self) -> Flask:
        pass

    def register_namespace(self, namespace: Namespace):
        if namespace.name in self.namespaces:
            raise KeyError(f"A namespace with the name {namespace.name} is already registered")
        self.namespaces[namespace.name] = namespace
        if self.tags is None:
            self.tags = []
        self.tags.append(self.namespaces[namespace.name]._get_tag())

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
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)
