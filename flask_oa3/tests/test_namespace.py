import pytest
from ..namespace import Namespace

class TestNamespace:
    @pytest.mark.parametrize(("test_route, expected_route"), [
        ("/a", "/a"),
        ("/a/", "/a"),
        ("a/", "/a"),
        ("\\a", "/a"),
        ("\\a\\", "/a"),
        ("a\\", "/a"),
        ("a", "/a")
    ])
    def test__format_route(self, test_route, expected_route):
        assert Namespace._format_route(test_route) == expected_route

    def test__init__(self):
        assert Namespace("test_namespace", "/test_namespace").base_route == "/test_namespace"
        assert Namespace("test_namespace", "/test_namespace/").base_route == "/test_namespace"
        assert Namespace("test_namespace", "test_namespace/").base_route == "/test_namespace"
        assert Namespace("test_namespace", "test_namespace").base_route == "/test_namespace"


    def test__parse_route(self, namespace_fixture):
        assert namespace_fixture._parse_route("/sample_route") == f"{namespace_fixture.base_route}/sample_route"
        assert namespace_fixture._parse_route("sample_route/") == f"{namespace_fixture.base_route}/sample_route"
        assert namespace_fixture._parse_route("sample_route/") == f"{namespace_fixture.base_route}/sample_route"
        assert namespace_fixture._parse_route("sample_route") == f"{namespace_fixture.base_route}/sample_route"