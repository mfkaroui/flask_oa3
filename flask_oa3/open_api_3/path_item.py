from typing import Optional, Annotated, List, Union, ClassVar
from enum import Enum
from pydantic import BaseModel, Field, field_validator
from .external_documentation import ExternalDocumentation
from .component import Component, ComponentType
from .reference import Reference
from .server import Server
from .parameter import Parameter
from .operation import Operation

class PathItem(Component):
    component_type: ClassVar[ComponentType] = ComponentType.PATH_ITEM

    ref: Annotated[Optional[str], Field(default=None, alias="$ref", description="Allows for a referenced definition of this path item. The referenced structure MUST be in the form of a Path Item Object. In case a Path Item Object field appears both in the defined object and the referenced object, the behavior is undefined. See the rules for resolving Relative References.")]
    summary: Annotated[Optional[str], Field(default=None, description="An optional, string summary, intended to apply to all operations in this path.")]
    description: Annotated[Optional[str], Field(default=None, description="An optional, string description, intended to apply to all operations in this path. CommonMark syntax MAY be used for rich text representation.")]
    get: Annotated[Optional[Operation], Field(default=None, description="A definition of a GET operation on this path.")]
    put: Annotated[Optional[Operation], Field(default=None, description="A definition of a PUT operation on this path.")]
    post: Annotated[Optional[Operation], Field(default=None, description="A definition of a POST operation on this path.")]
    delete: Annotated[Optional[Operation], Field(default=None, description="A definition of a DELETE operation on this path.")]
    options: Annotated[Optional[Operation], Field(default=None, description="A definition of a OPTIONS operation on this path.")]
    head: Annotated[Optional[Operation], Field(default=None, description="A definition of a HEAD operation on this path.")]
    patch: Annotated[Optional[Operation], Field(default=None, description="A definition of a PATCH operation on this path.")]
    trace: Annotated[Optional[Operation], Field(default=None, description="A definition of a TRACE operation on this path.")]
    servers: Annotated[Optional[List[Server]], Field(default=None, description="An alternative server array to service all operations in this path.")]
    parameters: Annotated[Optional[List[Union[Parameter, Reference[Parameter]]]], Field(default=None, description="A list of parameters that are applicable for all the operations described under this path. These parameters can be overridden at the operation level, but cannot be removed there. The list MUST NOT include duplicated parameters. A unique parameter is defined by a combination of a name and location. The list can use the Reference Object to link to parameters that are defined at the OpenAPI Object’s components/parameters.")]

    @field_validator("parameters")
    def validate_parameters(cls, parameters):
        seen = set()
        for param in parameters:
            if isinstance(param, Parameter):
                identifier = (param.name, param.location)
                if identifier in seen:
                    raise ValueError("Duplicate Parameter: A unique parameter is defined by a combination of a name and location")
                seen.add(identifier)
        return parameters

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Path Item Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#path-item-object
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)