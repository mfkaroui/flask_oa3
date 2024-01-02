from flask_oa3.open_api_3.oauth_flow import OAuthFlow

class TestOAuthFlow:

    def test_oauth_flow_required_fields(self):
        oauth_flow = OAuthFlow()
        assert oauth_flow.authorization_url is None
        assert oauth_flow.token_url is None
        assert oauth_flow.refresh_url is None
        assert oauth_flow.scopes is None

    def test_oauth_flows_specification_extensions(self, oauth_flow_specification_extensions_fixture):
        expected_schema: dict = {
            "x-some-data-1": "test",
            "x-some-data-2": "test",
            "x-some-data-3": "test"
        }
        assert oauth_flow_specification_extensions_fixture.oa3_schema == expected_schema
