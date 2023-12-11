import os
from typing import Dict, List, Optional, ClassVar
from urllib.parse import urljoin
from pydantic import BaseModel
from .view import View
from .open_api_3 import Tag
from .open_api_3 import ExternalDocumentation

class Namespace(BaseModel):
    name: str
    description: Optional[str] = None
    external_documentation: Optional[ExternalDocumentation] = None
    views: ClassVar[List[View]] = []
 
    def _get_tag(self) -> Tag:
        return Tag(
            name=self.name,
            description=self.description,
            external_documentation=self.external_documentation
        )