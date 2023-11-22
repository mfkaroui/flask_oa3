from typing import Any, List, Union

class FieldBase(type):  
    def __new__(cls, name, bases, attrs, **kwargs):
        super_new = super().__new__
        derived_constructor = None
        derived_constructor_annotations = {}
        constructors = []
        constructor_annotations = {}
        if "__init__" in attrs:
            derived_constructor = attrs["__init__"]
            derived_constructor_annotations = attrs["__init__"].__annotations__
        for base in bases:
            constructors.append(base.__init__)
            base.__init__.__class_name__ = base.__name__
            constructor_annotations[base.__name__] = base.__init__.__annotations__
        def __new__init__(self, *args, **kwargs):
            for constructor in reversed(constructors):
                init_kwargs = {key: kwargs[key] for key in kwargs if key in constructor_annotations[constructor.__class_name__]}
                constructor(self, **init_kwargs)
            if derived_constructor is not None:
                init_kwargs = {key: kwargs[key] for key in kwargs if key in derived_constructor_annotations}
                derived_constructor(self, *args **init_kwargs)
        attrs["__init__"] = __new__init__
        return super_new(cls, name, bases, attrs, **kwargs)

    @classmethod
    def __prepare__(metacls, name, bases):
        return {}

class BaseMixin:
    def __init__(self, description: Union[str, None] = None, required: bool = False, allow_null: bool = False):
        """Contains general initializers for keywords related to all fields

        Args:
            description (Union[str, None], optional): _description_. Defaults to None.
            required (bool, optional): _description_. Defaults to False.
            allow_null (bool, optional): _description_. Defaults to False.
        """        
        self.description = description
        self.required = required
        self.allow_null = allow_null

class NumberMixin:
    def __init__(self, minimum: Union[int, None] = None, maximum: Union[int, None] = None, exclusive_minimum: bool = False, exclusive_maximum: bool = False, multiple_of: int = 1):
        """Contains initializers for keywords related to number type fields

        Args:
            minimum (Union[int, None], optional): _description_. Defaults to None.
            maximum (Union[int, None], optional): _description_. Defaults to None.
            exclusive_minimum (bool, optional): _description_. Defaults to False.
            exclusive_maximum (bool, optional): _description_. Defaults to False.
            multiple_of (int, optional): _description_. Defaults to 1.
        """        
        self.minimum = minimum
        self.maximum = maximum
        self.exclusive_minimum = exclusive_minimum
        self.exclusive_maximum = exclusive_maximum
        self.multiple_of = multiple_of

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