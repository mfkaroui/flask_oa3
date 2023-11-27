import pytest
from ..decorators import specification_extensions_support, view_docs, tag, response
from ..errors import ReservedSpecificationExtentionError

class TestDecorators:
    def test_specification_extensions_support(self):
        @specification_extensions_support
        def test_function(**specification_extensions):
            for key in specification_extensions:
                assert key.startswith("x-")
                assert "_" not in key
        
        test_function(x="", y="", z="", a_b="")

        with pytest.raises(ReservedSpecificationExtentionError):
            test_function(oas_a="test")
        
        with pytest.raises(ReservedSpecificationExtentionError):
            test_function(oai_a="test")

    def test_view_docs(self):
        from ..view import View #Local import to not corrupt scope of test document, needed for the decorator
        
        summary = "Test summary"
        description = "A long test description"
        x_some_data = "some extra data"

        @view_docs(summary, description, x_some_data=x_some_data)
        class TestView(View):
            def get(self, **kwargs):
                pass
        
        assert "summary" in TestView.__api_docs__ and TestView.__api_docs__["summary"] == summary
        assert "description" in TestView.__api_docs__ and TestView.__api_docs__["description"] == description
        assert "x-some-data" in TestView.__api_docs__ and TestView.__api_docs__["x-some-data"] == x_some_data

        with pytest.raises(TypeError):
            @view_docs(summary, description)
            class TestView:
                def get(self, **kwargs):
                    pass
    
    def test_view_tags(self):
        from ..view import View #Local import to not corrupt scope of test document, needed for the decorator
        
        tags = [f"tag_{i}" for i in range(10)]

        @tag(tags)
        class TestView(View):
            def get(self, **kwargs):
                pass
        
        assert "tags" in TestView.get.__api_docs__ and TestView.get.__api_docs__["tags"] == tags

        with pytest.raises(TypeError):
            @tag(tags)
            class TestView:
                def get(self, **kwargs):
                    pass
    
    def test_view_method_tags(self):
        from ..view import View #Local import to not corrupt scope of test document, needed for the decorator
        
        tags = [f"tag_{i}" for i in range(10)]

        
        class TestView(View):
            @tag(tags)
            def get(self, **kwargs):
                pass
            
            def delete(self, **kwargs):
                pass
        
        assert "tags" in TestView.get.__api_docs__ and TestView.get.__api_docs__["tags"] == tags
        assert "__api_docs__" not in TestView.delete.__dict__ or "tags" not in TestView.delete.__api_docs__ or len(TestView.delete.__api_docs__["tags"]) == 0

    def test_view_response(self):
        from ..view import View #Local import to not corrupt scope of test document, needed for the decorator
        from ..model import Model
        from ..fields import StringField, IntegerField

        class TestModel(Model):
            id = IntegerField(description="Test id field", required=True)
            name = StringField(description="Test name field")
        
        @response("Test JSON Response", TestModel, status_code=200)
        class TestView(View):
            def get(self, **kwargs):
                pass

            def delete(self, **kwargs):
                pass

        assert "__responses__" in TestView.get.__dict__
        assert "__responses__" in TestView.delete.__dict__

        class TestView(View):
            @response("Test JSON Response", TestModel, status_code=200)
            def get(self, **kwargs):
                pass
            
            def delete(self, **kwargs):
                pass
        
        assert "__responses__" in TestView.get.__dict__
        assert "__responses__" not in TestView.delete.__dict__