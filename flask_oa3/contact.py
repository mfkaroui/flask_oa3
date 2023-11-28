from typing import Optional
from typing_extensions import Annotated
from pydantic import BaseModel, AnyUrl, EmailStr, Field

class Contact(BaseModel):
    name: Annotated[Optional[str], Field(default=None, description="The identifying name of the contact person/organization.")]
    url: Annotated[Optional[AnyUrl], Field(default=None, description="The URL pointing to the contact information. This MUST be in the form of a URL.")]
    email: Annotated[Optional[EmailStr], Field(default=None, description="The URL pointing to the contact information. This MUST be in the form of a URL.")]

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Contact Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#contact-object
        
        Returns:
            dict: The Open API schema
        """        
        schema = {}
        if self.name is not None:
            schema["name"] = self.name
        if self.description is not None:
            schema["description"] = self.description
        if self.email is not None:
            schema["email"] = self.email
        return schema