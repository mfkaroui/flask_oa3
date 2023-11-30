from typing import Optional
from typing_extensions import Annotated
from pydantic import BaseModel, AnyUrl, Field

class ExternalDocumentation(BaseModel):
    url: Annotated[AnyUrl, Field(description="REQUIRED. The URL for the target documentation. This MUST be in the form of a URL.")]
    description: Annotated[Optional[str], Field(default=None, description="A description of the target documentation. CommonMark syntax MAY be used for rich text representation.")]

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'External Documentation Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#external-documentation-object
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)