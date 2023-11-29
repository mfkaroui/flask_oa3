from typing import Any, List, Union
from enum import StrEnum

class FieldType(StrEnum):
    """The data type of a schema. OpenAPI defines the following basic types"""  
    NO_TYPE = "<no_type>"  
    STRING = "string"
    NUMBER = "number"
    INTEGER = "integer"
    BOOLEAN = "boolean"
    ARRAY = "array"
    OBJECT = "object"
