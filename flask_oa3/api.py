from typing import Dict, List, Union
from flask import Flask

from .decorators import specification_extensions_support
from .namespace import Namespace
from .view import View
from .licenses import License

class API:
    OPENAPI_VERSION = "3.1.0"

    def __init__(self, title: str, version: Union[str, None] = None) -> None:
        self.title: str = title
        self.summary: Union[str, None] = None
        self.description: Union[str, None] = None
        self.terms_of_service: Union[str, None] = None
        self.contact: Union[dict, None] = None
        self.license: Union[dict, None] = None
        self.tags: Union[Dict[str, dict], None] = None
        self.version: str = "dev" if version is None else version
        self.namespaces: List[Namespace] = []
        self.views: List[View] = []
    
    def init_app(self) -> Flask:
        pass

    def register_namespace(self, namespace: Namespace):
        self.namespaces.append(namespace)
    
    @specification_extensions_support
    def set_tag_info(self, name: str, description: Union[str, None] = None, external_documentation: Union[Dict[str, str], None] = None, **specification_extensions):
        """Adds metadata to a single tag that is used by the Operation Object. It is not mandatory to have a Tag Object per tag defined in the Operation Object instances.

        Args:
            name (str): REQUIRED. The name of the tag.
            description (Union[str, None], optional): A description for the tag. CommonMark syntax MAY be used for rich text representation. Defaults to None.
            external_documentation (Union[Dict[str, str], None], optional): Additional external documentation for this tag. Defaults to None.

        Raises:
            KeyError: When a tag has already been defined with the same name
        """        
        if name in self.tags:
            raise KeyError(f"A tag with the name {name} is already defined")
        self.tags[name] = {
            "name": name
        }
        if description is not None:
            self.tags[name]["description"] = description
        if external_documentation is not None:
            self.tags[name]["externalDocs"] = external_documentation
        self.tags[name].update(specification_extensions)
    
    @specification_extensions_support
    def set_contact_info(self, name: Union[str, None] = None, url: Union[str, None] = None, email: Union[str, None] = None, **specification_extensions):
        """Contact information for the exposed API.

        Args:
            name (Union[str, None], optional): The identifying name of the contact person/organization. Defaults to None.
            url (Union[str, None], optional): The URL pointing to the contact information. This MUST be in the form of a URL. Defaults to None.
            email (Union[str, None], optional): The email address of the contact person/organization. This MUST be in the form of an email address. Defaults to None.
        """        
        if name is None and url is None and email is None:
            self.contact = None
        else:
            self.contact = {}
            if name is not None:
                self.contact["name"] = name
            if url is not None:
                self.contact["url"] = url
            if email is not None:
                self.contact["email"] = email
            self.license.update(specification_extensions)

    @specification_extensions_support
    def set_spdx_license_info(self, license: License, url: Union[str, None] = None, **specification_extensions):
        """_summary_

        Args:
            license (License): An spdx defined license.
            url (Union[str, None], optional): A URL to the license used for the API. This MUST be in the form of a URL. Defaults to None.
        """        
        self.license = license.schema
        if url is not None:
            self.license["url"] = url
        self.license.update(specification_extensions)

    @specification_extensions_support
    def set_custom_license_info(self, name: Union[str, None], identifier: Union[str, None] = None, url: Union[str, None] = None, **specification_extensions):
        """License information for the exposed API.

        Args:
            name (Union[str, None]): REQUIRED. The license name used for the API. If None all other parameters are ignored and the license is disabled.
            identifier (Union[str, None], optional): An SPDX license expression for the API. The identifier field is mutually exclusive of the url field. Defaults to None.
            url (Union[str, None], optional): A URL to the license used for the API. This MUST be in the form of a URL. The url field is mutually exclusive of the identifier field. Defaults to None.
        """        
        if name is None:
            self.license = None
        else:
            self.license = {
                "name": name
            }
            if identifier is not None:
                self.license["identifier"] = identifier
            if url is not None:
                self.license["url"] = url
            self.license.update(specification_extensions)

    @property
    def schema(self) -> dict:
        schema = {
            "openapi": self.OPENAPI_VERSION,
            "jsonSchemaDialect": "https://spec.openapis.org/oas/3.1/dialect/base",
            "info": {
                "title": self.title,
                "version": self.version,
            }
        }
        if self.summary is not None:
            schema["info"]["summary"] = self.summary
        if self.description is not None:
            schema["info"]["description"] = self.description
        if self.terms_of_service is not None:
            schema["info"]["termsOfService"] = self.terms_of_service
        if self.contact is not None:
            schema["info"]["contact"] = self.contact
        if self.license is not None:
            schema["info"]["license"] = self.license
        if self.tags is not None:
            schema["tags"] = self.tags
        return schema