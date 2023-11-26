from .metaclass import FieldBase
from .mixin import RawMixin, NumberMixin
from .field_types import FieldType

class IntegerField(RawMixin, NumberMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = FieldType.INTEGER
    def __init__(self, **kwargs):
        pass

class FloatField(RawMixin, NumberMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = FieldType.NUMBER

    def __init__(self, **kwargs):
        pass

class ArbitraryField(RawMixin, NumberMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = FieldType.NUMBER

    def __init__(self, **kwargs):

        pass