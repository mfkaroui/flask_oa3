import pytest
from pydantic import ValidationError
from flask_oa3.open_api_3.schema import Schema, Discriminator
from flask_oa3.open_api_3.component import ComponentType
from flask_oa3.open_api_3.reference import Reference

class TestSchema:
    def test_schema_component_type(self):
        assert Schema.component_type == ComponentType.SCHEMA
    
    def test_schema_with_discriminator_no_iterable_fail(self, schema_class_fixture, discriminator_fixture):
        with pytest.raises(TypeError):
            Schema(schema_model=schema_class_fixture, discriminator=discriminator_fixture)

    def test_schema_with_discriminator_bad_property_name_fail(self, schema_class_fixture, reference_schema_fixture, schema_class_with_dict_fixture):
        with pytest.raises(KeyError):
            Schema(schema_model=[schema_class_fixture, schema_class_with_dict_fixture], discriminator=Discriminator(property_name="bad_property"))
        with pytest.raises(KeyError):
            Schema(schema_model=(schema_class_fixture, schema_class_with_dict_fixture), discriminator=Discriminator(property_name="bad_property"))
        with pytest.raises(KeyError):
            Schema(schema_model=(reference_schema_fixture, schema_class_with_dict_fixture), discriminator=Discriminator(property_name="bad_property"))
    
    def test_schema_with_bad_model_fail(self):
        class BadModel:
            str_field: str
        class AnotherBadModel:
            int_field: int
        with pytest.raises(TypeError):
            Schema(schema_model=BadModel)
        with pytest.raises(TypeError):
            Schema(schema_model=[BadModel, AnotherBadModel])
        with pytest.raises(TypeError):
            Schema(schema_model=(BadModel, AnotherBadModel))

    def test_schema_component_name(self, schema_class_fixture):
        test_schema = Schema(schema_model=schema_class_fixture)
        assert test_schema.component_name == "TestSchema"

    def test_schema_python_inheritance_component_name(self, schema_class_python_inheritance_fixture):
        test_schema = Schema(schema_model=schema_class_python_inheritance_fixture)
        assert test_schema.component_name == "PythonInheritanceTestSchema"

    def test_schema_reference_component_name(self, reference_schema_fixture):
        test_schema = Schema(schema_model=reference_schema_fixture)
        assert test_schema.component_name == "ref.TestSchema"

    def test_schema_oa3_composition_schema_component_name(self, schema_class_fixture, schema_class_with_dict_fixture):
        test_schema = Schema(schema_model=[schema_class_fixture, schema_class_with_dict_fixture])
        assert test_schema.component_name == "all_of[TestSchema, DictTestSchema]"

    def test_schema_oa3_composition_with_ref_schema_component_name(self, reference_schema_fixture, schema_class_with_dict_fixture):
        test_schema = Schema(schema_model=[reference_schema_fixture, schema_class_with_dict_fixture])
        assert test_schema.component_name == "all_of[ref.TestSchema, DictTestSchema]"

    def test_schema_oa3_union_schema_component_name(self, schema_class_fixture, schema_class_with_dict_fixture):
        test_schema = Schema(schema_model=(schema_class_fixture, schema_class_with_dict_fixture))
        assert test_schema.component_name == "one_of[TestSchema, DictTestSchema]"

    def test_schema_oa3_union_with_ref_schema_component_name(self, reference_schema_fixture, schema_class_with_dict_fixture):
        test_schema = Schema(schema_model=(reference_schema_fixture, schema_class_with_dict_fixture))
        assert test_schema.component_name == "one_of[ref.TestSchema, DictTestSchema]"

    def test_schema_oa3_schema(self, schema_class_fixture):
        expected_schema: dict = {
            "properties": {
                "int_field": {
                    "description": "An integer field",
                    "title": "Int Field",
                    "type": "integer"
                },
                "str_field": {
                    "description": "A string field",
                    "title": "Str Field",
                    "type": "string"
                },
                "optional_field": {
                    "anyOf": [
                        {"type": "string"},
                        {"type": "null"}
                    ],
                    "default": None,
                    "description": "An optional field",
                    "title": "Optional Field"
                }
            },
            "required": [
                "int_field",
                "str_field"
            ],
            "title": "TestSchema",
            "type": "object"
        }
        test_schema = Schema(schema_model=schema_class_fixture)
        assert test_schema.oa3_schema == expected_schema

    def test_schema_specification_extensions_oa3_schema(self, schema_with_specification_extensions_fixture):
        expected_schema: dict = {
            "properties": {
                "int_field": {
                    "description": "An integer field",
                    "title": "Int Field",
                    "type": "integer"
                },
                "str_field": {
                    "description": "A string field",
                    "title": "Str Field",
                    "type": "string"
                },
                "optional_field": {
                    "anyOf": [
                        {"type": "string"},
                        {"type": "null"}
                    ],
                    "default": None,
                    "description": "An optional field",
                    "title": "Optional Field"
                }
            },
            "required": [
                "int_field",
                "str_field"
            ],
            "title": "TestSchema",
            "type": "object",
            "x-some-data-1": "test",
            "x-some-data-2": "test",
            "x-some-data-3": "test"
        }
        assert schema_with_specification_extensions_fixture.oa3_schema == expected_schema

    def test_schema_python_inheritance_oa3_schema(self, schema_class_python_inheritance_fixture):
        expected_schema: dict = {
            "properties": {
                "int_field": {
                    "description": "An integer field override",
                    "title": "Int Field",
                    "type": "integer"
                },
                "str_field": {
                    "description": "A string field",
                    "title": "Str Field",
                    "type": "string"
                },
                "optional_field": {
                    "anyOf": [
                        {"type": "string"},
                        {"type": "null"}
                    ],
                    "default": None,
                    "description": "An optional field",
                    "title": "Optional Field"
                },
                "bool_field": {
                    "description": "A boolean field",
                    "title": "Bool Field",
                    "type": "boolean"
                }
            },
            "required": [
                "int_field",
                "str_field",
                "bool_field"
            ],
            "title": "PythonInheritanceTestSchema",
            "type": "object"
        }
        test_schema = Schema(schema_model=schema_class_python_inheritance_fixture)
        assert test_schema.oa3_schema == expected_schema

    def test_schema_reference_oa3_schema(self, reference_schema_fixture):
        expected_schema: dict = {
            "$ref": "#/components/schemas/TestSchema",
            "title": "ref.TestSchema"
        }
        test_schema = Schema(schema_model=reference_schema_fixture)
        assert test_schema.oa3_schema == expected_schema

    def test_schema_python_inheritance_oa3_schema(self, schema_class_python_inheritance_fixture):
        expected_schema: dict = {
            "properties": {
                "int_field": {
                    "description": "An integer field override",
                    "title": "Int Field",
                    "type": "integer"
                },
                "str_field": {
                    "description": "A string field",
                    "title": "Str Field",
                    "type": "string"
                },
                "optional_field": {
                    "anyOf": [
                        {"type": "string"},
                        {"type": "null"}
                    ],
                    "default": None,
                    "description": "An optional field",
                    "title": "Optional Field"
                },
                "bool_field": {
                    "description": "A boolean field",
                    "title": "Bool Field",
                    "type": "boolean"
                }
            },
            "required": [
                "int_field",
                "str_field",
                "bool_field"
            ],
            "title": "PythonInheritanceTestSchema",
            "type": "object"
        }
        test_schema = Schema(schema_model=schema_class_python_inheritance_fixture)
        assert test_schema.oa3_schema == expected_schema

    def test_schema_oa3_composition_schema_oa3_schema(self, schema_class_fixture, schema_class_with_dict_fixture):
        expected_schema: dict = {
            "allOf": [
                {
                    "properties": {
                        "int_field": {
                            "description": "An integer field",
                            "title": "Int Field",
                            "type": "integer"
                        },
                        "str_field": {
                            "description": "A string field",
                            "title": "Str Field",
                            "type": "string"
                        },
                        "optional_field": {
                            "anyOf": [
                                {"type": "string"},
                                {"type": "null"}
                            ],
                            "default": None,
                            "description": "An optional field",
                            "title": "Optional Field"
                        }
                    },
                    "required": [
                        "int_field",
                        "str_field"
                    ],
                    "title": "TestSchema",
                    "type": "object"
                },
                {
                    "properties": {
                        "model_type": {
                            "anyOf": [
                                {"const": "dict"},
                                {"const": "list"}
                            ],
                            "default": "dict",
                            "title": "Model Type"
                        },
                        "dict_field": {
                            "additionalProperties": {
                                "type": "integer"
                            },
                            "description": "A dict field",
                            "title": "Dict Field",
                            "type": "object"
                        }
                    },
                    "required": [
                        "dict_field"
                    ],
                    "title": "DictTestSchema",
                    "type": "object"
                }
            ],
            "title": "all_of[TestSchema, DictTestSchema]"
        }
        test_schema = Schema(schema_model=[schema_class_fixture, schema_class_with_dict_fixture])
        assert test_schema.oa3_schema == expected_schema

    def test_schema_oa3_composition_with_ref_schema_oa3_schema(self, reference_schema_fixture, schema_class_with_dict_fixture):
        expected_schema: dict = {
            "allOf": [
                {
                    "$ref": "#/components/schemas/TestSchema",
                    "title": "ref.TestSchema"
                },
                {
                    "properties": {
                        "model_type": {
                            "anyOf": [
                                {"const": "dict"},
                                {"const": "list"}
                            ],
                            "default": "dict",
                            "title": "Model Type"
                        },
                        "dict_field": {
                            "additionalProperties": {
                                "type": "integer"
                            },
                            "description": "A dict field",
                            "title": "Dict Field",
                            "type": "object"
                        }
                    },
                    "required": [
                        "dict_field"
                    ],
                    "title": "DictTestSchema",
                    "type": "object"
                }
            ],
            "title": "all_of[ref.TestSchema, DictTestSchema]"
        }
        test_schema = Schema(schema_model=[reference_schema_fixture, schema_class_with_dict_fixture])
        assert test_schema.oa3_schema == expected_schema

    def test_schema_oa3_union_schema_oa3_schema(self, schema_class_fixture, schema_class_with_dict_fixture):
        expected_schema: dict = {
            "oneOf": [
                {
                    "properties": {
                        "int_field": {
                            "description": "An integer field",
                            "title": "Int Field",
                            "type": "integer"
                        },
                        "str_field": {
                            "description": "A string field",
                            "title": "Str Field",
                            "type": "string"
                        },
                        "optional_field": {
                            "anyOf": [
                                {"type": "string"},
                                {"type": "null"}
                            ],
                            "default": None,
                            "description": "An optional field",
                            "title": "Optional Field"
                        }
                    },
                    "required": [
                        "int_field",
                        "str_field"
                    ],
                    "title": "TestSchema",
                    "type": "object"
                },
                {
                    "properties": {
                        "model_type": {
                            "anyOf": [
                                {"const": "dict"},
                                {"const": "list"}
                            ],
                            "default": "dict",
                            "title": "Model Type"
                        },
                        "dict_field": {
                            "additionalProperties": {
                                "type": "integer"
                            },
                            "description": "A dict field",
                            "title": "Dict Field",
                            "type": "object"
                        }
                    },
                    "required": [
                        "dict_field"
                    ],
                    "title": "DictTestSchema",
                    "type": "object"
                }
            ],
            "title": "one_of[TestSchema, DictTestSchema]"
        }
        test_schema = Schema(schema_model=(schema_class_fixture, schema_class_with_dict_fixture))
        assert test_schema.oa3_schema == expected_schema

    def test_schema_oa3_union_with_ref_schema_oa3_schema(self, reference_schema_fixture, schema_class_with_dict_fixture):
        expected_schema: dict = {
            "oneOf": [
                {
                    "$ref": "#/components/schemas/TestSchema",
                    "title": "ref.TestSchema"
                },
                {
                    "properties": {
                        "model_type": {
                            "anyOf": [
                                {"const": "dict"},
                                {"const": "list"}
                            ],
                            "default": "dict",
                            "title": "Model Type"
                        },
                        "dict_field": {
                            "additionalProperties": {
                                "type": "integer"
                            },
                            "description": "A dict field",
                            "title": "Dict Field",
                            "type": "object"
                        }
                    },
                    "required": [
                        "dict_field"
                    ],
                    "title": "DictTestSchema",
                    "type": "object"
                }
            ],
            "title": "one_of[ref.TestSchema, DictTestSchema]"
        }
        test_schema = Schema(schema_model=(reference_schema_fixture, schema_class_with_dict_fixture))
        assert test_schema.oa3_schema == expected_schema

    def test_schema_oa3_union_schema_with_discriminator_oa3_schema(self, schema_class_with_list_fixture, schema_class_with_dict_fixture):
        expected_schema: dict = {
            "discriminator": {
                "propertyName": "model_type"
            },
            "oneOf": [
                {
                    "properties": {
                        "model_type": {
                            "anyOf": [
                                {"const": "dict"},
                                {"const": "list"}
                            ],
                            "default": "list",
                            "title": "Model Type"
                        },
                        "list_field": {
                            "description": "A list field",
                            "items": {
                                "type": "string"
                            },
                        "title": "List Field",
                        "type": "array"
                        }
                    },
                    "required": [
                        "list_field"
                    ],
                    "title": "ListTestSchema",
                    "type": "object"
                },
                {
                    "properties": {
                        "model_type": {
                            "anyOf": [
                                {"const": "dict"},
                                {"const": "list"}
                            ],
                            "default": "dict",
                            "title": "Model Type"
                        },
                        "dict_field": {
                            "additionalProperties": {
                                "type": "integer"
                            },
                            "description": "A dict field",
                            "title": "Dict Field",
                            "type": "object"
                        }
                    },
                    "required": [
                        "dict_field"
                    ],
                    "title": "DictTestSchema",
                    "type": "object"
                }
            ],
            "title": "one_of[ListTestSchema, DictTestSchema]"
        }
        test_schema = Schema(schema_model=(schema_class_with_list_fixture, schema_class_with_dict_fixture), discriminator=Discriminator(property_name="model_type"))
        assert test_schema.oa3_schema == expected_schema
        test_schema = Schema(schema_model=[schema_class_with_list_fixture, schema_class_with_dict_fixture], discriminator=Discriminator(property_name="model_type"))
        assert test_schema.oa3_schema == expected_schema

    def test_schema_oa3_union_schema_with_reference_discriminator_oa3_schema(self, schema_class_with_list_fixture, schema_class_with_dict_fixture):
        expected_schema: dict = {
            "discriminator": {
                "propertyName": "model_type"
            },
            "oneOf": [
                {
                    "properties": {
                        "model_type": {
                            "anyOf": [
                                {"const": "dict"},
                                {"const": "list"}
                            ],
                            "default": "list",
                            "title": "Model Type"
                        },
                        "list_field": {
                            "description": "A list field",
                            "items": {
                                "type": "string"
                            },
                            "title": "List Field",
                            "type": "array"
                        }
                    },
                    "required": [
                        "list_field"
                    ],
                    "title": "ListTestSchema",
                    "type": "object"
                },
                {
                    "$ref": "#/components/schemas/DictTestSchema",
                    "title": "ref.DictTestSchema"
                }
            ],
            "title": "one_of[ListTestSchema, ref.DictTestSchema]"
        }
        test_schema = Schema(schema_model=(schema_class_with_list_fixture, Reference[Schema](component=Schema(schema_model=schema_class_with_dict_fixture))), discriminator=Discriminator(property_name="model_type"))
        assert test_schema.oa3_schema == expected_schema

    def test_schema_with_reference_of_reference_has_property(self, reference_schema_fixture):
        test_schema = Schema(schema_model=reference_schema_fixture)
        assert test_schema.has_property("int_field")
        assert test_schema.has_property("str_field")
        assert test_schema.has_property("optional_field")

    def test_schema_with_nested_field_oa3_schema(self, schema_class_with_nested_model):
        expected_schema = {
            "properties": {
                "nested_field": {
                    "$ref": "#/components/schemas/TestSchema"
                },
                "list_field": {
                    "description": "A list field",
                    "items": {
                        "type": "string"
                    },
                    "title": "List Field",
                    "type": "array"
                }
            },
            "required": [
                "nested_field",
                "list_field"
            ],
            "title": "NestedTestSchema",
            "type": "object"
        }
        test_schema = Schema(schema_model=schema_class_with_nested_model)
        assert test_schema.oa3_schema == expected_schema

    def test_schema_oa3_composition_with_nested_field_oa3_schema(self, schema_class_with_nested_model, schema_class_with_dict_fixture):
        expected_schema = {
            "allOf": [
                {
                    "properties": {
                        "nested_field": {
                            "$ref": "#/components/schemas/TestSchema"
                        },
                        "list_field": {
                            "description": "A list field",
                            "items": {"type": "string"},
                            "title": "List Field",
                            "type": "array"
                        }
                    },
                    "required": [
                        "nested_field",
                        "list_field"
                    ],
                    "title": "NestedTestSchema",
                    "type": "object"
                },
                {
                    "properties": {
                        "model_type": {
                            "anyOf": [
                                {"const": "dict"},
                                {"const": "list"}
                            ],
                            "default": "dict",
                            "title": "Model Type"
                        },
                        "dict_field": {
                            "additionalProperties": {
                                "type": "integer"
                            },
                            "description": "A dict field",
                            "title": "Dict Field",
                            "type": "object"
                        }
                    },
                    "required": [
                        "dict_field"
                    ],
                    "title": "DictTestSchema",
                    "type": "object"
                }
            ],
            "title": "all_of[NestedTestSchema, DictTestSchema]"
        }
        test_schema = Schema(schema_model=[schema_class_with_nested_model, schema_class_with_dict_fixture])
        assert test_schema.oa3_schema == expected_schema


class TestDiscriminator:
    def test_discriminator_required_fields(self):
        with pytest.raises(ValidationError) as validation_error:
            Discriminator()
        discriminator_errors = validation_error.value.errors()
        assert len(discriminator_errors) == 1
        assert discriminator_errors[0]["type"] == "missing"
        assert discriminator_errors[0]["loc"] == ("propertyName",)

    def test_discriminator_specification_extensions(self, discriminator_specification_extensions_fixture):
        expected_schema: dict = {
            "propertyName": "test_property",
            "x-some-data-1": "test",
            "x-some-data-2": "test",
            "x-some-data-3": "test"
        }
        assert discriminator_specification_extensions_fixture.oa3_schema == expected_schema

    def test_discriminator_oa3_schema(self, discriminator_fixture):
        assert discriminator_fixture.oa3_schema == {
            "propertyName": "test_property"
        }