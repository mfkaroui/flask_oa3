import pytest
from ...view import View

@pytest.fixture
def view_fixture():
    class SampleView(View):
        def get(self, **kwargs):
            return None
        def post(self, **kwargs):
            return None
        def put(self, **kwargs):
            return None
        def patch(self, **kwargs):
            return None
        def delete(self, **kwargs):
            return None
        def not_real_method(self, **kwargs):
            return None
    return SampleView