import pytest
from flask_oa3.open_api_3.security_requirement import SecurityRequirement

@pytest.fixture
def security_requirement_fixture() -> SecurityRequirement:
    yield SecurityRequirement(
        test_security_scheme = []
    )
