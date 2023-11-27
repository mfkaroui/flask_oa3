from .metaclass import FieldBase
from .field_types import FieldType
from .mixin import RawMixin, StringMixin

class StringField(RawMixin, StringMixin, metaclass=FieldBase):
    """
    Represents a basic string field without any specific formatting.
    
    Inherits from RawMixin and StringMixin to provide basic string handling
    functionality. It uses FieldBase as its metaclass.
    """
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        pass

class DateField(RawMixin, StringMixin, metaclass=FieldBase):
    """
    Represents a field specifically formatted for date values.
    
    Inherits from RawMixin and StringMixin, and utilizes FieldBase as its metaclass.
    It is pre-configured with a 'date' format.
    """
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "date"

class DateTimeField(RawMixin, StringMixin, metaclass=FieldBase):
    """
    Represents a field for date-time values.
    
    Inherits from RawMixin and StringMixin, and uses FieldBase as its metaclass.
    Pre-configured with a 'date-time' format to handle datetime values.
    """
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "date-time"

class PasswordField(RawMixin, StringMixin, metaclass=FieldBase):
    """
    A field designed for password strings.
    
    Inherits from RawMixin and StringMixin. Utilizes FieldBase as its metaclass.
    This field type is pre-configured with a 'password' format, suitable for
    password handling and validation.
    """
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "password"

class Base64EncodedField(RawMixin, StringMixin, metaclass=FieldBase):
    """
    Field for handling Base64 encoded strings.
    
    Inherits from RawMixin and StringMixin, with FieldBase as its metaclass.
    This field is specifically formatted for 'byte' type strings, typically
    used for Base64 encoded data.
    """
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "byte"

class EmailField(RawMixin, StringMixin, metaclass=FieldBase):
    """
    A field tailored for email address strings.
    
    Inherits from RawMixin and StringMixin, and uses FieldBase as its metaclass.
    It is configured with an 'email' format to validate email addresses.
    """
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "email"

class UUID4Field(RawMixin, StringMixin, metaclass=FieldBase):
    """
    Represents a field for UUID version 4 strings.
    
    Inherits from RawMixin and StringMixin, and uses FieldBase as its metaclass.
    Configured for handling 'uuid4' formatted strings.
    """
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "uuid4"

class URIField(RawMixin, StringMixin, metaclass=FieldBase):
    """
    A field designed for URI strings.
    
    Inherits from RawMixin and StringMixin, with FieldBase as its metaclass.
    It is specifically configured for 'uri' formatted strings, suitable for
    handling URIs.
    """
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "uri"

class IPv4Field(RawMixin, StringMixin, metaclass=FieldBase):
    """
    Represents a field for IPv4 address strings.
    
    Inherits from RawMixin and StringMixin, using FieldBase as its metaclass.
    This field is pre-configured for 'ipv4' formatted strings, to handle IPv4 addresses.
    """
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "ipv4"

class IPv6Field(RawMixin, StringMixin, metaclass=FieldBase):
    """
    Designed for IPv6 address strings.
    
    Inherits from RawMixin and StringMixin, with FieldBase as its metaclass.
    Configured specifically for 'ipv6' formatted strings, suitable for IPv6 address handling.
    """
    __FIELD_TYPE__ = FieldType.STRING

    def __init__(self, **kwargs):
        self.format = "ipv6"
