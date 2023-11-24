class TestModel:
    def test__get_fields(self, model_fixture):
        fields = model_fixture._get_fields()
    
    def test__get_component_name(self, model_fixture):
        model_component_name = model_fixture._get_component_name()
        assert model_component_name.startswith("#/components/schemas/")