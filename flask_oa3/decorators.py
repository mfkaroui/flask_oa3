import functools
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