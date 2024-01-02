from __future__ import annotations
from flask_oa3 import Model, View, ResponseModel, Namespace, FlaskApp
from flask_oa3.open_api_3 import license
from pydantic import EmailStr, Field
from pydantic_extra_types.phone_numbers import PhoneNumber
from typing import Optional, Union

class TestPayload(Model):
    name: str = Field(description="The name of the test model.")
    email: EmailStr = Field(description="The email of the test model.")
    phone_number: PhoneNumber = Field(description="The phone number of the test model.")

class TestResponse(ResponseModel):
    __status_code__: int = 200
    name: str = Field(description="The name of the response model.")

class TestErrorResponse(ResponseModel):
    __status_code__: int = 404
    error: str = Field(description="The error of the response model.")

    @classmethod
    def example_1(cls) -> dict:
        return {
            "error": "This is an error"
        }
    
    @classmethod
    def example_2(cls) -> dict: 
        return {
            "error": "This is an error"
        }

class TestView(View):
    """This is a test view"""

    def get(self, payload: TestPayload) -> Union[TestResponse, TestErrorResponse]:
        """
        This is a test method

        An even more detailed description of the test method
        
        :external_documentation:
            :url: https://www.google.com
            :description: please go here for more information
        
        :deprecation: 1.0.0
        """
        return TestResponse(name=payload.name)

if __name__ == "__main__":
    namespace = Namespace(name="TestNameSpace", route="/namespace")
    namespace.register_view("/TestView", TestView)
    app = FlaskApp(
        route="TestApplication",
        title="Test Application",
        description="This is a test application",
        contact_name="Mohamed Karoui",
        contact_email="mfkaroui@gmail.com",
        license=license.License0BSD(url="https://opensource.org/licenses/0BSD"),
        version="1.0.0",
    )
    app.register_namespace(namespace)
    app.init_app().run()
    print("test")