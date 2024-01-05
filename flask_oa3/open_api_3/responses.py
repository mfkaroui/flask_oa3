from __future__ import annotations
from typing import Dict, Union, List, Optional
from typing_extensions import Annotated
from pydantic import BaseModel, Field, model_serializer

from .response import Response
from .reference import Reference
from .decorators import specification_extensions_support


@specification_extensions_support
class Responses(BaseModel):
    default: Annotated[
        Optional[Union[Response, Reference[Response]]],
        Field(
            default=None,
            description="The documentation of responses other than the ones declared for specific HTTP response codes. Use this field to cover undeclared responses. A Reference Object can link to a response that the OpenAPI Object’s components/responses section defines. This field MAY be openapi: ",
        ),
    ]
    other_responses: Annotated[
        Optional[List[Union[Response, Reference[Response]]]],
        Field(
            description="Any HTTP status code can be used as the property name, but only one property per code, to describe the expected response for that HTTP status code. This field MUST be enclosed in quotation marks (for example, “200”) for compatibility between JSON and YAML. To define a range of response codes, this field MAY contain the uppercase wildcard character X. For example, 2XX represents all response codes between [200-299]. Only the following range definitions are allowed: 1XX, 2XX, 3XX, 4XX, and 5XX. If a response is defined using an explicit code, the explicit code definition takes precedence over the range definition for that code."
        ),
    ]

    @model_serializer(mode="plain", when_used="always")
    def validate_status_codes(self) -> Dict[str, Union[Response, Reference[Response]]]:
        responses = {}
        if self.default is not None:
            if isinstance(response, Reference[Response]):
                responses["default"] = self.default.oa3_schema
            else:
                responses["default"] = self.default
        if self.other_responses is not None:
            for response in self.other_responses:
                if isinstance(response, Reference[Response]):
                    responses[
                        str(response.component.__STATUS_CODE__)
                    ] = response.oa3_schema
                else:
                    responses[str(response.__STATUS_CODE__)] = response
        return responses

    @property
    def oa3_schema(self):
        """Constructs the Open API 'Responses Object' according to specifications

        Spec:
            https://spec.openapis.org/oas/v3.1.0#responses-object

        Returns:
            dict: The Open API schema
        """
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)
