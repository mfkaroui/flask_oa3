import pytest
from flask_oa3.open_api_3.security_scheme import (
    SecurityScheme,
    SecuritySchemeType,
    SecuritySchemeLocation,
    HTTPAuthenticationScheme,
)
from flask_oa3.open_api_3.component import ComponentType
from pydantic_core import ValidationError


class TestSecurityScheme:
    def test_security_scheme_component_type(self):
        assert SecurityScheme.component_type == ComponentType.SECURITY_SCHEME

    def test_security_scheme_variable_required_field(self):
        with pytest.raises(ValidationError) as validation_error:
            SecurityScheme()
        securtiy_scheme_errors = validation_error.value.errors()
        assert len(securtiy_scheme_errors) == 1
        assert securtiy_scheme_errors[0]["type"] == "missing"
        assert securtiy_scheme_errors[0]["loc"] == ("type",)

    def test_security_scheme_specification_extensions(
        self, security_scheme_specification_extensions_fixture
    ):
        expected_schema: dict = {
            "type": "mutualTLS",
            "x-some-data-1": "test",
            "x-some-data-2": "test",
            "x-some-data-3": "test",
        }
        assert (
            security_scheme_specification_extensions_fixture.oa3_schema
            == expected_schema
        )

    def test_security_scheme_variable_required_field_api_key(self):
        with pytest.raises(ValueError):
            SecurityScheme(security_scheme_type=SecuritySchemeType.API_KEY)
        with pytest.raises(ValueError):
            SecurityScheme(security_scheme_type=SecuritySchemeType.API_KEY, name="test")
        SecurityScheme(
            security_scheme_type=SecuritySchemeType.API_KEY,
            name="test",
            in_location=SecuritySchemeLocation.HEADER,
        )

    def test_security_scheme_variable_required_field_http(self):
        with pytest.raises(ValueError):
            SecurityScheme(security_scheme_type=SecuritySchemeType.HTTP)
        SecurityScheme(
            security_scheme_type=SecuritySchemeType.HTTP,
            scheme=HTTPAuthenticationScheme.BEARER,
        )

    def test_security_scheme_variable_required_field_oauth2(
        self, oauth_flows_specification_extensions_fixture
    ):
        with pytest.raises(ValueError):
            SecurityScheme(security_scheme_type=SecuritySchemeType.OAUTH2)
        SecurityScheme(
            security_scheme_type=SecuritySchemeType.OAUTH2,
            flows=oauth_flows_specification_extensions_fixture,
        )

    def test_security_scheme_variable_required_field_open_id_connect(self):
        with pytest.raises(ValueError):
            SecurityScheme(security_scheme_type=SecuritySchemeType.OPEN_ID_CONNECT)
        SecurityScheme(
            security_scheme_type=SecuritySchemeType.OPEN_ID_CONNECT,
            open_id_connect_url="https://example.com",
        )
