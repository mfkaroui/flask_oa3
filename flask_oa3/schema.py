from __future__ import annotations
from typing import Annotated, Any, Dict, Optional, ClassVar
from pydantic import BaseModel, Field
from copy import deepcopy

from .discriminator import Discriminator
from .external_documentation import ExternalDocumentation
from .xml import XML

class Schema(BaseModel):
    discriminator: Annotated[Optional[Discriminator], Field(defualt=None, description="Adds support for polymorphism. The discriminator is an object name that is used to differentiate between other schemas which may satisfy the payload description. See Composition and Inheritance for more details.")] 
    xml: Annotated[Optional[XML], Field(default=None, description="This MAY be used only on properties schemas. It has no effect on root schemas. Adds additional metadata to describe the XML representation of this property.")]
    external_documentation: Annotated[Optional[ExternalDocumentation], Field(default=None, description="Additional external documentation for this schema.")]

    @property
    def oa3_schema(self):
        """Constructs the Open API 'Schema Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#schemaObject
        
        Returns:
            dict: The Open API schema
        
        Notes:
            if "$defs" is defined then they must be popped out and ensured that they exist in the components object
        """   
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)
