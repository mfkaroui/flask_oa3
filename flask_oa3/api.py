from typing import Dict, List, Union
from flask import Flask

from .decorators import specification_extensions_support
from .namespace import Namespace
from .view import View
from .licenses import License
from .tag import Tag

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
    
    def set_tag_info(self, tag: Union[Tag, dict]):
        """This method accepts a tag, which can either be an instance of the `Tag` class or a dictionary representing a tag.
        If a dictionary is provided, it is converted into a `Tag` instance. The method then stores the Open API schema
        representation of this tag in the `tags` attribute, using the tag's name as the key.
    
        Args:
            tag (Union[Tag, dict]): A `Tag` object or a dictionary representing a tag. The dictionary should contain keys
            and values corresponding to the attributes of the `Tag` class.
    
        Note:
            The `Tag` class is used to represent a tag in Open API specifications, with attributes like 'name',
            'description', and 'external_documentation'. The method leverages the `oa3_schema` property of the `Tag`
            class to store a standardized Open API schema version of the tag.
        """        
        if isinstance(tag, dict):
            tag = Tag(**tag)
        self.tags[tag.name] = tag.oa3_schema

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