from typing import Dict, Union, Optional, ClassVar, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic import BaseModel, Field, field_serializer
from ..encoding import Encoding
from ..example import Example
from ..reference import Reference
from ..schema import Schema

class MediaType(BaseModel):
    __MEDIA_TYPE__: ClassVar[Optional[str]] = None
    
    schema_object: Annotated[Optional[Schema], Field(default=None, alias="schema", description="The schema defining the content of the request, response, or parameter.")]
    examples: Annotated[Optional[Dict[str, Union[Example, Reference[Example]]]], Field(default=None, description="Examples of the media type. Each example object SHOULD match the media type and specified schema if present. The examples field is mutually exclusive of the example field. Furthermore, if referencing a schema which contains an example, the examples value SHALL override the example provided by the schema.")]
    encoding: Annotated[Optional[Dict[str, Encoding]], Field(default=None, description="A map between a property name and its encoding information. The key, being the property name, MUST exist in the schema as a property. The encoding object SHALL only apply to requestBody objects when the media type is multipart or application/x-www-form-urlencoded.")]
    
    @classmethod
    def _get_name(cls) -> str:
        if cls.__MEDIA_TYPE__ is None:
            raise ValueError(f"The media type was not set")
        return cls.__MEDIA_TYPE__
    
    @field_serializer("schema_object")
    def schema_object_serializer(self, schema_object: Optional[Schema], _info) -> dict:
        if schema_object is None:
           raise ValueError("The schema_object was not set") 
        return Reference.from_component(schema_object).oa3_schema()

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Media Type Object' according to specifications

        Spec:
            https://spec.openapis.org/oas/v3.1.0#license-object

        Returns:
            dict: The Open API schema
        """     
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)
