from __future__ import annotations
from typing import Annotated, Any, Dict, Optional, ClassVar
from pydantic import BaseModel, Field
from copy import deepcopy

class Model(BaseModel):
    @classmethod
    def _get_component_name(cls) -> str:
        return f"#/components/schemas/{cls.__name__}"

    @classmethod
    def oa3_schema(cls):
        """Constructs the Open API 'Schema Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#schemaObject
        
        Returns:
            dict: The Open API schema
        
        Notes:
            if "$defs" is defined then they must be popped out and ensured that they exist in the components object
        """   
        schema = cls.model_json_schema(ref_template = "#/components/schemas/{model}")
        if cls.discriminator is not None:
            schema["discriminator"] = cls.discriminator.oa3_schema
        if cls.external_documentation is not None:
            schema["externalDocs"] = cls.external_documentation.oa3_schema
        return schema
