from __future__ import annotations
from typing import Optional, Annotated, Dict, Any
from pydantic import BaseModel, Field, validator
from .component import Component

class Reference(BaseModel):
    ref: Annotated[str, Field(alias="$ref", description="REQUIRED. The reference identifier. This MUST be in the form of a URI.")]
    summary: Annotated[Optional[str], Field(default=None, description="A short summary which by default SHOULD override that of the referenced component. If the referenced object-type does not allow a summary field, then this field has no effect.")]
    description: Annotated[Optional[str], Field(default=None, description="A description which by default SHOULD override that of the referenced component. CommonMark syntax MAY be used for rich text representation. If the referenced object-type does not allow a description field, then this field has no effect.")]

    @validator('summary', 'description')
    def check_optional_str_fields(cls, v):
        if v is not None and not isinstance(v, str):
            raise ValueError('The summary and description fields must be either None or a string.')
        return v

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Refence Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#referenceObject
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)
    
    @classmethod
    def from_component(cls, component: Component) -> Reference:
        """
        Creates a Reference instance from a given component.

        Args:
            component (Component): The component instance to create a Reference from.

        Returns:
            Reference: The created Reference instance.
        """
        return cls(ref=component.component_path, summary=None, description=None)