import inspect
from typing import Dict, List, Union, Callable
from .model import Model
from .errors import ModelAlreadyRegisteredError

class View:
    ALLOWED_METHODS: List[str] = [
        "get",
        "post",
        "put",
        "patch",
        "delete",
        "options",
        "head"
    ]
    __api_docs__: Dict[str, str] = {}

    @classmethod
    def _get_methods(cls) -> Dict[str, Callable]:
        methods = {}
        for func_name, func in inspect.getmembers(cls, inspect.isfunction):
            if func_name.lower() in cls.ALLOWED_METHODS:
                methods[func_name] = func
        return methods
    
    @classmethod
    def schema(cls):
        methods = cls._get_methods()
        schema = {
            method: {
                "tags": [method],
                "operationId": methods[method].__qualname__
            } for method in methods
        }
        schema.update(cls.__api_docs__)
        return schema