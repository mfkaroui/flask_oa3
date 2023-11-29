from .metaclass import FieldMeta
from .field_types import FieldType
from .mixin import RawMixin, StringMixin
import datetime as dt

class StringField(RawMixin, StringMixin, metaclass=FieldMeta):
    """
    Represents a basic string field without any specific formatting.
    
    Inherits from RawMixin and StringMixin to provide basic string handling
    functionality. It uses FieldMeta as its metaclass.
    """
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        pass

    @property
    def _get_type(self) -> type[str]:
        return str

class DateField(RawMixin, StringMixin, metaclass=FieldMeta):
    """
    Represents a field specifically formatted for date values.
    
    Inherits from RawMixin and StringMixin, and utilizes FieldMeta as its metaclass.
    It is pre-configured with a 'date' format.
    """
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "date"
    
    @property
    def _get_type(self) -> type[dt.date]:
        return dt.date

class DateTimeField(RawMixin, StringMixin, metaclass=FieldMeta):
    """
    Represents a field for date-time values.
    
    Inherits from RawMixin and StringMixin, and uses FieldMeta as its metaclass.
    Pre-configured with a 'date-time' format to handle datetime values.
    """
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "date-time"
    
    @property
    def _get_type(self) -> type[dt.datetime]:
        return dt.datetime

class PasswordField(RawMixin, StringMixin, metaclass=FieldMeta):
    """
    A field designed for password strings.
    
    Inherits from RawMixin and StringMixin. Utilizes FieldMeta as its metaclass.
    This field type is pre-configured with a 'password' format, suitable for
    password handling and validation.
    """
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "password"
    
    @property
    def _get_type(self) -> type[str]:
        return str

class Base64EncodedField(RawMixin, StringMixin, metaclass=FieldMeta):
    """
    Field for handling Base64 encoded strings.
    
    Inherits from RawMixin and StringMixin, with FieldMeta as its metaclass.
    This field is specifically formatted for 'byte' type strings, typically
    used for Base64 encoded data.
    """
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "byte"

    @property
    def _get_type(self) -> type[str]:
        return str

class EmailField(RawMixin, StringMixin, metaclass=FieldMeta):
    """
    A field tailored for email address strings.
    
    Inherits from RawMixin and StringMixin, and uses FieldMeta as its metaclass.
    It is configured with an 'email' format to validate email addresses.
    """
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "email"

    @property
    def _get_type(self) -> type[str]:
        return str

class UUID4Field(RawMixin, StringMixin, metaclass=FieldMeta):
    """
    Represents a field for UUID version 4 strings.
    
    Inherits from RawMixin and StringMixin, and uses FieldMeta as its metaclass.
    Configured for handling 'uuid4' formatted strings.
    """
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "uuid4"

    @property
    def _get_type(self) -> type[str]:
        return str

class URIField(RawMixin, StringMixin, metaclass=FieldMeta):
    """
    A field designed for URI strings.
    
    Inherits from RawMixin and StringMixin, with FieldMeta as its metaclass.
    It is specifically configured for 'uri' formatted strings, suitable for
    handling URIs.
    """
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "uri"
    
    @property
    def _get_type(self) -> type[str]:
        return str

class IPv4Field(RawMixin, StringMixin, metaclass=FieldMeta):
    """
    Represents a field for IPv4 address strings.
    
    Inherits from RawMixin and StringMixin, using FieldMeta as its metaclass.
    This field is pre-configured for 'ipv4' formatted strings, to handle IPv4 addresses.
    """
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "ipv4"
    
    @property
    def _get_type(self) -> type[str]:
        return str

class IPv6Field(RawMixin, StringMixin, metaclass=FieldMeta):
    """
    Designed for IPv6 address strings.
    
    Inherits from RawMixin and StringMixin, with FieldMeta as its metaclass.
    Configured specifically for 'ipv6' formatted strings, suitable for IPv6 address handling.
    """
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "ipv6"

    @property
    def _get_type(self) -> type[str]:
        return str
