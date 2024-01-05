from flask_oa3.open_api_3.oauth_flow import OAuthFlow


class TestOAuthFlow:
    def test_oauth_flow_required_fields(self):
        oauth_flow = OAuthFlow()
        assert oauth_flow.authorization_url is None
        assert oauth_flow.token_url is None
        assert oauth_flow.refresh_url is None
        assert oauth_flow.scopes is None

    def test_oauth_flow_specification_extensions(
        self, oauth_flow_specification_extensions_fixture
    ):
        expected_schema: dict = {
            "x-some-data-1": "test",
            "x-some-data-2": "test",
            "x-some-data-3": "test",
        }
        assert oauth_flow_specification_extensions_fixture.oa3_schema == expected_schema

    def test_oauth_flow_oa3_schema(
        self,
        oauth_flow_implicit_fixture,
        oauth_flow_password_fixture,
        oauth_flow_client_credentials_fixture,
        oauth_flow_authorization_code_fixture,
    ):
        assert oauth_flow_implicit_fixture.oa3_schema == {
            "authorizationUrl": "https://example.com/authorize",
            "scopes": {"read": "Grants read access"},
        }
        assert oauth_flow_password_fixture.oa3_schema == {
            "tokenUrl": "https://example.com/token",
            "scopes": {"write": "Grants write access"},
        }
        assert oauth_flow_client_credentials_fixture.oa3_schema == {
            "tokenUrl": "https://example.com/token",
            "scopes": {"admin": "Grants admin access"},
        }
        assert oauth_flow_authorization_code_fixture.oa3_schema == {
            "authorizationUrl": "https://example.com/authorize",
            "tokenUrl": "https://example.com/token",
            "scopes": {"read": "Grants read access", "write": "Grants write access"},
        }
