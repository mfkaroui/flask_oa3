import pytest
from flask_oa3.open_api_3.oauth_flow import OAuthFlow


@pytest.fixture
def oauth_flow_specification_extensions_fixture() -> OAuthFlow:
    yield OAuthFlow(some_data_1="test", some_data_2="test", some_data_3="test")


@pytest.fixture
def oauth_flow_implicit_fixture() -> OAuthFlow:
    yield OAuthFlow(
        authorization_url="https://example.com/authorize",
        scopes={"read": "Grants read access"},
    )


@pytest.fixture
def oauth_flow_password_fixture() -> OAuthFlow:
    yield OAuthFlow(
        token_url="https://example.com/token", scopes={"write": "Grants write access"}
    )


@pytest.fixture
def oauth_flow_client_credentials_fixture() -> OAuthFlow:
    yield OAuthFlow(
        token_url="https://example.com/token", scopes={"admin": "Grants admin access"}
    )


@pytest.fixture
def oauth_flow_authorization_code_fixture() -> OAuthFlow:
    yield OAuthFlow(
        authorization_url="https://example.com/authorize",
        token_url="https://example.com/token",
        scopes={"read": "Grants read access", "write": "Grants write access"},
    )
