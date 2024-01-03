from enum import Enum
from typing import ClassVar, Optional
from pydantic import BaseModel, ConfigDict, model_serializer

class ComponentType(Enum):
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

    @model_serializer(mode="wrap")
    def serialize_component(self, handler):
        exclude = ["component_type", "component_name"]
        d = handler(self)
        d = {k:v for k, v in d.items() if k not in exclude}
        return d

    @property
    def component_name(self) -> str:
        raise NotImplementedError("A component name must be implemented")

    @classmethod
    def component_path(cls) -> str:
        if cls.component_type is None:
            raise ValueError("A component type was not set")
        return f"#/components/{cls.component_type.value}"