from __future__ import annotations
from typing import Annotated, Any, Dict, Optional, ClassVar
from enum import StrEnum
from pydantic import BaseModel, Field, AnyUrl
from copy import deepcopy

from .component import Component, ComponentType
from .discriminator import Discriminator
from .external_documentation import ExternalDocumentation
from .xml import XML
from .oauth_flows import OAuthFlows

class SecuritySchemeType(StrEnum):
    HTTP = "http"
    API_KEY = "apiKey"
    MUTUAL_TLS = "mutualTLS"
    OAUTH2 = "oauth2"
    OPEN_ID_CONNECT = "openIdConnect"

class SecuritySchemeLocation(StrEnum):
    QUERY = "query" #Parameters that are appended to the URL. For example, in /items?id=###, the query parameter is id.
    HEADER = "header" #Custom headers that are expected as part of the request. Note that [RFC7230] states header names are case insensitive.
    COOKIE = "cookie" #Used to pass a specific cookie value to the API.

class HTTPAuthenticationScheme(StrEnum):
    """
    Spec:

    https://www.iana.org/assignments/http-authschemes/http-authschemes.xhtml
    """
    BASIC = "Basic"
    BEARER = "Bearer"
    DIGEST = "Digest"
    DPOP = "DPoP"
    HOBA = "HOBA"
    MUTUAL = "Mutual"
    NEGOTIATE = "Negotiate"
    OAUTH = "OAuth"
    PRIVATE_TOKEN = "PrivateToken"
    SCRAM_SHA_1 = "SCRAM-SHA-1"
    SCRAM_SHA_256 = "SCRAM-SHA-256"
    VAPID = "vapid"

class SecurityScheme(Component):
    security_scheme_type: Annotated[SecuritySchemeType, Field(description="REQUIRED. The type of the security scheme. Valid values are \"apiKey\", \"http\", \"mutualTLS\", \"oauth2\", \"openIdConnect\".")]
    description: Annotated[Optional[str], Field(default=None, description="A description for security scheme. CommonMark syntax MAY be used for rich text representation.")]
    name: Annotated[Optional[str], Field(default=None, description="REQUIRED. The name of the header, query or cookie parameter to be used.")]
    in_location: Annotated[Optional[str], Field(default=None, alias="in", description="REQUIRED. The location of the API key. Valid values are \"query\", \"header\" or \"cookie\".")]
    scheme: Annotated[Optional[HTTPAuthenticationScheme], Field(default=None, description="REQUIRED. The name of the HTTP Authorization scheme to be used in the Authorization header as defined in [RFC7235]. The values used SHOULD be registered in the IANA Authentication Scheme registry")]
    bearer_format: Annotated[Optional[str], Field(default=None, description="A hint to the client to identify how the bearer token is formatted. Bearer tokens are usually generated by an authorization server, so this information is primarily for documentation purposes.")]
    flows: Annotated[Optional[OAuthFlows], Field(default=None, description="REQUIRED. An object containing configuration information for the flow types supported.")]
    open_id_connect_url: Annotated[Optional[AnyUrl], Field(default=None, alias="openIdConnectUrl", description="REQUIRED. OpenId Connect URL to discover OAuth2 configuration values. This MUST be in the form of a URL. The OpenID Connect standard requires the use of TLS.")]


    @property
    def oa3_schema(self):
        """Constructs the Open API 'Security Scheme Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#securitySchemeObject
        
        Returns:
            dict: The Open API schema
        
        Notes:
            if "$defs" is defined then they must be popped out and ensured that they exist in the components object
        """   
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)
