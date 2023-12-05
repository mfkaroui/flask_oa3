from typing import Dict, Union, Annotated
from pydantic import BaseModel, Field

from .response import Response
from .reference import Reference

class Responses(BaseModel):
    __root__: Annotated[Dict[str, Union[Response, Reference]], Field(description="The documentation of responses other than the ones declared for specific HTTP response codes. Use this field to cover undeclared responses.")]

    @property
    def oa3_schema(self):
        """Constructs the Open API 'Responses Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#responses-object
        
        Returns:
            dict: The Open API schema
        """   
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)