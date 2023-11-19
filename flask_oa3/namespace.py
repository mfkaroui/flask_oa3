import os
from typing import Dict, List
from urllib.parse import urljoin

from .base import Base
from .model import Model
from .view import View
from .errors import RouteInUseError, ModelAlreadyRegisteredError

class Namespace(Base):
    def __init__(self, name: str, base_route: str):
        super().__init__(name)
        self.base_route = Namespace._format_route(base_route)
        self.views: Dict[str, View] = {}
        self.models: Dict[str, Model] = {}

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

    def register_model(self, model: Model):
        if model.name in self.models:
            raise ModelAlreadyRegisteredError(f"Model {model.name} already registered")
        self.models[model.name] = model