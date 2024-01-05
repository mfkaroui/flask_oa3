import pytest
from flask_oa3.open_api_3.security_scheme import SecurityScheme, SecuritySchemeType


@pytest.fixture
def security_scheme_specification_extensions_fixture() -> SecurityScheme:
    yield SecurityScheme(
        security_scheme_type=SecuritySchemeType.MUTUAL_TLS,
        some_data_1="test",
        some_data_2="test",
        some_data_3="test",
    )
