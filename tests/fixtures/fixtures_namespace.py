import pytest
from ...namespace import Namespace

@pytest.fixture
def namespace_fixture() -> Namespace:
    fixture = Namespace("test_namespace", "/test_namespace")
    return fixture