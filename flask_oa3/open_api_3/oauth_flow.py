from typing import Optional, Annotated, Dict
from pydantic import BaseModel, Field, AnyUrl

class OAuthFlow(BaseModel):
    authorization_url: Annotated[Optional[AnyUrl], Field(default=None, alias="authorizationUrl", description="REQUIRED. The authorization URL to be used for this flow. This MUST be in the form of a URL. The OAuth2 standard requires the use of TLS.")]
    token_url: Annotated[Optional[AnyUrl], Field(default=None, alias="tokenUrl", description="REQUIRED. The token URL to be used for this flow. This MUST be in the form of a URL. The OAuth2 standard requires the use of TLS.")]
    refresh_url: Annotated[Optional[AnyUrl], Field(default=None, alias="refreshUrl", description="The URL to be used for obtaining refresh tokens. This MUST be in the form of a URL. The OAuth2 standard requires the use of TLS.")]
    scopes: Annotated[Optional[Dict[str, str]], Field(default=None, description="REQUIRED. The available scopes for the OAuth2 security scheme. A map between the scope name and a short description for it. The map MAY be empty.")]

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'OAuth Flow Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#oauth-flow-object
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)