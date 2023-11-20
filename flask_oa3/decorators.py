import functools
from typing import Union
from .errors import ReservedSpecificationExtentionError

def specification_extensions_support(function):
    """A decorator to allow for extensions to the OpenAPI Schema. The value can be null, a primitive, an array or an object.
    
    Args:
        function (_type_): The wrapped function

    Raises:
        ReservedSpecificationExtentionError: Field names beginning x-oai- and x-oas- are reserved for uses defined by the OpenAPI Initiative

    Returns:
        _type_: The wrapper function to be called
    """    
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        specification_extensions = {}
        for key in kwargs:
            x_key = (key if key.startswith("x-") else f"x-{key}").replace("_", "-")
            if x_key.startswith("x-oai-") or x_key.startswith("x-oas-"):
                raise ReservedSpecificationExtentionError(f"Error with key {x_key}. Specification extentions that start with 'x-oai-' or 'x-oas-' are reserved for uses defined by the OpenAPI Initiative.")
            specification_extensions[x_key] = kwargs[key]
        return function(*args, **specification_extensions)
    return wrapper

def view_docs(
    summary: Union[str, None] = None,
    description: Union[str, None] = None,
):
    """Add global documentation to the view

    Args:
        summary (Union[str, None], optional): An optional, string summary, intended to apply to all operations in this path. Defaults to None.
        description (Union[str, None], optional): An optional, string description, intended to apply to all operations in this path. CommonMark syntax MAY be used for rich text representation. Defaults to None.
    
    Raises:
        TypeError: Raised when the class being decorated is not a subclass of view

    Returns:
        _type_: The decorated class
    """    
    from .view import View
    def decorator(cls):
        if not issubclass(cls, View):
            raise TypeError('View_docs can only be used on a subclass of View')

        if summary is not None:
            cls.__api_docs__["summary"] = summary
        if description is not None:
            cls.__api_docs__["description"] = description
        return cls
    return decorator