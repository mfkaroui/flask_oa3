import pytest
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

    @pytest.mark.parametrize(("field_class, expected_field_type"), [
        (NestedField, FieldType.OBJECT),
        (ListField, FieldType.ARRAY),
        (StringField, FieldType.STRING),
        (DateField, FieldType.STRING),
        (DateTimeField, FieldType.STRING),
        (PasswordField, FieldType.STRING),
        (Base64EncodedField, FieldType.STRING),
        (EmailField, FieldType.STRING),
        (UUID4Field, FieldType.STRING),
        (URIField, FieldType.STRING),
        (IPv4Field, FieldType.STRING),
        (IPv6Field, FieldType.STRING),
        (BooleanField, FieldType.BOOLEAN),
        (IntegerField, FieldType.INTEGER),
        (FloatField, FieldType.NUMBER),
        (ArbitraryField, FieldType.NUMBER)
    ])
    def test___FIELD_TYPE___value(self, field_class, expected_field_type):
        assert field_class.__FIELD_TYPE__ == expected_field_type
