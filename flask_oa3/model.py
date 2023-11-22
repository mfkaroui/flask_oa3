import inspect
from typing import Dict
from .fields import FieldBase

class Model:
    @classmethod
    def _get_fields(cls) -> Dict[str, FieldBase]:
        fields = {}
        for field_name, field in inspect.getmembers(cls, lambda m: hasattr(m, "_meta")):
            if field._meta == FieldBase:
                fields[field_name] = field
        return fields

    @classmethod
    def schema(cls):
        pass
