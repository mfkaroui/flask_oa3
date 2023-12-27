from typing import Dict, Union, TYPE_CHECKING
from pydantic import RootModel, model_validator
from .runtime_expression import RuntimeExpression
from .reference import Reference

if TYPE_CHECKING:
    from .path_item import PathItem

class Callback(RootModel):
    root: Dict[str, Union['PathItem', Reference['PathItem']]]

    @model_validator(mode="before")
    @classmethod
    def check_keys(cls, values):
        for key in values.get('root', {}):
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

