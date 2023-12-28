import pytest
from flask_oa3.open_api_3.external_documentation import ExternalDocumentation
from pydantic_core import ValidationError

class TestExternalDocumentation:
    def test_external_documentation_required_field(self):
        with pytest.raises(ValidationError) as validation_error:
            ExternalDocumentation()
        external_documentation_errors = validation_error.value.errors()
        assert len(external_documentation_errors) == 1
        assert external_documentation_errors[0]["type"] == "missing"
        assert external_documentation_errors[0]["loc"] == ("url",)

    def test_external_documentation_specification_extensions(self, external_documentation_specification_extensions_fixture):
        expected_schema: dict = {
            "url": "http://test.com/",
            "description": "test description",
            "x-some-data-1": "test",
            "x-some-data-2": "test",
            "x-some-data-3": "test"
        }
        assert external_documentation_specification_extensions_fixture.oa3_schema == expected_schema

    def test_external_documentation_optional_parameters_oa3_schema(self, external_documentation_no_description_fixture):
        expected_schema_no_description: dict = {
            "url": "http://test.com/"
        }
        assert external_documentation_no_description_fixture.oa3_schema == expected_schema_no_description
    