from enum import StrEnum
from typing import ClassVar, Optional
from pydantic import BaseModel, Field

class ComponentType(StrEnum):
    SCHEMA = "schemas"
    RESPONSE = "responses"
    PARAMETER = "parameters"
    EXAMPLE = "examples"
    REQUEST_BODY = "requestBodies" #missing
    HEADER = "headers"
    SECURITY_SCHEME = "securitySchemes" #missing
    LINK = "links" #missing
    CALLBACK = "callbacks" #missing
    PATH_ITEM = "pathItems" #missing

class Component(BaseModel):
    component_type: ClassVar[Optional[ComponentType]] = None
    
    @classmethod
    def component_name(cls) -> str:
        return cls.__name__

    @classmethod
    def component_path(cls) -> str:
        if cls.component_type is None:
            raise ValueError("A component type was not set")
        return f"#/components/{cls.component_type.value}"