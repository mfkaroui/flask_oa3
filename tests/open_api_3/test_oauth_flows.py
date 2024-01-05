import pytest
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

    def test_oauth_flows_specification_extensions(
        self, oauth_flows_specification_extensions_fixture
    ):
        expected_schema: dict = {
            "x-some-data-1": "test",
            "x-some-data-2": "test",
            "x-some-data-3": "test",
        }
        assert (
            oauth_flows_specification_extensions_fixture.oa3_schema == expected_schema
        )

    @pytest.mark.parametrize(
        ("oauth_flows_init_args",),
        [
            ({"implicit": {"authorization_url": "https://example.com/authorize"}},),
            ({"implicit": {"scopes": {"read": "Grants read access"}}},),
            ({"password": {"token_url": "https://example.com/token"}},),
            ({"password": {"scopes": {"read": "Grants read access"}}},),
            ({"client_credentials": {"token_url": "https://example.com/token"}},),
            ({"client_credentials": {"scopes": {"read": "Grants read access"}}},),
            (
                {
                    "authorization_code": {
                        "token_url": "https://example.com/token",
                        "scopes": {
                            "read": "Grants read access",
                            "write": "Grants write access",
                        },
                    }
                },
            ),
            (
                {
                    "authorization_code": {
                        "authorization_url": "https://example.com/authorize",
                        "scopes": {
                            "read": "Grants read access",
                            "write": "Grants write access",
                        },
                    }
                },
            ),
            (
                {
                    "authorization_code": {
                        "authorization_url": "https://example.com/authorize",
                        "token_url": "https://example.com/token",
                    }
                },
            ),
        ],
    )
    def test_oauth_flows_flow_requirements_fail(self, oauth_flows_init_args):
        with pytest.raises(ValueError):
            OAuthFlows(**oauth_flows_init_args)
