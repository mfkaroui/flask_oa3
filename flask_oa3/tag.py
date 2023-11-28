from typing import Optional
from pydantic import BaseModel

from .external_documentation import ExternalDocumentation

class Tag(BaseModel):
    name: str #REQUIRED. The name of the tag.
    description: Optional[str] = None #A description for the tag. CommonMark syntax MAY be used for rich text representation. Defaults to None.
    external_documentation: Optional[ExternalDocumentation] = None #Additional external documentation for this tag. Defaults to None.

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Tag Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#tag-object
        
        Returns:
            dict: The Open API schema
        """        
        schema = {
            "name": self.url
        }
        if self.description is not None:
            schema["description"] = self.description
        if self.external_documentation is not None:
            schema["externalDocs"] = self.external_documentation.oa3_schema
        return schema