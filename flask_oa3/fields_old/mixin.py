from typing import Union, Any

from .field_types import FieldType

class BaseField:
    __FIELD_TYPE__: Union[FieldType, None] = None

    @classmethod
    def keyword_schema(cls) -> dict:
        """Converts between field properties and their respective Open API keyword names.

        Returns:
            dict: A conversion dictionary.
        """        
        return {}

    @property
    def _get_type(self) -> type:
        raise NotImplementedError("Should be implemented by derived class")

    @property
    def schema(self) -> dict:
        if self.__FIELD_TYPE__ is None or not isinstance(self.__FIELD_TYPE__, FieldType):
            raise TypeError("The field type does not match OpenAPI Specifications")
        if self.__FIELD_TYPE__ == FieldType.NO_TYPE:
            schema = {}
        else:
            schema = {
                "type": self.__FIELD_TYPE__.value
            }
        for property_name, keyword in self.keyword_schema().items():
            if self.__dict__[property_name] is not None:
                schema[keyword] = self.__dict__[property_name]
        return schema

class RawMixin(BaseField):
    """Contains keywords and options that are available to all field types"""    
    def __init__(self, description: Union[str, None] = None, required: bool = False, allow_null: Union[bool, None] = None):
        """Initializers for keywords related to all fields.

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

class NumberMixin(BaseField):
    """Contains keywords and options that are available to number field types"""    
    def __init__(self, minimum: Union[int, None] = None, maximum: Union[int, None] = None, exclusive_minimum: Union[bool, None] = None, exclusive_maximum: Union[bool, None] = None, multiple_of: Union[int, None] = None):
        """Initializers for keywords related to number type fields.

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

class StringMixin(BaseField):
    """Contains keywords and options that are available to string field types"""    

    def __init__(self, min_length: Union[int, None] = None, max_length: Union[int, None] = None, pattern: Union[str, None] = None, format: Union[str, None] = None):
        """Initializers for keywords related to string type fields.

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
