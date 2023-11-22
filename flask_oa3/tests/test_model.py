class TestModel:
    def test__get_fields(self, model_fixture):
        fields = model_fixture._get_fields()