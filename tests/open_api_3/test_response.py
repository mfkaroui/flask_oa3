import os
from typing import List
import pytest
from json import load
from flask_oa3.open_api_3.response import Response, get_response_by_status_code
from flask_oa3.open_api_3.component import Component, ComponentType


def get_predefined_responses() -> List[dict]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    responses_path = os.path.join(
        dir_path, "../../flask_oa3/open_api_3/response/status_codes.json"
    )
    with open(responses_path, encoding="utf8") as f:
        f.seek(0)
        return load(f)


class TestResponse:
    def test_response_component(self):
        assert issubclass(Response, Component)

    def test_response_component_type(self):
        assert Response.component_type == ComponentType.RESPONSE

    def test_response_component_path(self):
        assert Response.component_path() == "#/components/responses"

    @pytest.mark.parametrize("predefined_response", get_predefined_responses())
    def test_get_response_by_status_code(self, predefined_response: dict):
        response = get_response_by_status_code(int(predefined_response["code"]))
        assert issubclass(response, Response)
        assert response.__STATUS_CODE__ == int(predefined_response["code"])
        assert response.__PHRASE__ == predefined_response["phrase"]
        assert response().component_name == response.__name__
