from typing import Optional, List, Union, Dict
from typing_extensions import Annotated
from pydantic import BaseModel, Field
from .external_documentation import ExternalDocumentation
from .reference import Reference
from .server import Server
from .parameter import Parameter
from .tag import Tag
from .request_body import RequestBody
from .callback import Callback
from .security_requirement import SecurityRequirement
from .responses import Responses

class Operation(BaseModel):
    tags: Annotated[Optional[List[Union[Tag, str]]], Field(default=None, description="A list of tags for API documentation control. Tags can be used for logical grouping of operations by resources or any other qualifier.")]
    summary: Annotated[Optional[str], Field(default=None, description="A short summary of what the operation does.")]
    description: Annotated[Optional[str], Field(default=None, description="A verbose explanation of the operation behavior. CommonMark syntax MAY be used for rich text representation.")]
    external_documentation: Annotated[Optional[ExternalDocumentation], Field(default=None, description="Additional external documentation for this operation.")]
    operation_id: Annotated[Optional[str], Field(default=None, description="Unique string used to identify the operation. The id MUST be unique among all operations described in the API. The operationId value is case-sensitive. Tools and libraries MAY use the operationId to uniquely identify an operation, therefore, it is RECOMMENDED to follow common programming naming conventions.")]
    parameters: Annotated[Optional[List[Union[Parameter, Reference[Parameter]]]], Field(default=None, description="A list of parameters that are applicable for this operation. If a parameter is already defined at the Path Item, the new definition will override it but can never remove it. The list MUST NOT include duplicated parameters. A unique parameter is defined by a combination of a name and location. The list can use the Reference Object to link to parameters that are defined at the OpenAPI Object’s components/parameters.")]
    request_body: Annotated[Optional[Union[RequestBody, Reference[RequestBody]]], Field(default=None, description="The request body applicable for this operation. The requestBody is fully supported in HTTP methods where the HTTP 1.1 specification [RFC7231] has explicitly defined semantics for request bodies. In other cases where the HTTP spec is vague (such as GET, HEAD and DELETE), requestBody is permitted but does not have well-defined semantics and SHOULD be avoided if possible.")]
    responses: Annotated[Optional[Responses], Field(default=None, description="The list of possible responses as they are returned from executing this operation.")]
    callbacks: Annotated[Optional[Dict[str, Union[Callback, Reference[Callback]]]], Field(default=None, description="A map of possible out-of band callbacks related to the parent operation. The key is a unique identifier for the Callback Object. Each value in the map is a Callback Object that describes a request that may be initiated by the API provider and the expected responses.")]
    deprecated: Annotated[Optional[bool], Field(default=None, description="Declares this operation to be deprecated. Consumers SHOULD refrain from usage of the declared operation. Default value is false.")]
    security: Annotated[Optional[List[SecurityRequirement]], Field(default=None, description="A declaration of which security mechanisms can be used for this operation. The list of values includes alternative security requirement objects that can be used. Only one of the security requirement objects need to be satisfied to authorize a request. To make security optional, an empty security requirement ({}) can be included in the array. This definition overrides any declared top-level security. To remove a top-level security declaration, an empty array can be used.")]
    servers: Annotated[Optional[List[Server]], Field(default=None, description="An alternative server array to service this operation. If an alternative server object is specified at the Path Item Object or Root level, it will be overridden by this value.")]
    
    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Operation Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#operation-object
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)