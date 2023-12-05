from typing import Optional, Annotated
from pydantic import BaseModel, Field, validator

from .external_documentation import ExternalDocumentation

class Tag(BaseModel):
    name: Annotated[str, Field(description="REQUIRED. The name of the tag.")]
    description: Annotated[Optional[str], Field(default=None, description="A description for the tag. CommonMark syntax MAY be used for rich text representation. Defaults to None.")]
    external_documentation: Annotated[Optional[ExternalDocumentation], Field(default=None, alias="externalDocs", description="Additional external documentation for this tag. Defaults to None.")]

    @validator('name')
    def check_name(cls, v):
        if not v:
            raise ValueError('The name of the tag is required and cannot be empty.')
        return v

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Tag Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#tag-object
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)