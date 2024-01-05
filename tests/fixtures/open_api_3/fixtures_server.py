import pytest
from flask_oa3.open_api_3.server import Server


@pytest.fixture
def server_specification_extensions_fixture() -> Server:
    yield Server(
        url="http://test.com/",
        some_data_1="test",
        some_data_2="test",
        some_data_3="test",
    )


@pytest.fixture
def server_with_description_server_variables_fixture(
    server_variable_with_enum_fixture,
) -> Server:
    yield Server(
        url="http://{test}.com/",
        description="test description",
        variables={"test": server_variable_with_enum_fixture},
    )
