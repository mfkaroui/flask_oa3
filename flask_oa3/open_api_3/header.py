from typing import Optional, ClassVar
from typing_extensions import Annotated
from pydantic import Field
from .component import Component, ComponentType

class Header(Component):
    component_type: ClassVar[ComponentType] = ComponentType.HEADER

    description: Annotated[Optional[str], Field(default=None, description="A brief description of the header. This could contain examples of use. CommonMark syntax MAY be used for rich text representation")]
    required: Annotated[Optional[bool], Field(default=None, description="Determines whether this header is mandatory. By default the behavior is false.")]
    deprecated: Annotated[Optional[bool], Field(default=None, description="Specifies that a header is deprecated and SHOULD be transitioned out of usage. Default value is false.")]

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Header Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#headerObject
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)