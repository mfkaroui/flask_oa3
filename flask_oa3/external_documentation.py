from typing import Optional
from pydantic import BaseModel, AnyUrl

class ExternalDocumentation(BaseModel):
    description: Optional[str] = None
    url: AnyUrl

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'External Documentation Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#external-documentation-object
        
        Returns:
            dict: The Open API schema
        """        
        schema = {
            "url": self.url
        }
        if self.description is not None:
            schema["description"] = self.description
        return schema