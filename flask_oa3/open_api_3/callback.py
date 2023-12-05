from typing import Dict
from pydantic import BaseModel, root_validator
from .path_item import PathItem
from .runtime_expression import RuntimeExpression

class Callback(BaseModel):
    __root__: Dict[str, PathItem]

    @root_validator(pre=True)
    @classmethod
    def check_keys(cls, values):
        for key in values.get('__root__', {}):
            RuntimeExpression(expression=key)
        return values

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Callback Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#callbackObject
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)