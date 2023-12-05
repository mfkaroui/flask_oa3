import os
from typing import Dict, List, Optional, ClassVar
from urllib.parse import urljoin
from pydantic import BaseModel
from .model import Model
from .view import View
from .errors import RouteInUseError, ModelAlreadyRegisteredError
from .open_api_3 import Tag
from .open_api_3 import ExternalDocumentation

class Namespace(BaseModel):
    name: str
    description: Optional[str] = None
    external_documentation: Optional[ExternalDocumentation] = None
    views: ClassVar[List[View]] = []
 
    @classmethod
    def _format_route(cls, route: str):
        formatted_route = route.replace("\\", "/")
        if not formatted_route.startswith("/"):
            formatted_route = f"/{formatted_route}"
        if formatted_route.endswith("/"):
            formatted_route = formatted_route[:-1]
        return formatted_route

    def _parse_route(self, route: str):
        return f"{self.base_route}{Namespace._format_route(route)}"

    def register_view(self, view: View, route: str):
        full_route = self._parse_route(route)
        if full_route in self.views:
            raise RouteInUseError(f"Route {full_route} already in use by {self.views[full_route].__class__.__name__}")
        self.views[full_route] = view

    def _get_tag(self) -> Tag:
        return Tag(
            name=self.name,
            description=self.description,
            external_documentation=self.external_documentation
        )