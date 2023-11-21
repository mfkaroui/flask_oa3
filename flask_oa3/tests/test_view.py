import pytest
from ..view import View

class TestView:
    def test__get_methods(self, view_fixture):
        methods = view_fixture._get_methods()
        assert isinstance(methods, dict)
        assert "not_real_method" not in methods
        for method in methods:
            assert method in View.ALLOWED_METHODS
            assert "__api_docs__" in methods[method].__dict__
            assert "schema" in methods[method].__dict__
    
    def test_schema(self, view_fixture):
        schema = view_fixture.schema()
        print("test")