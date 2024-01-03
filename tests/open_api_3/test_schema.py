import pytest
from pydantic import ValidationError
from flask_oa3.open_api_3.schema import Schema, Discriminator
from flask_oa3.open_api_3.component import ComponentType

class TestSchema:
    def test_schema_component_type(self):
        assert Schema.component_type == ComponentType.SCHEMA
    
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

    def test_schema_specification_extensions(self, schema_with_specification_extensions_fixture):
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