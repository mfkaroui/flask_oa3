from __future__ import annotations
from typing import Annotated, Any, Dict, Optional, ClassVar
from pydantic import BaseModel, Field, AnyUrl
from copy import deepcopy

from .discriminator import Discriminator
from .external_documentation import ExternalDocumentation

class XML(BaseModel):
    name: Annotated[Optional[str], Field(default=None, description="Replaces the name of the element/attribute used for the described schema property. When defined within items, it will affect the name of the individual XML elements within the list. When defined alongside type being array (outside the items), it will affect the wrapping element and only if wrapped is true. If wrapped is false, it will be ignored.")]
    namespace: Annotated[Optional[AnyUrl], Field(default=None, description="The URI of the namespace definition. This MUST be in the form of an absolute URI.")]
    prefix: Annotated[Optional[str], Field(default=None, description="The prefix to be used for the name.")]
    attribute: Annotated[Optional[bool], Field(default=None, description="Declares whether the property definition translates to an attribute instead of an element. Default value is false.")]
    wrapped: Annotated[Optional[bool], Field(default=None, description="MAY be used only for an array definition. Signifies whether the array is wrapped (for example, <books><book/><book/></books>) or unwrapped (<book/><book/>). Default value is false. The definition takes effect only when defined alongside type being array (outside the items).")]

    @property
    def oa3_schema(self):
        """Constructs the Open API 'XML Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#xmlObject
        
        Returns:
            dict: The Open API schema
        """   
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)
