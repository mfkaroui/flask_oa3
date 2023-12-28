import pytest
from flask_oa3.open_api_3.xml import XML

@pytest.fixture
def xml_specification_extensions_fixture() -> XML:
    yield XML(
        some_data_1="test",
        some_data_2="test",
        some_data_3="test"
    )
