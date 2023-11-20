import pytest
from ..decorators import specification_extensions_support, view_docs
from ..errors import ReservedSpecificationExtentionError

class TestDecorators:
    def test_specification_extensions_support(self):
        @specification_extensions_support
        def test_function(**specification_extensions):
            for key in specification_extensions:
                assert key.startswith("x-")
        
        test_function(x="", y="", z="")

        with pytest.raises(ReservedSpecificationExtentionError):
            test_function(oas_a="test")
        
        with pytest.raises(ReservedSpecificationExtentionError):
            test_function(oai_a="test")

    def test_view_docs(self):
        from ..view import View #Local import to not corrupt scope of test document, needed for the decorator
        
        summary = "Test summary"
        description = "A long test description"

        @view_docs(summary=summary, description=description)
        class TestView(View):
            def get(self, **kwargs):
                pass
        
        assert "summary" in TestView.__api_docs__ and TestView.__api_docs__["summary"] == summary
        assert "description" in TestView.__api_docs__ and TestView.__api_docs__["description"] == description

        with pytest.raises(TypeError):
            @view_docs(summary=summary, description=description)
            class TestView:
                def get(self, **kwargs):
                    pass