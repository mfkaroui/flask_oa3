import functools
from .errors import ReservedSpecificationExtentionError

def specification_extensions_support(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        specification_extensions = {}
        for key in kwargs:
            x_key = key if key.startswith("x-") else f"x-{key}"
            if x_key.startswith("x-oai-") or x_key.startswith("x-oas-"):
                raise ReservedSpecificationExtentionError(f"Error with key {x_key}. Specification extentions that start with 'x-oai-' or 'x-oas-' are reserved for uses defined by the OpenAPI Initiative.")
            specification_extensions[x_key] = specification_extensions[key]
        return function(*args, **specification_extensions)
    return wrapper