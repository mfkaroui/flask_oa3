import pytest
from flask_oa3.open_api_3.security_scheme import SecurityScheme, SecuritySchemeType, SecuritySchemeLocation
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

    def test_security_scheme_variable_required_field_api_key(self):
        with pytest.raises(ValueError):
            SecurityScheme(
                security_scheme_type=SecuritySchemeType.API_KEY
            )
        with pytest.raises(ValueError):
            SecurityScheme(
                security_scheme_type=SecuritySchemeType.API_KEY,
                name="test"
            )
        SecurityScheme(
            security_scheme_type=SecuritySchemeType.API_KEY,
            name="test",
            in_location=SecuritySchemeLocation.HEADER
        )
