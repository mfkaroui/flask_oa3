from typing import Optional, Annotated, Dict, ClassVar
from enum import StrEnum
from pydantic import BaseModel, Field
from .external_documentation import ExternalDocumentation
from .component import Component, ComponentType

class ParameterLocation(StrEnum):
    PATH = "path" #Used together with Path Templating, where the parameter value is actually part of the operation’s URL. This does not include the host or base path of the API. For example, in /items/{itemId}, the path parameter is itemId.
    QUERY = "query" #Parameters that are appended to the URL. For example, in /items?id=###, the query parameter is id.
    HEADER = "header" #Custom headers that are expected as part of the request. Note that [RFC7230] states header names are case insensitive.
    COOKIE = "cookie" #Used to pass a specific cookie value to the API.

class Parameter(Component):
    name: Annotated[str, Field(defualt=None, description="REQUIRED. The name of the parameter. Parameter names are case sensitive.")]
    in_location: Annotated[Optional[ParameterLocation], Field(defualt=None, alias="in", description="REQUIRED. The location of the parameter. Possible values are \"query\", \"header\", \"path\" or \"cookie\".")]
    description: Annotated[Optional[str], Field(defualt=None, description="A brief description of the parameter. This could contain examples of use. CommonMark syntax MAY be used for rich text representation.")]
    required: Annotated[Optional[str], Field(defualt=None, description="Determines whether this parameter is mandatory. If the parameter location is \"path\", this property is REQUIRED and its value MUST be true. Otherwise, the property MAY be included and its default value is false.")]
    deprecated: Annotated[Optional[str], Field(defualt=None, description="Specifies that a parameter is deprecated and SHOULD be transitioned out of usage. Default value is false.")]

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Parameter Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#parameter-object
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)