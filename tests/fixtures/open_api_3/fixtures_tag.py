import pytest
from flask_oa3.open_api_3.tag import Tag

@pytest.fixture
def tag_by_field_name_fixture(external_documentation_fixture) -> Tag:
    yield Tag(
        name="test",
        description="test description",
        external_documentation=external_documentation_fixture
    )

@pytest.fixture
def tag_by_alias_fixture(external_documentation_fixture) -> Tag:
    yield Tag(
        name="test",
        description="test description",
        externalDocs=external_documentation_fixture
    )

@pytest.fixture
def tag_no_description_fixture(external_documentation_fixture) -> Tag:
    yield Tag(
        name="test",
        external_documentation=external_documentation_fixture
    )

@pytest.fixture
def tag_no_external_documentation_fixture() -> Tag:
    yield Tag(
        name="test",
        description="test description"
    )

@pytest.fixture
def tag_just_name_fixture() -> Tag:
    yield Tag(
        name="test"
    )