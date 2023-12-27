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

    def test_tag_specification_extentions(self, tag_specification_extentions_fixture):
        expected_schema: dict = {
            "name": "test",
            "description": "test description",
            "externalDocs": {
                "url": "http://test.com/",
                "description": "test description"
            },
            "x-some-data-1": "test",
            "x-some-data-2": "test",
            "x-some-data-3": "test"
        }
        assert tag_specification_extentions_fixture.oa3_schema == expected_schema
        
   