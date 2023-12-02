from enum import StrEnum
from typing import ClassVar, Optional
from pydantic import BaseModel, Field

class ComponentType(StrEnum):
    SCHEMA = "schemas"
    RESPONSE = "responses"
    PARAMETER = "parameters" #missing
    EXAMPLE = "examples"
    REQUEST_BODY = "requestBodies" #missing
    HEADER = "headers"
    SECURITY_SCHEME = "securitySchemes" #missing
    LINK = "links" #missing
    CALLBACK = "callbacks" #missing
    PATH_ITEM = "pathItems" #missing

class Component(BaseModel):
    component_type: ClassVar[Optional[ComponentType]] = None

    @property
    def component_path(cls) -> str:
        if cls.component_type is None:
            raise ValueError("A component type was not set")
        return f"#/components/{cls.component_type.value}/{cls.__name__}"