import pytest
from flask_oa3.open_api_3.tag import Tag
from pydantic_core import ValidationError


class TestTag:
    """
    Test class for testing the Tag model.
    """

    def test_tag_required_field(self):
        """
        Test case for verifying that the 'name' field is required in the Tag model.
        """
        with pytest.raises(ValidationError) as validation_error:
            Tag()
        tag_errors = validation_error.value.errors()
        assert len(tag_errors) == 1
        assert tag_errors[0]["type"] == "missing"
        assert tag_errors[0]["loc"] == ("name",)

    def test_tag_specification_extensions(self, tag_specification_extensions_fixture):
        """
        Test case for verifying the specification extensions in the Tag model.
        """
        expected_schema: dict = {
            "name": "test",
            "description": "test description",
            "externalDocs": {
                "url": "http://test.com/",
                "description": "test description",
            },
            "x-some-data-1": "test",
            "x-some-data-2": "test",
            "x-some-data-3": "test",
        }
        assert tag_specification_extensions_fixture.oa3_schema == expected_schema

    def test_tag_oa3_schema(self, tag_by_field_name_fixture, tag_by_alias_fixture):
        """
        Test case for verifying the OpenAPI 3 schema of the Tag model by field name and by alias.
        """
        expected_schema: dict = {
            "name": "test",
            "description": "test description",
            "externalDocs": {
                "url": "http://test.com/",
                "description": "test description",
            },
        }
        assert tag_by_field_name_fixture.oa3_schema == expected_schema
        assert tag_by_alias_fixture.oa3_schema == expected_schema

    def test_tag_optional_parameters_oa3_schema(
        self,
        tag_no_description_fixture,
        tag_no_external_documentation_fixture,
        tag_just_name_fixture,
    ):
        """
        Test case for verifying the OpenAPI 3 schema of the Tag model with optional parameters.
        """
        expected_schema_no_description: dict = {
            "name": "test",
            "externalDocs": {
                "url": "http://test.com/",
                "description": "test description",
            },
        }
        expected_schema_no_external_documentation: dict = {
            "name": "test",
            "description": "test description",
        }
        expected_schema_just_name: dict = {"name": "test"}
        assert tag_no_description_fixture.oa3_schema == expected_schema_no_description
        assert (
            tag_no_external_documentation_fixture.oa3_schema
            == expected_schema_no_external_documentation
        )
        assert tag_just_name_fixture.oa3_schema == expected_schema_just_name
