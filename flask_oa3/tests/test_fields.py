import pytest
from ..fields import *

class TestFields:
    @pytest.mark.parametrize(("field_class, expected_bases"), [
        (NestedField, [RawMixin]),
        (ListField, [RawMixin]),
        (StringField, [RawMixin, StringMixin]),
        (DateField, [RawMixin, StringMixin]),
        (DateTimeField, [RawMixin, StringMixin]),
        (PasswordField, [RawMixin, StringMixin]),
        (Base64EncodedField, [RawMixin, StringMixin]),
        (EmailField, [RawMixin, StringMixin]),
        (UUID4Field, [RawMixin, StringMixin]),
        (URIField, [RawMixin, StringMixin]),
        (IPv4Field, [RawMixin, StringMixin]),
        (IPv6Field, [RawMixin, StringMixin]),
        (BooleanField, [RawMixin]),
        (IntegerField, [RawMixin, NumberMixin]),
        (FloatField, [RawMixin, NumberMixin]),
        (ArbitraryField, [RawMixin, NumberMixin])
    ])
    def test_field_mixin(self, field_class, expected_bases):
        assert field_class.__class__ == FieldBase
        for expected_base in expected_bases:
            assert issubclass(field_class, expected_base)

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
