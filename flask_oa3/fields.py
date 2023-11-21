from typing import Union

class BaseField:
    __FIELD_TYPE__ = None

    def __init__(self, description: Union[str, None] = None, required: bool = False, allow_null: bool = False):
        self.description = description
        self.required = required
        self.allow_null = allow_null

class NestedField(BaseField):
    __FIELD_TYPE__ = "object"

    def __init__(self):
        super().__init__()

class ListField(BaseField):
    __FIELD_TYPE__ = "list"

    def __init__(self):
        super().__init__()

class StringField(BaseField):
    __FIELD_TYPE__ = "string"

    def __init__(self):
        super().__init__()

class BooleanField(BaseField):
    __FIELD_TYPE__ = "boolean"

    def __init__(self):
        super().__init__()

class IntegerField(BaseField):
    __FIELD_TYPE__ = "number"

    def __init__(self):
        super().__init__()

class FloatField(BaseField):
    __FIELD_TYPE__ = "number"

    def __init__(self):
        super().__init__()

class ArbitraryField(BaseField):
    __FIELD_TYPE__ = "number"

    def __init__(self):
        super().__init__()