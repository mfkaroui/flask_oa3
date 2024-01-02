import pytest
from flask_oa3.open_api_3.oauth_flows import OAuthFlows

@pytest.fixture
def oauth_flows_specification_extensions_fixture() -> OAuthFlows:
    yield OAuthFlows(
        some_data_1="test",
        some_data_2="test",
        some_data_3="test"
    )
