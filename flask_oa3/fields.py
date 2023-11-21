class BaseField:
    __FIELD_TYPE__ = None

class NestedField(BaseField):
    __FIELD_TYPE__ = "object"

class ListField(BaseField):
    __FIELD_TYPE__ = "list"

class StringField(BaseField):
    __FIELD_TYPE__ = "string"

class BooleanField(BaseField):
    __FIELD_TYPE__ = "boolean"

class IntegerField(BaseField):
    __FIELD_TYPE__ = "number"

class FloatField(BaseField):
    __FIELD_TYPE__ = "number"

class ArbitraryField(BaseField):
    __FIELD_TYPE__ = "number"