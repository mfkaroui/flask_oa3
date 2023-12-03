from ..model import Model

class TestModel:
    def test__get_fields(self, model_fixture):
        fields = model_fixture._get_fields()
    
    def test__get_component_name(self, model_fixture):
        model_component_name = model_fixture._get_component_name()
        assert model_component_name.startswith("#/components/schemas/")

    def test_schema___EXTENDS__(self, model_fixture):
        """The OpenAPI Specification allows combining and extending model definitions using the allOf property of JSON Schema, in effect offering model composition.
        allOf takes an array of object definitions that are validated independently but together compose a single object.
        """
        from ..fields import StringField, IntegerField
        class TestModel2(Model):
            id = IntegerField(description="Test id field", required=True)
            name = StringField(description="Test name field")

        class TestDerivedModel1(Model):
            __EXTENDS__ = [model_fixture, TestModel2]
            a = IntegerField(description="Test a field", required=True)
            b = IntegerField(description="Test b field")

        schema = TestDerivedModel1.schema()
        assert len(schema) == 1 and "allOf" in schema
        assert isinstance(schema["allOf"], list) and len(schema["allOf"]) == 3
        assert {"$ref": model_fixture._get_component_name()} in schema["allOf"]
        assert {"$ref": TestModel2._get_component_name()} in schema["allOf"]
