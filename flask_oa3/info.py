from typing import Optional
from pydantic import BaseModel, AnyUrl, EmailStr
from .contact import Contact
from .licenses import License

class Info(BaseModel):
    title: str
    version: str = "dev"
    summary: Optional[str] = None
    description: Optional[str] = None
    terms_of_service: Optional[AnyUrl] = None
    contact: Optional[Contact] = None
    license: Optional[License] = None
    

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Info Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#info-object
        
        Returns:
            dict: The Open API schema
        """        
        schema = {
            "title": self.title,
            "version": self.version
        }
        if self.summary is not None:
            schema["summary"] = self.summary
        if self.description is not None:
            schema["description"] = self.description
        if self.terms_of_service is not None:
            schema["termsOfService"] = self.terms_of_service
        if self.contact is not None:
            schema["contact"] = self.contact
        if self.license is not None:
            schema["license"] = self.license
        return schema