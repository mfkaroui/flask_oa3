from pydantic import BaseModel, Field, AnyUrl
from typing import Optional
from typing_extensions import Annotated

class License(BaseModel):
    name: Annotated[str, Field(description="REQUIRED. The license name used for the API.")]
    identifier: Annotated[Optional[str], Field(default=None, description="An SPDX license expression for the API. The identifier field is mutually exclusive of the url field.")]
    url: Annotated[Optional[AnyUrl], Field(default=None, description="A URL to the license used for the API. This MUST be in the form of a URL. The url field is mutually exclusive of the identifier field.")]

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'License Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#license-object
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True)