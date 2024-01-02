from flask_oa3.open_api_3.oauth_flows import OAuthFlows

class TestOAuthFlows:
    """
    Test class for testing the OAuthFlows model.
    """

    def test_oauth_flows_required_fields(self):
        """
        Test case for verifying that the 'implicit', 'password', 'client_credentials', and 'authorization_code' fields are optional in the OAuthFlows model.
        """
        oauth_flows = OAuthFlows()
        assert oauth_flows.implicit is None
        assert oauth_flows.password is None
        assert oauth_flows.client_credentials is None
        assert oauth_flows.authorization_code is None

    def test_oauth_flows_specification_extensions(self, oauth_flows_specification_extensions_fixture):
        expected_schema: dict = {
            "x-some-data-1": "test",
            "x-some-data-2": "test",
            "x-some-data-3": "test"
        }
        assert oauth_flows_specification_extensions_fixture.oa3_schema == expected_schema
