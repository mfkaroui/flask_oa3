from typing import List, Optional, ClassVar, Dict, Union, Type
from typing_extensions import Annotated
from pydantic import BaseModel, AnyUrl, EmailStr, Field, model_serializer
from ..open_api_3 import OpenAPI, License, PredefinedLicense, Paths
from ..namespace import Namespace
from ..view import View


class App(BaseModel):
    route: Annotated[
        str, Field(default="/", description="The route of the application.")
    ]
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
    contact_name: Annotated[
        Optional[str],
        Field(
            default=None,
            description="The identifying name of the contact person/organization.",
        ),
    ]
    contact_url: Annotated[
        Optional[AnyUrl],
        Field(
            default=None,
            description="The URL pointing to the contact information. This MUST be in the form of a URL.",
        ),
    ]
    contact_email: Annotated[
        Optional[EmailStr],
        Field(
            default=None,
            description="The URL pointing to the contact information. This MUST be in the form of a URL.",
        ),
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

    namespaces: Dict[str, Namespace] = {}
    views: Dict[str, Type[View]] = {}

    @model_serializer(mode="wrap")
    def serialize_component(self, handler):
        exclude = ["namespaces", "views"]
        d = handler(self)
        d = {k: v for k, v in d.items() if k not in exclude}
        return d

    @property
    def base_route(self) -> List[str]:
        """
        This property splits the route into a list of its parts.
        The route is a string representing a URL path, and this property
        returns a list where each element is a part of the path.

        Returns:
            List[str]: The parts of the route.
        """
        return self.route.split("/")

    def get_route(self, *args) -> str:
        routes = self.base_route
        for part in args:
            if isinstance(part, str):
                routes.extend(part.split("/"))
        route = "/".join(routes).replace("//", "/")
        if not route.startswith("/"):
            return f"/{route}"
        return route

    def init_app(self):
        raise NotImplementedError(
            f"Application cannot be initialized from the base class, must be overridden"
        )

    def register_namespace(self, namespace: Namespace):
        if namespace.route in self.namespaces:
            raise ValueError(
                f"Namespace with route '{namespace.route}' already registered"
            )
        self.namespaces[namespace.route] = namespace

    def register_view(self, route: str, view: Type[View]):
        if route in self.views:
            raise ValueError(f"View with route '{route}' already registered")
        self.views[route] = view

    @property
    def oa3_spec(self) -> OpenAPI:
        open_api = OpenAPI(
            **{
                "info": {
                    "title": self.title,
                    "summary": self.summary,
                    "description": self.description,
                    "terms_of_service": self.terms_of_service,
                    "contact": {
                        "name": self.contact_name,
                        "url": self.contact_url,
                        "email": self.contact_email,
                    },
                    "license": self.license,
                    "version": self.version,
                },
                # "paths": {
                #    self.get_route(namespace.get_route(route)): namespace.oa3_spec
                #    for route, namespace in self.namespaces.items()
                # },
                # "components": {
                #    "schemas": {
                #        route: view.oa3_spec
                #        for route, view in self.views.items()
                #    }
                # },
                "tags": [
                    namespace._get_tag() for namespace in self.namespaces.values()
                ],
            }
        )
        paths = {}
        for route, namespace in self.namespaces.items():
            for route, view in namespace.views.items():
                paths[
                    self.get_route(namespace.get_route(route))
                ] = view.produce_path_item()
        open_api.paths = Paths(root=paths)
        return open_api.oa3_schema
