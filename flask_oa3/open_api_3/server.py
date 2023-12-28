from __future__ import annotations
from typing import Optional, Annotated, Dict, List
from pydantic import BaseModel, Field, model_validator
import re

from .server_variable import ServerVariable
from .decorators import specification_extensions_support

@specification_extensions_support
class Server(BaseModel):
    url: Annotated[str, Field(description="REQUIRED. A URL to the target host. This URL supports Server Variables and MAY be relative, to indicate that the host location is relative to the location where the OpenAPI document is being served. Variable substitutions will be made when a variable is named in {brackets}.")]
    description: Annotated[Optional[str], Field(default=None, description="An optional string describing the host designated by the URL. CommonMark syntax MAY be used for rich text representation.")]
    variables: Annotated[Optional[Dict[str, ServerVariable]], Field(default=None, description="A map between a variable name and its value. The value is used for substitution in the server’s URL template.")]

    @model_validator(mode="after")
    @classmethod
    def validate_variables(cls, self: Server) -> Server:
        failed_variables: List[str] = []
        for match in re.findall(r"\{([a-zA-Z0-9\-\_]+)\}", str(self.url)):
            if self.variables is None or match not in self.variables:
                failed_variables.append(match)
        if len(failed_variables) > 0:
            raise NameError(f"Variables {failed_variables} are not defined in 'variables'")
        return self


    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Server Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#server-object
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)