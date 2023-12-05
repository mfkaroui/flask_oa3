from typing import Optional, Annotated, Dict
from pydantic import BaseModel, Field, field_validator

from .server_variable import ServerVariable

class Server(BaseModel):
    url: Annotated[str, Field(description="REQUIRED. A URL to the target host. This URL supports Server Variables and MAY be relative, to indicate that the host location is relative to the location where the OpenAPI document is being served. Variable substitutions will be made when a variable is named in {brackets}.")]
    description: Annotated[Optional[str], Field(default=None, description="An optional string describing the host designated by the URL. CommonMark syntax MAY be used for rich text representation.")]
    variables: Annotated[Optional[Dict[str, ServerVariable]], Field(default=None, description="A map between a variable name and its value. The value is used for substitution in the server’s URL template.")]

    @field_validator('url')
    def check_url(cls, v):
        if not v:
            raise ValueError('The URL to the target host is required and cannot be empty.')
        return v

    @field_validator('description')
    def check_description(cls, v):
        if v is not None and not isinstance(v, str):
            raise ValueError('The description must be a string.')
        return v

    @field_validator('variables')
    def check_variables(cls, v):
        if v is not None and not isinstance(v, dict):
            raise ValueError('The variables must be a dictionary.')
        for key, value in v.items():
            if not isinstance(key, str) or not isinstance(value, ServerVariable):
                raise ValueError('Each key in the variables dictionary must be a string and each value must be a ServerVariable instance.')
        return v

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Server Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#server-object
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)