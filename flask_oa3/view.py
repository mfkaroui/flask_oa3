import inspect
from typing import Dict, List
from .base import Base
from .model import Model
from .errors import ModelAlreadyRegisteredError

class View:
    ALLOWED_METHODS: List[str] = [
        "get",
        "post",
        "put",
        "patch",
        "delete"
    ]

    @classmethod
    def _get_methods(cls):
        methods = {}
        for func_name, func in inspect.getmembers(cls, inspect.isfunction):
            if func_name.lower() in cls.ALLOWED_METHODS:
                methods[func_name] = func
        return methods