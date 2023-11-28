from __future__ import annotations
import inspect
from typing import Dict, List
from pydantic import BaseModel, create_model
from .fields.metaclass import FieldBase

class Model:
    __EXTENDS__: List[Model] = []

    @classmethod
    def _get_component_name(cls) -> str:
        return f"#/components/schemas/{cls.__name__}"

    @classmethod
    def _get_fields(cls) -> Dict[str, FieldBase]:
        """
        Collects and returns a dictionary of field members belonging to the class and its base classes.

        This method aggregates field members defined in the class and its base classes (if any are specified in `__EXTENDS__`).
        It considers a member a field if it has an attribute `_meta` that equals `FieldBase`. The method traverses the class
        hierarchy, gathering these fields into a dictionary, where keys are the field names and values are the corresponding
        field instances.

        Returns:
            Dict[str, FieldBase]: A dictionary mapping field names to their respective field instances. These fields are
            collected from the class and any classes specified in its `__EXTENDS__` attribute.
        """
        fields = {}
        if len(cls.__EXTENDS__) > 0:
            for base in cls.__EXTENDS__:
                fields.update(base._get_fields())
        for field_name, field in inspect.getmembers(cls, lambda m: hasattr(m, "_meta")):
            if field._meta == FieldBase:
                fields[field_name] = field
        return fields

    @classmethod
    def generate_validator(cls) -> type[BaseModel]:
        """
        Dynamically generates a Pydantic model for input validation based on the class's defined fields.
    
        This method utilizes the `_get_fields` class method to retrieve all the relevant fields of the class.
        It then constructs a Pydantic model where each field is transformed into a corresponding Pydantic field type,
        enabling validation and parsing of input data according to the field specifications. The name of the generated
        Pydantic model is derived from the class's name with 'Validator' appended.
    
        Returns:
            type[BaseModel]: A dynamically created Pydantic model class, which can be used for validating
            and parsing input data based on the field definitions of the current class.
        """     
        fields = {field_name: field._get_type() for field_name, field in cls._get_fields()}
        return create_model(f"{cls.__name__}Validator", **fields)

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
        extends = [base for base in cls.__EXTENDS__ if issubclass(base, Model) and base.__name__ != cls.__name__]
        if len(extends) > 0:
            extends = {
                "allOf": [
                    {
                        "$ref": base._get_component_name()
                    }
                    for base in extends
                ]
            }
            extends["allOf"].append(schema)
            schema = extends
        return schema
