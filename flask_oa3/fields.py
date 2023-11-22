from typing import Any, List, Union

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
        
        def new_keyword_schema():
            keyword_schema = {}
            for keyword_schemas_classmethod in keyword_schemas_classmethods:
                keyword_schema.update(keyword_schemas_classmethod())
            return keyword_schema
        
        attrs["keyword_schema"] = new_keyword_schema

        return super_new(cls, name, bases, attrs, **kwargs)

    @classmethod
    def __prepare__(metacls, name, bases):
        return {}

class RawMixin:
    @classmethod
    def keyword_schema(cls):
        return {}

class BaseMixin(RawMixin):
    def __init__(self, description: Union[str, None] = None, required: bool = False, allow_null: bool = False):
        """Contains general initializers for keywords related to all fields

        Args:
            description (Union[str, None], optional): _description_. Defaults to None.
            required (bool, optional): _description_. Defaults to False.
            allow_null (bool, optional): _description_. Defaults to False.
        """        
        self.description = description
        self.required = required
    
    @classmethod
    def keyword_schema(cls):
        return {
            "description": "description",
            "required": "required",
            "allow_null": "nullable"
        }

class NumberMixin(RawMixin):
    def __init__(self, minimum: Union[int, None] = None, maximum: Union[int, None] = None, exclusive_minimum: bool = False, exclusive_maximum: bool = False, multiple_of: Union[int, None] = None):
        """Contains initializers for keywords related to number type fields

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

class NestedField(BaseMixin, metaclass=FieldBase):
    from .model import Model
    __FIELD_TYPE__ = "object"

    def __init__(self, model: Model, **kwargs):
        """References another model to be used as a field.

        Args:
            model (Union[Model, List[Model]]): A model to reference.
        """        
        pass

class ListField(BaseMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = "list"

    def __init__(self, **kwargs):
        pass

class StringField(BaseMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = "string"

    def __init__(self, **kwargs):
        pass

class BooleanField(BaseMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = "boolean"

    def __init__(self, **kwargs):
        pass

class IntegerField(BaseMixin, NumberMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = "integer"
    def __init__(self, **kwargs):
        pass

class FloatField(BaseMixin, NumberMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = "number"

    def __init__(self, **kwargs):
        pass

class ArbitraryField(BaseMixin, NumberMixin, metaclass=FieldBase):
    __FIELD_TYPE__ = "number"

    def __init__(self, **kwargs):

        pass