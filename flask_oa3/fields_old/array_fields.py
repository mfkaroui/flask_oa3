from typing import Union, List, TypeVar

from .metaclass import FieldMeta
from .mixin import RawMixin, BaseField
from .field_types import FieldType

class ListField(RawMixin, metaclass=FieldMeta):
    __FIELD_TYPE__ = FieldType.ARRAY

    def __init__(self, items: Union[BaseField, List[BaseField]], **kwargs):
        if isinstance(items, list):
            if len(items) == 0:
                raise ValueError("List field cannot be empty")
            else:
                for item in items:
                    if not issubclass(item.__class__, BaseField):
                        raise TypeError("All elements of the list must be instances of BaseField class")
        self.items = items
    
    @property
    def _get_type(self) -> type[list]:
        return list 

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
