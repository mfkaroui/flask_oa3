import inspect
import functools
from typing import List, Union, Callable
from .errors import ReservedSpecificationExtentionError, PayloadModelAlreadyExistsError
from .model import Model
from .view import View
from .responses import BaseResponse, get_response_by_status_code
from .media_types import BaseMediaType, ApplicationJson

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
            x_key = key.replace("_", "-")
            x_key = x_key if x_key.startswith("x-") else f"x-{x_key}"
            if x_key.startswith("x-oai-") or x_key.startswith("x-oas-"):
                raise ReservedSpecificationExtentionError(f"Error with key {x_key}. Specification extentions that start with 'x-oai-' or 'x-oas-' are reserved for uses defined by the OpenAPI Initiative.")
            specification_extensions[x_key] = kwargs[key]
        return function(*args, **specification_extensions)
    return wrapper

@specification_extensions_support
def view_docs(
    summary: Union[str, None] = None,
    description: Union[str, None] = None,
    **specification_extentions
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
    def decorator(view):
        if not issubclass(view, View):
            raise TypeError('View_docs can only be used on a subclass of View')

        if summary is not None:
            view.__api_docs__["summary"] = summary
        if description is not None:
            view.__api_docs__["description"] = description
        view.__api_docs__.update(specification_extentions)
        return view
    return decorator

def tag(tags: List[str]):
    """Decorator that can be used to add tags either to each method in a view class 
    or to a single method in a view.

    Args:
        tags (List[str]): A list of tags for API documentation control.

    Raises:
        TypeError: Raised when the class being decorated is not a subclass of View
                  or when the object being decorated is neither a View subclass nor a method.

    Returns:
        The decorated class or method.
    """
    def _add_tags_to_method(method, tags):
        if "__api_docs__" not in method.__dict__:
            method.__api_docs__ = {}
        if "tags" not in method.__api_docs__:
            method.__api_docs__["tags"] = tags
        else:
            method.__api_docs__["tags"].extend(tags)
            method.__api_docs__["tags"] = list(set(method.__api_docs__["tags"]))

    def decorator(obj: Union[View, Callable]):
        if inspect.isclass(obj):
            if not issubclass(obj, View):
                raise TypeError('"tags" can only be used on a subclass of View')
            for _, method in obj._get_methods().items():
                _add_tags_to_method(method, tags)
        else:
            _add_tags_to_method(obj, tags)
        return obj
    return decorator

def response(description: str, model: Model, media_type: Union[str, BaseMediaType] = ApplicationJson, **kwargs):
    def decorator(obj: Union[View, Callable]):
        media_type_object = media_type(model)
        if len(kwargs) == 1 and "status_code" in kwargs:
            #only status code was defined, thus the intent is to look up a predefined status code
            response_object = get_response_by_status_code(kwargs["status_code"])
            if response_object is None:
                raise LookupError(f"A response could not be found with the status code {kwargs['status_code']}. Please define the response phrase and description to use this status code.")
            response_object = response_object(description)
        elif "status_code" not in kwargs or "phrase" not in kwargs:
            raise ValueError("To define a custom response the following arguments must be preset. status_code: int, phrase: str")
        else:
            class CustomResponse(BaseResponse):
                __STATUS_CODE__: int = kwargs["status_code"]
                __PHRASE__: str = kwargs["phrase"]
            response_object = CustomResponse(description)
        response_object.add_media_type(media_type_object)
        if inspect.isclass(obj):
            if not issubclass(obj, View):
                raise TypeError('"response" can only be used on a subclass of View')
            for _, method in obj._get_methods().items():
                method._register_response(response_object)
        else:
            View._bind_method_schema(obj)
            View._bind_register_response(obj)
            obj._register_response(response_object)
        return obj
    return decorator
