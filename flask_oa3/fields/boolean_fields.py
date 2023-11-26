from .metaclass import FieldBase
from .mixin import RawMixin
from .field_types import FieldType

class BooleanField(RawMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = FieldType.BOOLEAN

    def __init__(self, **kwargs):
        pass