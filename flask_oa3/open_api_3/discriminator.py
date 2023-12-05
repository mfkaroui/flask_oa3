from typing import Optional, Annotated, Dict
from pydantic import BaseModel, Field

class Discriminator(BaseModel):
    property_name: Annotated[str, Field(alias="propertyName", description="REQUIRED. The name of the property in the payload that will hold the discriminator value.")]
    mapping: Annotated[Optional[Dict[str, str]], Field(default=None, description="An object to hold mappings between payload values and schema names or references.")]

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Discriminator Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#discriminatorObject
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)