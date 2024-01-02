from __future__ import annotations
import inspect
from typing import Any, Dict, List, Union, Callable, get_type_hints
from docstring_parser import parse

from .open_api_3 import Responses, Operation, PathItem, ExternalDocumentation, Components
from .model import Model, ResponseModel

class View:
    ALLOWED_METHODS: List[str] = [
        "get",
        "put",
        "post",
        "delete",
        "options",
        "head",
        "patch",
        "trace"
    ]

    @classmethod
    def _validate_method(cls, method: Callable):
        """Validates that the method is allowed

        Args:
            method (Callable): The method to validate

        Raises:
            ValueError: If the method is not allowed
        """        
        
        type_hints = get_type_hints(method)
        if "return" not in type_hints:
            raise ValueError(f"Method {method.__name__} must have a return annotation")
        if type_hints["return"].__name__ == "Union":
            for union_type in type_hints["return"].__args__:
                if not issubclass(union_type, ResponseModel):
                    raise ValueError(f"Method {method.__name__} must have a return annotation of type ResponseModel")
        elif not issubclass(type_hints["return"], ResponseModel):
            raise ValueError(f"Method {method.__name__} must have a return annotation of type ResponseModel")
        if "__api_docs__" not in method.__dict__:
            method.__api_docs__ = {}

    @classmethod
    def get_all_methods(cls) -> Dict[str, Dict[str, Union[Callable, Dict[str, Any]]]]:
        methods = {}
        for func_name, func in inspect.getmembers(cls, inspect.isfunction):
            if func_name.lower() in cls.ALLOWED_METHODS:
                cls._validate_method(func)
                methods[func_name.lower()] = {
                    "function": func,
                    "type_hints": get_type_hints(func)
                }
        return methods
    
    @classmethod
    def produce_components(cls) -> Components:
        for method_name, method_data in cls.get_all_methods().items():
            if method_data["type_hints"]["return"].__name__ == "Union":
                for union_type in method_data["type_hints"]["return"].__args__:
                    pass

    @classmethod
    def produce_path_item(cls) -> PathItem:
        """Gets all methods defined that have a name listed in the allowed methods list

        Returns:
            Dict[str, Callable]: A dictionary that maps the name of a method to the method itself
        """        
        path_item = {}
        for func_name, func in inspect.getmembers(cls, inspect.isfunction):
            if func_name.lower() in cls.ALLOWED_METHODS:
                cls._validate_method(func)
                type_hints = get_type_hints(func)
                operation = {
                    "operationId": f"{cls.__name__}::{func_name}",
                    "responses": Responses(root={
                        str(response.__status_code__): response.produce_response()
                        for response in type_hints["return"].__args__
                    })
                }
                if func.__doc__ is not None:
                    parsed_doc_strings = parse(func.__doc__)
                    if parsed_doc_strings.short_description is not None:
                        operation["summary"] = parsed_doc_strings.short_description
                    if parsed_doc_strings.long_description is not None:
                        operation["description"] = parsed_doc_strings.long_description
                    if parsed_doc_strings.deprecation is not None:
                        operation["deprecated"] = True
                    external_documentation = {}
                    for doc_string_meta in parsed_doc_strings.meta:
                        if doc_string_meta.args[0].lower() == "external_documentation":
                            external_documentation_args = parse(doc_string_meta.description)
                            for external_documentation_meta in external_documentation_args.meta:
                                if external_documentation_meta.args[0].lower() == "url":
                                    external_documentation["url"] = external_documentation_meta.description
                                if external_documentation_meta.args[0].lower() == "description":
                                    external_documentation["description"] = external_documentation_meta.description
                    if len(external_documentation) > 0:
                        operation["external_documentation"] = ExternalDocumentation(**external_documentation)
                path_item[func_name.lower()] = Operation(**operation)
        if cls.__doc__ is not None:
            parsed_doc_strings = parse(cls.__doc__)
            if parsed_doc_strings.short_description is not None:
                path_item["summary"] = parsed_doc_strings.short_description
            if parsed_doc_strings.long_description is not None:
                path_item["description"] = parsed_doc_strings.long_description
        return PathItem(**path_item)
    