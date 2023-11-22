from ..fields import *

class TestFields:
    def test_nested_field(self):
        field = NestedField(description="This is a test", minimum=12)
        print("test")
    
    def test_list_field(self):
        field = ListField(description="This is a test", minimum=12)
        print("test")

    def test_string_field(self):
        field = StringField(description="This is a test", minimum=12)
        print("test")
    
    def test_boolean_field(self):
        field = BooleanField(description="This is a test", minimum=12)
        print("test")

    def test_integer_field(self):
        field = IntegerField(description="This is a test", minimum=12)
        print("test")
    
    def test_float_field(self):
        field = FloatField(description="This is a test", minimum=12)
        print("test")
    
    def test_arbitrary_field(self):
        field = ArbitraryField(description="This is a test", minimum=12)
        print("test")