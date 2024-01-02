from __future__ import annotations
from typing import Optional, Generic, TypeVar
from typing_extensions import Annotated
from pydantic import BaseModel, Field, computed_field
from .component import Component

ComponentType = TypeVar("ComponentType", bound=Component)

class Reference(BaseModel, Generic[ComponentType]):
    component: ComponentType

    summary: Annotated[Optional[str], Field(default=None, description="A short summary which by default SHOULD override that of the referenced component. If the referenced object-type does not allow a summary field, then this field has no effect.")]
    description: Annotated[Optional[str], Field(default=None, description="A description which by default SHOULD override that of the referenced component. CommonMark syntax MAY be used for rich text representation. If the referenced object-type does not allow a description field, then this field has no effect.")]

    class Config:
        exclude = [
            "component"
        ]


    @computed_field(alias="$ref", description="REQUIRED. The reference identifier. This MUST be in the form of a URI.")
    def reference(self) -> str:
        return f"{self.component.component_path()}/{self.component.component_name}"

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Refence Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#referenceObject
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)
