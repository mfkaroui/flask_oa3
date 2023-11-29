from .metaclass import FieldMeta
from .mixin import RawMixin
from .field_types import FieldType

class BooleanField(RawMixin, metaclass=FieldMeta):
    __FIELD_TYPE__ = FieldType.BOOLEAN

    def __init__(self, **kwargs):
        pass