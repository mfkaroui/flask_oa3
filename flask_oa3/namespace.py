import os
from typing import Dict, List, Optional, Type
from typing_extensions import Annotated
from urllib.parse import urljoin
from pydantic import BaseModel, Field, model_serializer
from .view import View
from .open_api_3 import Tag
from .open_api_3 import ExternalDocumentation

class Namespace(BaseModel):
    name: str
    route: Annotated[str, Field(default="/", description="The route of the namespace.")]
    description: Annotated[Optional[str], Field(default=None, description="A short description of the namespace. CommonMark syntax MAY be used for rich text representation. Defaults to None.")]
    external_documentation: Annotated[Optional[ExternalDocumentation], Field(default=None, description="Additional external documentation for this namespace. Defaults to None.")]

    views: Dict[str, Type[View]] = {}

    @model_serializer(mode="wrap")
    def serialize_component(self, handler):
        exclude = ["views"]
        d = handler(self)
        d = {k:v for k, v in d.items() if k not in exclude}
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
 
    def register_view(self, route: str, view: Type[View]):
        if route in self.views:
            raise ValueError(f"View with route '{route}' already registered")
        self.views[route] = view

    def _get_tag(self) -> Tag:
        return Tag(
            name=self.name,
            description=self.description,
            external_documentation=self.external_documentation
        )