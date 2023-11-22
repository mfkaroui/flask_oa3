import pytest

from ...model import Model
from ...fields import *

@pytest.fixture
def model_fixture():
    class TestModel(Model):
        id = IntegerField()
        name = StringField()
        weight = FloatField()
        is_active = BooleanField()
        created_at = DateTimeField()
        birthday = DateField()
        email = EmailField()
    return TestModel