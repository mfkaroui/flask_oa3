from typing import Optional, Annotated, Dict, Union
from pydantic import BaseModel, Field

from .schema import Schema
from .response import Response
from .example import Example
from .header import Header
from .parameter import Parameter
from .reference import Reference
from .request_body import RequestBody
from .security_scheme import SecurityScheme
from .link import Link
from .path_item import PathItem
from .callback import Callback

class Components(BaseModel):
    schemas: Annotated[Optional[Dict[str, Union[Schema, Reference]]], Field(default=None, description="An object to hold reusable Schema Objects.")]
    responses: Annotated[Optional[Dict[str, Union[Response, Reference]]], Field(default=None, description="An object to hold reusable Response Objects.")]
    parameters: Annotated[Optional[Dict[str, Union[Parameter, Reference]]], Field(default=None, description="An object to hold reusable Parameter Objects.")]
    examples: Annotated[Optional[Dict[str, Union[Example, Reference]]], Field(default=None, description="An object to hold reusable Example Objects.")]
    request_bodies: Annotated[Optional[Dict[str, Union[RequestBody, Reference]]], Field(default=None, alias="requestBodies", description="An object to hold reusable Request Body Objects.")]
    headers: Annotated[Optional[Dict[str, Union[Header, Reference]]], Field(default=None, description="An object to hold reusable Header Objects.")]
    security_schemes: Annotated[Optional[Dict[str, Union[SecurityScheme, Reference]]], Field(default=None, alias="securitySchemes", description="An object to hold reusable Security Scheme Objects.")]
    links: Annotated[Optional[Dict[str, Union[Link, Reference]]], Field(default=None, description="An object to hold reusable Link Objects.")]
    callbacks: Annotated[Optional[Dict[str, Union[Callback, Reference]]], Field(default=None, description="An object to hold reusable Callback Objects.")]
    path_items: Annotated[Optional[Dict[str, Union[PathItem, Reference]]], Field(default=None, alias="pathItems", description="An object to hold reusable Path Item Object.")]

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Components Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#components-object
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)