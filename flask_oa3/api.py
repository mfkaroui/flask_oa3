from typing import Dict, List, Union
from flask import Flask

from .base import Base
from .namespace import Namespace
from .licenses import License

class API(Base):
    def __init__(self, title: str, version: Union[str, None] = None) -> None:
        super().__init__(None)
        self.title: str = title
        self.summary: Union[str, None] = None
        self.description: Union[str, None] = None
        self.terms_of_service: Union[str, None] = None
        self.contact: Union[dict, None] = None
        self.license: Union[dict, None] = None
        self.version: str = "dev" if version is None else version
        self.namespaces: List[Namespace] = []
    
    def init_app(self) -> Flask:
        pass

    def register_namespace(self, namespace: Namespace):
        self.namespaces.append(namespace)
    
    def set_contact_info(self, name: Union[str, None] = None, url: Union[str, None] = None, email: Union[str, None] = None):
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
    
    def set_spdx_license_info(self, license: License, url: Union[str, None] = None, specification_extensions: Union[dict, None] = None):
        """_summary_

        Args:
            license (License): An spdx defined license.
            url (Union[str, None], optional): A URL to the license used for the API. This MUST be in the form of a URL. Defaults to None.
            specification_extensions (Union[dict, None], optional): Allows extensions to the OpenAPI Schema. The field name MUST begin with x-, for example, x-internal-id. Field names beginning x-oai- and x-oas- are reserved. Defaults to None.
        """        
        self.license = license.schema
        if url is not None:
            self.license["url"] = url
        if specification_extensions is not None:
            for key in specification_extensions:
                if key.startswith("x-"):
                    self.license[key] = specification_extensions[key]
                else:
                    self.license[f"x-{key}"] = specification_extensions[key]

    def set_custom_license_info(self, name: Union[str, None], identifier: Union[str, None] = None, url: Union[str, None] = None, specification_extensions: Union[dict, None] = None):
        """License information for the exposed API.

        Args:
            name (Union[str, None]): REQUIRED. The license name used for the API. If None all other parameters are ignored and the license is disabled.
            identifier (Union[str, None], optional): An SPDX license expression for the API. The identifier field is mutually exclusive of the url field. Defaults to None.
            url (Union[str, None], optional): A URL to the license used for the API. This MUST be in the form of a URL. The url field is mutually exclusive of the identifier field. Defaults to None.
            specification_extensions (Union[dict, None], optional): Allows extensions to the OpenAPI Schema. The field name MUST begin with x-, for example, x-internal-id. Field names beginning x-oai- and x-oas- are reserved. Defaults to None.
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
            if specification_extensions is not None:
                for key in specification_extensions:
                    if key.startswith("x-"):
                        self.license[key] = specification_extensions[key]
                    else:
                        self.license[f"x-{key}"] = specification_extensions[key]

    @property
    def schema(self) -> dict:
        schema = super().schema
        schema["info"] = {
            "title": self.title,
            "version": self.version
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
        return schema