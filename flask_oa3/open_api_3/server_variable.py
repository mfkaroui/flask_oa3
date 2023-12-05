from typing import Optional, Annotated, List
from pydantic import BaseModel, Field, field_validator

class ServerVariable(BaseModel):
    enum: Annotated[Optional[List[str]], Field(default=None, description="An enumeration of string values to be used if the substitution options are from a limited set. The array MUST NOT be empty.")]
    default: Annotated[str, Field(description="REQUIRED. The default value to use for substitution, which SHALL be sent if an alternate value is not supplied. Note this behavior is different than the Schema Object’s treatment of default values, because in those cases parameter values are optional. If the enum is defined, the value MUST exist in the enum’s values.")]
    description: Annotated[Optional[str], Field(default=None, description="An optional description for the server variable. CommonMark syntax MAY be used for rich text representation.")]

    @field_validator('enum')
    def check_enum(cls, v):
        if v is not None:
            if not all(isinstance(item, str) and item for item in v):
                raise ValueError('All items in enum must be non-empty strings.')
        return v

    @field_validator('default')
    def check_default(cls, v, values, **kwargs):
        if not v:
            raise ValueError('The default value is required and cannot be empty.')
        if 'enum' in values and v not in values['enum']:
            raise ValueError('The default value must exist in the enum values.')
        return v

    @field_validator('description')
    def check_description(cls, v):
        if v is not None and not isinstance(v, str):
            raise ValueError('The description must be a string.')
        return v

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Server Variable Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#serverVariableObject
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)