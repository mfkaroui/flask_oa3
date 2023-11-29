from .metaclass import FieldMeta
from .mixin import RawMixin, NumberMixin
from .field_types import FieldType

class IntegerField(RawMixin, NumberMixin, metaclass=FieldMeta):
    __FIELD_TYPE__ = FieldType.INTEGER
    def __init__(self, **kwargs):
        pass

    @property
    def _get_type(self) -> type[int]:
        return int

class FloatField(RawMixin, NumberMixin, metaclass=FieldMeta):
    __FIELD_TYPE__ = FieldType.NUMBER

    def __init__(self, **kwargs):
        pass
    
    @property
    def _get_type(self) -> type[float]:
        return float