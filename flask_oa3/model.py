from __future__ import annotations
from jsonref import loads
from typing import List
from pydantic import BaseModel, create_model
from .open_api_3 import Response, get_response_by_status_code,get_media_type_by_name, Component, Header

class Model(BaseModel):
    def produce_components(self) -> Component:
        raise NotImplementedError("produce_components method must be implemented")

class RequestModel(Model):
    pass

class RequestHeadersModel(RequestModel):
    def produce_components(self) -> List[Header]:
        headers: List[Header] = []
        model_schema = loads(self.model_json_schema(by_alias=True))
        for property_name, property_schema in model_schema["properties"].items():
            headers.append(Header(
                _component_name=property_name,
                required=property_name in model_schema["required"]
            ))
        return headers

class RequestFormDataModel(RequestModel):
    pass

class RequestBodyModel(RequestModel):
    pass

class ResponseModel(Model):
    @classmethod
    def get_status_code(cls) -> int:
        return 200

    @classmethod
    def get_media_type(cls) -> str:
        return "application/json"

    @classmethod
    def produce_response(cls) -> Response:
        schema_object = cls.oa3_schema()
        response_object = get_response_by_status_code(cls.get_status_code())()
        response_object.add_media_type(get_media_type_by_name(cls.get_media_type())(schema_object=schema_object))
        return response_object
