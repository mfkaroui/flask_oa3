import pytest
from pydantic import ValidationError
from flask_oa3.open_api_3.security_requirement import SecurityRequirement

class TestSecurityRequirement:
    def test_security_requirement_no_specification_extensions(self):
        with pytest.raises(ValidationError):
            SecurityRequirement({"test-no-ext": "bad-data"})

    def test_security_requirement_oa3_schema(self, security_requirement_fixture):
        assert security_requirement_fixture.oa3_schema == {
            "test_security_scheme": []
        }