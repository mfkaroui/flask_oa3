from __future__ import annotations
from typing import Optional, Annotated
from pydantic import BaseModel, Field, model_validator, ConfigDict

from .oauth_flow import OAuthFlow
from .decorators import specification_extensions_support

@specification_extensions_support
class OAuthFlows(BaseModel):
    implicit: Annotated[Optional[OAuthFlow], Field(default=None, description="Configuration for the OAuth Implicit flow")]
    password: Annotated[Optional[OAuthFlow], Field(default=None, description="Configuration for the OAuth Resource Owner Password flow")]
    client_credentials: Annotated[Optional[OAuthFlow], Field(default=None, alias="clientCredentials", description="Configuration for the OAuth Client Credentials flow. Previously called application in OpenAPI 2.0.")]
    authorization_code: Annotated[Optional[OAuthFlow], Field(default=None, alias="authorizationCode", description="Configuration for the OAuth Authorization Code flow. Previously called accessCode in OpenAPI 2.0.")]

    model_config = ConfigDict(
        populate_by_name=True
    )

    @model_validator(mode="after")
    @classmethod
    def validate_flow_requirements(cls, self: OAuthFlows) -> OAuthFlows:
        if self.implicit is not None:
            if self.implicit.authorization_url is None:
                raise ValueError("An authorization url is required for an OAuth Implicit flow")
            if self.implicit.scopes is None:
                raise ValueError("Scopes are required for an OAuth Implicit flow")
        if self.password is not None:
            if self.password.token_url is None:
                raise ValueError("A token url is required for an OAuth Resource Owner Password flow")
            if self.password.scopes is None:
                raise ValueError("Scopes are required for an OAuth Resource Owner Password flow")
        if self.client_credentials is not None:
            if self.client_credentials.token_url is None:
                raise ValueError("A token url is required for an OAuth Client Credentials flow")
            if self.client_credentials.scopes is None:
                raise ValueError("Scopes are required for an OAuth Client Credentials flow")
        if self.authorization_code is not None:
            if self.authorization_code.authorization_url is None:
                raise ValueError("An authorization url is required for an OAuth Authorization Code flow")
            if self.authorization_code.token_url is None:
                raise ValueError("A token url is required for an OAuth Authorization Code flow")
            if self.authorization_code.scopes is None:
                raise ValueError("Scopes are required for an OAuth Authorization Code flow")
        return self

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'OAuth Flows Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#oauth-flows-object
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)