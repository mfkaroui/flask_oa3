from typing import Optional
from typing_extensions import Annotated
from pydantic import BaseModel, AnyUrl, EmailStr, Field, model_validator

class Contact(BaseModel):
    name: Annotated[Optional[str], Field(default=None, description="The identifying name of the contact person/organization.")]
    url: Annotated[Optional[AnyUrl], Field(default=None, description="The URL pointing to the contact information. This MUST be in the form of a URL.")]
    email: Annotated[Optional[EmailStr], Field(default=None, description="The URL pointing to the contact information. This MUST be in the form of a URL.")]

    @model_validator(mode="before")
    def check_atleast_one(cls, values):
        if "name" not in values and "url" not in values and "email" not in values:
            raise ValueError("At least one of 'name', 'url' or 'email' must be specified")
        return values


    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Contact Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#contact-object
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)