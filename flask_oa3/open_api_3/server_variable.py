from typing import Optional, Annotated, List
from pydantic import BaseModel, Field

class ServerVariable(BaseModel):
    enum: Annotated[Optional[List[str]], Field(default=None, description="An enumeration of string values to be used if the substitution options are from a limited set. The array MUST NOT be empty.")]
    default: Annotated[str, Field(description="REQUIRED. The default value to use for substitution, which SHALL be sent if an alternate value is not supplied. Note this behavior is different than the Schema Object’s treatment of default values, because in those cases parameter values are optional. If the enum is defined, the value MUST exist in the enum’s values.")]
    description: Annotated[Optional[str], Field(default=None, description="An optional description for the server variable. CommonMark syntax MAY be used for rich text representation.")]

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Server Variable Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#serverVariableObject
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)