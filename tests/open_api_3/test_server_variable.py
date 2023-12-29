import pytest
from flask_oa3.open_api_3.server_variable import ServerVariable
from pydantic_core import ValidationError

class TestServerVariable:
    def test_server_variable_required_field(self):
        with pytest.raises(ValidationError) as validation_error:
            ServerVariable()
        server_variable_errors = validation_error.value.errors()
        assert len(server_variable_errors) == 1
        assert server_variable_errors[0]["type"] == "missing"
        assert server_variable_errors[0]["loc"] == ("default",)

    def test_variable_specification_extensions(self, server_variable_specification_extensions_fixture):
        expected_schema: dict = {
            "default": "test1",
            "x-some-data-1": "test",
            "x-some-data-2": "test",
            "x-some-data-3": "test"
        }
        assert server_variable_specification_extensions_fixture.oa3_schema == expected_schema

    def test_server_variable_oa3_schema(self, server_variable_with_enum_fixture):
        expected_schema: dict = {
            "enum": [
                "test1",
                "test2"
            ],
            "default": "test1",
            "description": "test description"
        }
        assert server_variable_with_enum_fixture.oa3_schema == expected_schema

    def test_server_variable_no_description_oa3_schema(self, server_variable_with_enum_no_description_fixture):
        expected_schema: dict = {
            "enum": [
                "test1",
                "test2"
            ],
            "default": "test1"
        }
        assert server_variable_with_enum_no_description_fixture.oa3_schema == expected_schema

    def test_server_variable_just_default_oa3_schema(self, server_variable_just_default_fixture):
        expected_schema: dict = {
            "default": "test1"
        }
        assert server_variable_just_default_fixture.oa3_schema == expected_schema

    @pytest.mark.parametrize(("default_value",), [
        ("test3",),
        ("test4",),
        ("test5",),
        ("test",),
        ("test_1",),
        ("test2_",)
    ])
    def test_server_variable_enum_default_fail(self, default_value):
        with pytest.raises(ValueError) as validation_error:
            ServerVariable(
                enum=["test1", "test2"],
                default=default_value,
                description="test description"
            )

    @pytest.mark.parametrize(("default_value",), [
        ("test1",),
        ("test2",),
        ("test3",),
        ("test4",),
        ("test5",)
    ])
    def test_server_variable_enum_default_pass(self, default_value):
        ServerVariable(
            enum=["test1", "test2", "test3", "test4", "test5"],
            default=default_value,
            description="test description"
        )
