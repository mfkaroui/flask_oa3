import pytest

from ...model import Model
from ...fields import *

@pytest.fixture
def model_fixture():
    class TestModel(Model):
        id = IntegerField(required=True)
        name = StringField(required=True)
        weight = FloatField(allow_null=True)
        is_active = BooleanField()
        created_at = DateTimeField()
        birthday = DateField()
        email = EmailField(required=True)
    return TestModel