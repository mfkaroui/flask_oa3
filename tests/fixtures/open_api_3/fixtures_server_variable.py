import pytest
from flask_oa3.open_api_3.server_variable import ServerVariable


@pytest.fixture
def server_variable_specification_extensions_fixture() -> ServerVariable:
    yield ServerVariable(
        default="test1", some_data_1="test", some_data_2="test", some_data_3="test"
    )


@pytest.fixture
def server_variable_with_enum_fixture() -> ServerVariable:
    yield ServerVariable(
        enum=["test1", "test2"], default="test1", description="test description"
    )


@pytest.fixture
def server_variable_with_enum_no_description_fixture() -> ServerVariable:
    yield ServerVariable(enum=["test1", "test2"], default="test1")


@pytest.fixture
def server_variable_just_default_fixture() -> ServerVariable:
    yield ServerVariable(default="test1")
