from __future__ import annotations
from typing import Annotated, Optional,
from pydantic import BaseModel, Field
from copy import deepcopy

from .discriminator import Discriminator
from .external_documentation import ExternalDocumentation

class Model(BaseModel):
    discriminator: Annotated[Optional[Discriminator], Field(default=None, description="Adds support for polymorphism. The discriminator is an object name that is used to differentiate between other schemas which may satisfy the payload description. See Composition and Inheritance for more details.")]
    external_documentation: Annotated[Optional[ExternalDocumentation], Field(default=None, description="Additional external documentation for this schema.")]

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
        #deal with inheritance, use the allOf keyword and refs to avoid duplication
        all_of = []
        bases_schema = {}
        for base in cls.__bases__:
            if issubclass(base, Model) and base != Model:
                base_schema = base.oa3_schema()
                bases_schema[base_schema["title"]] = base_schema
                all_of.append({
                    "$ref" : base._get_component_name()
                })
                for property in base_schema["properties"]:
                    if property in schema["properties"]:
                        schema["properties"].pop(property)
                    if property in schema["required"]:
                        schema["required"].remove(property)
        if len(all_of) > 0:
            defs = schema.pop("$defs", {})
            defs.update(bases_schema)
            all_of.append(deepcopy(schema))
            schema = {
                "$defs": defs,
                "allOf": all_of
            }
        #flatten defs
        defs = schema.pop("$defs", {})
        for model_title in list(defs.keys()):
            model_defs = defs[model_title].pop("$defs", {})
            defs.update(model_defs)
        schema["$defs"] = defs
        return schema
