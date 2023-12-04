from typing import Optional, Annotated, Dict
from pydantic import BaseModel, Field, AnyUrl
from .oauth_flow import OAuthFlow

class OAuthFlows(BaseModel):
    implicit: Annotated[Optional[OAuthFlow], Field(default=None, description="Configuration for the OAuth Implicit flow")]
    password: Annotated[Optional[OAuthFlow], Field(default=None, description="Configuration for the OAuth Resource Owner Password flow")]
    client_credentials: Annotated[Optional[OAuthFlow], Field(default=None, alias="clientCredentials", description="Configuration for the OAuth Client Credentials flow. Previously called application in OpenAPI 2.0.")]
    authorization_code: Annotated[Optional[OAuthFlow], Field(default=None, alias="authorizationCode", description="Configuration for the OAuth Authorization Code flow. Previously called accessCode in OpenAPI 2.0.")]

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'OAuth Flows Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#oauth-flows-object
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)