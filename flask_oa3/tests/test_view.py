import pytest
from ..view import View

class TestView:
    def test__bind_method_schema(self):
        def test_function():
            pass
        View._bind_method_schema(test_function)
        assert "__api_docs__" in test_function.__dict__
        assert "schema" in test_function.__dict__

    def test__get_methods(self, view_fixture):
        methods = view_fixture._get_methods()
        assert isinstance(methods, dict)
        assert "not_real_method" not in methods
        for method in methods:
            assert method in View.ALLOWED_METHODS
    
    def test_schema(self, view_fixture):
        schema = view_fixture.schema()
        print("test")