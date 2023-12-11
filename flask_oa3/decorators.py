import inspect
import functools
from typing import List, Union, Callable
from .errors import ReservedSpecificationExtentionError, PayloadModelAlreadyExistsError
from .model import Model
from .view import View
from .open_api_3.response import Response, get_response_by_status_code
from .open_api_3.media_type import MediaType, MediaTypeApplicationJson


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

def response(description: str, model: Model, media_type: Union[str, MediaType] = MediaTypeApplicationJson, **kwargs):
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
            class CustomResponse(Response):
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
