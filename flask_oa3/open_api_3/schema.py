from __future__ import annotations
from typing import Optional, ClassVar, Type, Dict, Union, List, Tuple, Any
from typing_extensions import Annotated
from pydantic import Field, AnyUrl, BaseModel, RootModel, ConfigDict, model_validator, model_serializer, field_serializer, field_validator, SerializationInfo, ValidationInfo

from .component import Component, ComponentType
from .external_documentation import ExternalDocumentation
from .decorators import specification_extensions_support
from .reference import Reference
from .xml import XML

@specification_extensions_support
class Schema(Component):
    component_type: ClassVar[ComponentType] = ComponentType.SCHEMA
    
    discriminator: Annotated[Optional[Discriminator], Field(default=None, description="Adds support for polymorphism. The discriminator is an object name that is used to differentiate between other schemas which may satisfy the payload description. See Composition and Inheritance for more details.")] 
    xml: Annotated[Optional[XML], Field(default=None, description="This MAY be used only on properties schemas. It has no effect on root schemas. Adds additional metadata to describe the XML representation of this property.")]
    external_documentation: Annotated[Optional[ExternalDocumentation], Field(default=None, description="Additional external documentation for this schema.")]
    json_schema_dialect: Annotated[Optional[AnyUrl], Field(default=None, alias="$schema", description="The $schema keyword MAY be present in any root Schema Object, and if present MUST be used to determine which dialect should be used when processing the schema. This allows use of Schema Objects which comply with other drafts of JSON Schema than the default Draft 2020-12 support. Tooling MUST support the OAS dialect schema id, and MAY support additional values of $schema.")]
    schema_model: Annotated[Union[
        Type[BaseModel],
        Type[RootModel],
        Reference[Schema],
        List[Union[Type[BaseModel], Type[RootModel], Reference[Schema]]],
        Tuple[Union[Type[BaseModel], Type[RootModel], Reference[Schema]]]
    ], Field(description="A pydantic model type that contains the fields needed for the schema. When using a list, the schemas are combined using allOf except for when a discriminator is defined, then oneOf is inferred. When using a tuple, the schemas are combined using oneOf regardless of whether a discriminiator is defined.")]
    
    model_config = ConfigDict(
        populate_by_name=True
    )

    @property
    def component_name(self) -> str:
        if isinstance(self.schema_model, Reference[Schema]):
            return f"ref.{self.schema_model.component.component_name}"
        elif isinstance(self.schema_model, list) or isinstance(self.schema_model, tuple):
            components = []
            for model in self.schema_model:
                if isinstance(model, Reference[Schema]):
                    components.append(f"ref.{model.component.component_name}")
                else:
                    components.append(f"{model.__name__}")
            is_one_of = (isinstance(self.schema_model, tuple) or self.discriminator is not None)
            return f"{('one_of' if is_one_of else 'all_of')}[{', '.join(components)}]"
        return self.schema_model.__name__

    @field_validator("schema_model", mode="plain", check_fields=False)
    @classmethod
    def validate_schema_model(cls, value: Any, info: ValidationInfo) -> Union[
        Type[BaseModel],
        Type[RootModel],
        Reference[Schema],
        List[Union[Type[BaseModel], Type[RootModel], Reference[Schema]]],
        Tuple[Union[Type[BaseModel], Type[RootModel], Reference[Schema]]]
    ]:
        if isinstance(value, list) or isinstance(value, tuple):
            for model in value:
                if not isinstance(model, Reference[Schema]) and not issubclass(model, BaseModel) and not issubclass(value, RootModel):
                    raise TypeError("schema_model in list must be a pydantic model or a reference to a schema")
        elif not isinstance(value, Reference[Schema]) and not issubclass(value, BaseModel) and not issubclass(value, RootModel):
            raise TypeError("schema_model must be a pydantic model or a reference to a schema")
        return value

    def has_property(self, property_name: str) -> bool:
        if isinstance(self.schema_model, Reference[Schema]):
            return self.schema_model.component.has_property(property_name)
        elif isinstance(self.schema_model, list) or isinstance(self.schema_model, tuple):
            found_property = False
            for model in self.schema_model:
                if isinstance(model, Reference[Schema]):
                    found_property = model.component.has_property(property_name)
                else:
                    found_property = property_name in model.model_fields
                if found_property:
                    break
            return found_property
        return property_name in self.schema_model.model_fields

    @model_validator(mode="after")
    @classmethod
    def validate_schema(cls, self: Schema) -> Schema:
        if self.discriminator is not None:
            if isinstance(self.schema_model, list) or isinstance(self.schema_model, tuple):
                if not self.has_property(self.discriminator.property_name):
                    raise KeyError("schema_model must have a property that matches the discriminator property name")
            else:
                raise TypeError("schema_model must be a list or tuple when a discriminator is defined")
        return self

    @field_serializer('schema_model', when_used="always", check_fields=False)
    @property
    def ignore_schema_model(self, value: Any, info: SerializationInfo) -> None:
        return None

    @property
    def schema_model_json_schema(self) -> Tuple[dict, dict]:
        defs = {}
        if isinstance(self.schema_model, Reference[Schema]):
            defs = self.schema_model.component.schema_model_json_schema[1]
            json_schema = self.schema_model.oa3_schema
            json_schema["title"] = self.component_name
        elif isinstance(self.schema_model, list) or isinstance(self.schema_model, tuple):
            components = []
            for model in self.schema_model:
                if isinstance(model, Reference[Schema]):
                    defs.update(model.component.schema_model_json_schema[1])
                    json_schema = model.oa3_schema
                    json_schema["title"] = f"ref.{model.component.component_name}"
                    components.append(json_schema)
                else:
                    json_schema = model.model_json_schema(by_alias=True, ref_template = self.component_path() + "/{model}")
                    json_schema_defs = json_schema.pop("$defs", None)
                    components.append(json_schema)
                    if json_schema_defs is not None:
                        defs.update(json_schema_defs)
            is_one_of = (isinstance(self.schema_model, tuple) or self.discriminator is not None)
            json_schema = {
                "oneOf" if is_one_of else "allOf": components,
                "title": self.component_name
            }
        else:
            json_schema = self.schema_model.model_json_schema(by_alias=True, ref_template = self.component_path() + "/{model}")
            json_schema_defs = json_schema.pop("$defs", None)
            if json_schema_defs is not None:
                defs.update(json_schema_defs)
        return json_schema, defs

    @model_serializer(mode="wrap", when_used="always")
    def schema_model_serializer(self, handler) -> dict:
        schema = handler(self)
        schema.pop("schema_model", None)
        schema.update(self.schema_model_json_schema[0])
        return schema

    @property
    def oa3_schema(self):
        """Constructs the Open API 'Schema Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#schemaObject
        
        Returns:
            dict: The Open API schema
        
        Notes:
            if "$defs" is defined then they must be popped out and ensured that they exist in the components object
        """   
        schema = self.model_dump(mode="json", by_alias=True, exclude_none=True)
        fields_schema = schema.pop("schema_fields", {})
        schema.update(fields_schema)
        return schema

@specification_extensions_support
class Discriminator(BaseModel):
    property_name: Annotated[str, Field(alias="propertyName", description="REQUIRED. The name of the property in the payload that will hold the discriminator value.")]
    mapping: Annotated[Optional[Dict[str, Union[str, Reference[Schema]]]], Field(default=None, description="An object to hold mappings between payload values and schema names or references.")]

    model_config = ConfigDict(
        populate_by_name=True
    )

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Discriminator Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#discriminatorObject
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)