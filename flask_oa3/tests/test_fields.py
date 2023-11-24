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
        (NestedField, FieldType.NO_TYPE),
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

    def test_nested_field_schema(self, model_fixture):
        nested_field = NestedField(model_fixture)
        assert "$ref" in nested_field.schema and nested_field.schema["$ref"] == model_fixture._get_component_name()

    def test_list_field_schema(self, model_fixture):
        single_type_list_field = ListField(IntegerField())
        multi_type_list_field = ListField([
            NestedField(model_fixture),
            StringField(),
            IntegerField()
        ])
        assert "items" in single_type_list_field.schema and "items" in multi_type_list_field.schema
        assert single_type_list_field.schema["items"] == IntegerField().schema
        assert "oneOf" in multi_type_list_field.schema["items"] and isinstance(multi_type_list_field.schema["items"]["oneOf"], list)
        assert NestedField(model_fixture).schema in multi_type_list_field.schema["items"]["oneOf"]
        assert StringField().schema in multi_type_list_field.schema["items"]["oneOf"]
        assert IntegerField().schema in multi_type_list_field.schema["items"]["oneOf"]