from __future__ import annotations
from typing import Annotated, Any, Dict, Optional, ClassVar, Any
from pydantic import BaseModel, create_model
from .open_api_3 import Response, get_response_by_status_code, MediaType, get_media_type_by_name, Schema

class Model(BaseModel):
    @classmethod
    def oa3_schema(cls) -> Schema: 
        return Schema(schema_fields=cls)

class ResponseModel(Model):
    __media_type__: ClassVar[str] = "application/json"
    __status_code__: ClassVar[int] = 200

    @classmethod
    def produce_response(cls) -> Response:
        schema_object = cls.oa3_schema()
        response_object = get_response_by_status_code(cls.__status_code__)()
        response_object.add_media_type(get_media_type_by_name(cls.__media_type__)(schema_object=schema_object))
        return response_object