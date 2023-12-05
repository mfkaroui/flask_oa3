from typing import Dict, List, Annotated
from pydantic import BaseModel, Field, validator
from .security_scheme import SecuritySchemeType

class SecurityRequirement(BaseModel):
    __root__: Annotated[Dict[str, List[str]], Field(description="Each name MUST correspond to a security scheme which is declared in the Security Schemes under the Components Object. If the security scheme is of type 'oauth2' or 'openIdConnect', then the value is a list of scope names required for the execution, and the list MAY be empty if authorization does not require a specified scope. For other security scheme types, the array MAY contain a list of role names which are required for the execution, but are not otherwise defined or exchanged in-band.")]

    @validator('__root__')
    def check_root(cls, v):
        if not isinstance(v, dict):
            raise ValueError('The root field must be a dictionary.')
        for key, value in v.items():
            if not isinstance(key, str) or not all(isinstance(item, str) for item in value):
                raise ValueError('Each key in the root dictionary must be a string and each value must be a list of strings.')
        return v

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Security Requirement Object' according to specifications

        Spec:
            https://spec.openapis.org/oas/v3.1.0#security-requirement-object

        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)