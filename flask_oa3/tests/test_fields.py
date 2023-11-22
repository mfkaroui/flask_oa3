from ..fields import IntegerField

class TestFields:
    def test_integer_field(self):
        field = IntegerField(description="This is a test", minimum=12)
        print("test")