from __future__ import annotations
from typing import Annotated, Optional, ClassVar
from pydantic import Field, AnyUrl

from .component import Component, ComponentType
from .discriminator import Discriminator
from .external_documentation import ExternalDocumentation
from .xml import XML

class Schema(Component):
    component_type: ClassVar[ComponentType] = ComponentType.SCHEMA

    discriminator: Annotated[Optional[Discriminator], Field(defualt=None, description="Adds support for polymorphism. The discriminator is an object name that is used to differentiate between other schemas which may satisfy the payload description. See Composition and Inheritance for more details.")] 
    xml: Annotated[Optional[XML], Field(default=None, description="This MAY be used only on properties schemas. It has no effect on root schemas. Adds additional metadata to describe the XML representation of this property.")]
    external_documentation: Annotated[Optional[ExternalDocumentation], Field(default=None, description="Additional external documentation for this schema.")]
    json_schema_dialect: Annotated[Optional[AnyUrl], Field(default=None, alias="$schema", description="The $schema keyword MAY be present in any root Schema Object, and if present MUST be used to determine which dialect should be used when processing the schema. This allows use of Schema Objects which comply with other drafts of JSON Schema than the default Draft 2020-12 support. Tooling MUST support the OAS dialect schema id, and MAY support additional values of $schema.")]

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
