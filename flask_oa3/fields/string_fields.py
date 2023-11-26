class StringField(RawMixin, StringMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        pass

class DateField(RawMixin, StringMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "date"

class DateTimeField(RawMixin, StringMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "date-time"

class PasswordField(RawMixin, StringMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "password"

class Base64EncodedField(RawMixin, StringMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "byte"

from .metaclass import FieldBase
from .mixin import RawMixin, StringMixin
from .field_types import FieldType

class EmailField(RawMixin, StringMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "email"

class UUID4Field(RawMixin, StringMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "uuid4"

class URIField(RawMixin, StringMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "uri"

class IPv4Field(RawMixin, StringMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "ipv4"

class IPv6Field(RawMixin, StringMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "ipv6"
