import pytest
from flask_oa3.open_api_3.external_documentation import ExternalDocumentation

@pytest.fixture
def external_documentation_fixture() -> ExternalDocumentation:
    yield ExternalDocumentation(
        url="http://test.com",
        description="test description"
    )

@pytest.fixture
def external_documentation_no_description_fixture() -> ExternalDocumentation:
    yield ExternalDocumentation(
        url="http://test.com"
    )
