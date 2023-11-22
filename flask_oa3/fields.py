from typing import Any, List, Union
from enum import StrEnum

class FieldType(StrEnum):
    STRING = "string"
    NUMBER = "number"
    INTEGER = "integer"
    BOOLEAN = "boolean"
    ARRAY = "array"
    OBJECT = "object"

class FieldBase(type):  
    def __new__(cls, name, bases, attrs, **kwargs):
        super_new = super().__new__
        derived_constructor = None
        derived_constructor_annotations = {}
        constructors = []
        constructor_annotations = {}
        keyword_schemas_classmethods = []
        
        if "__init__" in attrs:
            derived_constructor = attrs["__init__"]
            derived_constructor_annotations = attrs["__init__"].__annotations__
        
        if "keyword_schema" in attrs:
            keyword_schemas_classmethods.append(attrs["keyword_schema"])

        for base in bases:
            constructors.append(base.__init__)
            base.__init__.__class_name__ = base.__name__
            constructor_annotations[base.__name__] = base.__init__.__annotations__
            keyword_schemas_classmethods.append(base.keyword_schema)

        def __new__init__(self, *args, **kwargs):
            for constructor in reversed(constructors):
                init_kwargs = {key: kwargs[key] for key in kwargs if key in constructor_annotations[constructor.__class_name__]}
                constructor(self, **init_kwargs)
            if derived_constructor is not None:
                init_kwargs = {key: kwargs[key] for key in kwargs if key in derived_constructor_annotations}
                derived_constructor(self, *args, **init_kwargs)
        attrs["__init__"] = __new__init__
        
        def new_keyword_schema(*args):
            keyword_schema = {}
            for keyword_schemas_classmethod in keyword_schemas_classmethods:
                keyword_schema.update(keyword_schemas_classmethod())
            return keyword_schema
        
        attrs["keyword_schema"] = new_keyword_schema

        return super_new(cls, name, bases, attrs, **kwargs)

class BaseMixin:
    __FIELD_TYPE__: Union[FieldType, None] = None

    @classmethod
    def keyword_schema(cls) -> dict:
        """Converts between field properties and their respective Open API keyword names.

        Returns:
            dict: A conversion dictionary.
        """        
        return {}

    def validate(self, data: Any):
        """Validates data against the expected type

        Args:
            data (Any): The data to validate

        Raises:
            NotImplementedError: This error flags that the derived class has not implemented a validator yet and should do so.
        """        
        raise NotImplementedError("Validation is not implemented in the BaseMixin class. The field class should override this method.")

    @property
    def schema(self) -> dict:
        if self.__FIELD_TYPE__ is None or not isinstance(self.__FIELD_TYPE__, FieldType):
            raise TypeError("The field type does not match OpenAPI Specifications")
        schema = {
            "type": self.__FIELD_TYPE__.value
        }
        for property_name, keyword in self.keyword_schema().items():
            if self.__dict__[property_name] is not None:
                schema[keyword] = self.__dict__[property_name]
        return schema

class RawMixin(BaseMixin):
    def __init__(self, description: Union[str, None] = None, required: bool = False, allow_null: Union[bool, None] = None):
        """Contains general initializers for keywords related to all fields.

        Args:
            description (Union[str, None], optional): _description_. Defaults to None.
            required (bool, optional): _description_. Defaults to False.
            allow_null (bool, optional): _description_. Defaults to False.
        """        
        self.description = description
        self.required = required
        self.allow_null = allow_null
    
    @classmethod
    def keyword_schema(cls):
        return {
            "description": "description",
            "allow_null": "nullable"
        }

class NumberMixin(BaseMixin):
    def __init__(self, minimum: Union[int, None] = None, maximum: Union[int, None] = None, exclusive_minimum: Union[bool, None] = None, exclusive_maximum: Union[bool, None] = None, multiple_of: Union[int, None] = None):
        """Contains initializers for keywords related to number type fields.

        Args:
            minimum (Union[int, None], optional): Minimum boundary of the number. Defaults to None.
            maximum (Union[int, None], optional): Maximum boundary of the number. Defaults to None.
            exclusive_minimum (bool, optional): Determines if the minimum boundary is exclusive or inclusive. Defaults to False.
            exclusive_maximum (bool, optional): Determines if the maximum boundary is exclusive or inclusive. Defaults to False.
            multiple_of (Union[int, None], optional): Specifies that the number must be the multiple of this keyword. Defaults to None.
        """        
        self.minimum = minimum
        self.maximum = maximum
        self.exclusive_minimum = exclusive_minimum
        self.exclusive_maximum = exclusive_maximum
        self.multiple_of = multiple_of
    
    @classmethod
    def keyword_schema(cls):
        return {
            "minimum": "minimum",
            "maximum": "maximum",
            "exclusive_minimum": "exclusiveMinimum",
            "exclusive_maximum": "exclusiveMaximum",
            "multiple_of": "multipleOf"
        }

class StringMixin(BaseMixin):
    def __init__(self, min_length: Union[int, None] = None, max_length: Union[int, None] = None, pattern: Union[str, None] = None, format: Union[str, None] = None):
        """Contains initializers for keywords related to string type fields.

        Args:
            min_length (Union[int, None], optional): Minimum amount of characters in the string. Defaults to None.
            max_length (Union[int, None], optional): Maximum amount of characters in the string. Defaults to None.
            pattern (Union[str, None], optional): Lets you define a regular expression template for the string value. Only the values that match this template will be accepted. The regular expression syntax used is from JavaScript (more specifically, ECMA 262). Defaults to None.
            format (Union[str, None], optional): An optional format modifier serves as a hint at the contents and format of the string.
        """        
        self.min_length = min_length
        self.max_length = max_length
        self.pattern = pattern
        self.format = format
    
    @classmethod
    def keyword_schema(cls):
        return {
            "min_length": "minLength",
            "max_length": "maxLength",
            "pattern": "pattern",
            "format": "format"
        }

class NestedField(RawMixin, metaclass=FieldBase):
    from .model import Model #importing within class to avoid circular dependancies
    __FIELD_TYPE__ = FieldType.OBJECT

    def __init__(self, model: Model, **kwargs):
        """References another model to be used as a field.

        Args:
            model (Union[Model, List[Model]]): A model to reference.
        """        
        pass

class ListField(RawMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = FieldType.ARRAY

    def __init__(self, **kwargs):
        pass

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

class BooleanField(RawMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = FieldType.BOOLEAN

    def __init__(self, **kwargs):
        pass

class IntegerField(RawMixin, NumberMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = FieldType.INTEGER
    def __init__(self, **kwargs):
        pass

class FloatField(RawMixin, NumberMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = FieldType.NUMBER

    def __init__(self, **kwargs):
        pass

class ArbitraryField(RawMixin, NumberMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = FieldType.NUMBER

    def __init__(self, **kwargs):

        pass