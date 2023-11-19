import pytest
from ..view import View

class TestView:
    def test__get_methods(self, view_fixture):
        methods = view_fixture._get_methods()
        assert isinstance(methods, dict)
        assert "not_real_method" not in methods
        for method in methods:
            assert method in View.ALLOWED_METHODS
        