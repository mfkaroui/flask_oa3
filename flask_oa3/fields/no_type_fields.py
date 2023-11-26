from typing import TYPE_CHECKING
from .metaclass import FieldBase
from .mixin import RawMixin
from .field_types import FieldType

if TYPE_CHECKING:
    from ..model import Model

class NestedField(RawMixin, metaclass=FieldBase):
    

    """A field the references an existing model as its values"""
    __FIELD_TYPE__ = FieldType.NO_TYPE

    def __init__(self, model: "Model", **kwargs):
        """References another model to be used as a field.

        Args:
            model (Union[Model, List[Model]]): A model to reference.
        """        
        self.model = model

    @property
    def schema(self) -> dict:
        schema = super().schema
        schema["$ref"] = self.model._get_component_name()
        return schema
