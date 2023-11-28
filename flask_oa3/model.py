from __future__ import annotations
import inspect
from typing import Dict, List

from .fields.metaclass import FieldBase

class Model:
    __EXTENDS__: List[Model] = []

    @classmethod
    def _get_component_name(cls) -> str:
        return f"#/components/schemas/{cls.__name__}"

    @classmethod
    def _get_fields(cls) -> Dict[str, FieldBase]:
        fields = {}
        for field_name, field in inspect.getmembers(cls, lambda m: hasattr(m, "_meta")):
            if field._meta.__name__ == FieldBase:
                fields[field_name] = field
        return fields

    @classmethod
    def schema(cls):
        """Constructs the Open API 'Schema Object' according to specifications

        Returns:
            dict: The Open API schema
        """   
        model_fields = cls._get_fields()
        schema = {
            "type": "object",
            "required": [field_name for field_name in model_fields if model_fields[field_name].required],
            "properties": {field_name: model_fields[field_name].schema for field_name in model_fields}
        }
        if len(schema["required"]) == 0:
            schema.pop("required") #dont need it, remove it
        if len(cls.__EXTENDS__) > 0:
            extends = {
                "allOf": [
                    {
                        "$ref": extend.__self._get_component_name()
                    }
                    for extend in cls.__EXTENDS__
                ]
            }
            schema = [schema, *extends]
        return schema
