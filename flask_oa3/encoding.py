from typing import Optional, Annotated, Dict
from pydantic import BaseModel, Field
from .header import Header

class Encoding(BaseModel):
    content_type: Annotated[Optional[str], Field(default=None, alias="contentType", description="The Content-Type for encoding a specific property. Default value depends on the property type: for object - application/json; for array – the default is defined based on the inner type; for all other cases the default is application/octet-stream. The value can be a specific media type (e.g. application/json), a wildcard media type (e.g. image/*), or a comma-separated list of the two types.")]
    headers: Annotated[Optional[Dict[str, Header]], Field(default=None, description="A map allowing additional information to be provided as headers, for example Content-Disposition. Content-Type is described separately and SHALL be ignored in this section. This property SHALL be ignored if the request body media type is not a multipart.")]
    style: Annotated[Optional[str], Field(default=None, description="Describes how a specific property value will be serialized depending on its type. See Parameter Object for details on the style property. The behavior follows the same values as query parameters, including default values. This property SHALL be ignored if the request body media type is not application/x-www-form-urlencoded or multipart/form-data. If a value is explicitly defined, then the value of contentType (implicit or explicit) SHALL be ignored.")]
    explode: Annotated[Optional[bool], Field(default=None, description="When this is true, property values of type array or object generate separate parameters for each value of the array, or key-value-pair of the map. For other types of properties this property has no effect. When style is form, the default value is true. For all other styles, the default value is false. This property SHALL be ignored if the request body media type is not application/x-www-form-urlencoded or multipart/form-data. If a value is explicitly defined, then the value of contentType (implicit or explicit) SHALL be ignored.")]
    allow_reserved: Annotated[Optional[bool], Field(default=None, alias="allowReserved" description="Determines whether the parameter value SHOULD allow reserved characters, as defined by [RFC3986] :/?#[]@!$&'()*+,;= to be included without percent-encoding. The default value is false. This property SHALL be ignored if the request body media type is not application/x-www-form-urlencoded or multipart/form-data. If a value is explicitly defined, then the value of contentType (implicit or explicit) SHALL be ignored.")]

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Encoding Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#encodingObject
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)