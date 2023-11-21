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
    def _bind_method_schema(cls, function: Callable):
        """Generates a callable function that will be bound to a defined function. The bound method will produce the schema for the operation.

        Args:
            function (Callable): The allowed method to bind to.

        """        
        if "__api_docs__" not in function.__dict__:
            function.__api_docs__ = {}
        def method_schema() -> dict:
            """Constructs the Open API 'Operation Object' according to specifications

            Returns:
                dict: The Open API schema
            """            
            schema = {
                "operationId": function.__qualname__.replace(".", "::").replace("<", "__").replace(">", "__")
            }
            if "tags" in function.__api_docs__:
                schema["tags"] = function.__api_docs__["tags"]
            if "summary" in function.__api_docs__:
                schema["summary"] = function.__api_docs__["summary"]
            if "description" in function.__api_docs__:
                schema["description"] = function.__api_docs__["description"]
            if "external_docs" in function.__api_docs__:
                schema["externalDocs"] = function.__api_docs__["external_docs"].schema()
            if "deprecated" in function.__api_docs__:
                schema["deprecated"] = function.__api_docs__["deprecated"]
            return schema
        function.__dict__["schema"] = method_schema

    @classmethod
    def _get_methods(cls) -> Dict[str, Callable]:
        """Gets all methods defined that have a name listed in the allowed methods list

        Returns:
            Dict[str, Callable]: A dictionary that maps the name of a method to the method itself
        """        
        methods = {}
        for func_name, func in inspect.getmembers(cls, inspect.isfunction):
            if func_name.lower() in cls.ALLOWED_METHODS:
                if "schema" not in func.__dict__:
                    cls._bind_method_schema(func)
                methods[func_name] = func
        return methods
    
    @classmethod
    def schema(cls) -> dict:    
        """Constructs the Open API 'Path Item Object' according to specifications

        Returns:
            dict: The Open API schema
        """        
        methods = cls._get_methods()
        schema = {
            method: methods[method].schema() for method in methods
        }
        schema.update(cls.__api_docs__)
        return schema