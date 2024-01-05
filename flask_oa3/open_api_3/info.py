from typing import Optional, Union
from typing_extensions import Annotated
from pydantic import BaseModel, AnyUrl, Field
from .contact import Contact
from .license import License, PredefinedLicense


class Info(BaseModel):
    title: Annotated[str, Field(description="REQUIRED. The title of the API.")]
    summary: Annotated[
        Optional[str], Field(default=None, description="A short summary of the API.")
    ]
    description: Annotated[
        Optional[str],
        Field(
            default=None,
            description="A description of the API. CommonMark syntax MAY be used for rich text representation.",
        ),
    ]
    terms_of_service: Annotated[
        Optional[AnyUrl],
        Field(
            default=None,
            alias="termsOfService",
            description="A URL to the Terms of Service for the API. This MUST be in the form of a URL.",
        ),
    ]
    contact: Annotated[
        Optional[Contact],
        Field(default=None, description="The contact information for the exposed API."),
    ]
    license: Annotated[
        Optional[Union[License, PredefinedLicense]],
        Field(default=None, description="The license information for the exposed API."),
    ]
    version: Annotated[
        str,
        Field(
            default="dev",
            description="REQUIRED. The version of the OpenAPI document (which is distinct from the OpenAPI Specification version or the API implementation version).",
        ),
    ]

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Info Object' according to specifications

        Spec:
            https://spec.openapis.org/oas/v3.1.0#info-object

        Returns:
            dict: The Open API schema
        """
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)
