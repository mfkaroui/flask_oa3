from __future__ import annotations
from flask_oa3 import Field, Model, View, ExternalDocumentation, License
import flask_oa3.licenses as Licenses
from pydantic import EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from typing import Optional, Union

class UserModel(Model):
    external_documentation = ExternalDocumentation(
        url = "https://www.google.com",
        description = "External documentation for the user model"
    )
    first_name: str = Field(description="The first name of the user")
    last_name: str = Field(description="The last name of the user")
    email: Optional[EmailStr] = Field(default=None, description="The email of the user")
    phone_number: Optional[PhoneNumber] = Field(default=None, description="The phone number of the user")

class ChildUserModel(UserModel):
    has_lego: Union[bool, None]
    will_become: TeenUserModel

class TeenUserModel(ChildUserModel):
    has_car: bool
    will_become: AdultUserModel

class AdultUserModel(TeenUserModel):
    has_booze: bool
    will_become: None = None

class BaseRoute(View):
    def get(self, **kwargs):
        pass

from pydantic import create_model
if __name__ == "__main__":
    schema = Licenses.LicenseGpl3_0(url="https://google.com").oa3_schema
    print("test")
    #app = flask.Flask(__name__)
    #api = flask_oa3.API(app)
    #api.set_spdx_license_info()
    #namespace = flask_oa3.Namespace("base", "/")
    #namespace.register_view(BaseRoute)
    #api.register_namespace(namespace)