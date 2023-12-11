from typing import Optional, Annotated, ClassVar, Dict
from pydantic import BaseModel, AnyUrl, EmailStr, Field
from ..open_api_3 import OpenAPI, License
from ..namespace import Namespace
from ..view import View

class App(BaseModel):
    title: Annotated[str, Field(description="REQUIRED. The title of the API.")]
    summary: Annotated[Optional[str], Field(default=None, description="A short summary of the API.")]
    description: Annotated[Optional[str], Field(default=None, description="A description of the API. CommonMark syntax MAY be used for rich text representation.")]
    terms_of_service: Annotated[Optional[AnyUrl], Field(default=None, alias="termsOfService", description="A URL to the Terms of Service for the API. This MUST be in the form of a URL.")]
    contact_name: Annotated[Optional[str], Field(default=None, description="The identifying name of the contact person/organization.")]
    contact_url: Annotated[Optional[AnyUrl], Field(default=None, description="The URL pointing to the contact information. This MUST be in the form of a URL.")]
    contact_email: Annotated[Optional[EmailStr], Field(default=None, description="The URL pointing to the contact information. This MUST be in the form of a URL.")]
    license: Annotated[Optional[License], Field(default=None, description="The license information for the exposed API.")]
    version: Annotated[str, Field(default="dev", description="REQUIRED. The version of the OpenAPI document (which is distinct from the OpenAPI Specification version or the API implementation version).")]

    namespaces: ClassVar[Dict[str, Namespace]] = {}
    views: ClassVar[Dict[str, View]] = {}

    def register_namespace(self, route: str, namespace: Namespace):
        if route in self.namespaces:
            raise ValueError(f"Namespace with route '{route}' already registered")
        self.namespaces[route] = namespace

    def register_view(self, route: str, view: type[View]):
        if route in self.views:
            raise ValueError(f"View with route '{route}' already registered")
        self.views[route] = view

    @property
    def oa3_spec(self) -> OpenAPI:
        return OpenAPI(**{
            "info": {
                "title": self.title,
                "summary": self.summary,
                "description": self.description,
                "terms_of_service": self.terms_of_service,
                "contact": {
                    "name": self.contact_name,
                    "url": self.contact_url,
                    "email": self.contact_email
                },
                "license": self.license,
                "version": self.version
            },
            "paths": {
                route: namespace.oa3_spec
                for route, namespace in self.namespaces.items()
            },
            "components": {
                "schemas": {
                    route: view.oa3_spec
                    for route, view in self.views.items()
                }
            },
            "tags": [
                {
                    "name": namespace.name,
                    "description": namespace.description
                }
                for namespace in self.namespaces.values()
            ]
        })