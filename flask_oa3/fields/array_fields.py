from typing import Union, List

from .metaclass import FieldBase
from .mixin import RawMixin, BaseMixin
from .field_types import FieldType

class ListField(RawMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = FieldType.ARRAY

    def __init__(self, items: Union[BaseMixin, List[BaseMixin]], **kwargs):
        self.items = items
    
    @property
    def schema(self) -> dict:
        schema = super().schema
        if isinstance(self.items, list): #multi-type list
            schema["items"] = {
                "oneOf" : [item.schema for item in self.items]
            }
        else:
            schema["items"] = self.items.schema
        return schema
