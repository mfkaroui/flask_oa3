
class FieldMeta(type):  
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
        attrs["_meta"] = cls

        return super_new(cls, name, bases, attrs, **kwargs)
