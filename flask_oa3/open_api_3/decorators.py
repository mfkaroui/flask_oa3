from typing import Dict, Any, Union
from pydantic import RootModel, BaseModel, model_validator, ConfigDict, create_model

def specification_extensions_support(cls: type[Union[RootModel, BaseModel]]):
    """Support for specification extensions
    
    This function adds support for specification extensions to a pydantic model.
    """
    @model_validator(mode="before")
    def specification_extensions(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        defined_fields = [field_name for field_name in cls.model_fields]
        defined_fields.extend([field.alias for _, field in cls.model_fields.items() if field.alias is not None])
        new_values = {}
        for field_name in values:
            if field_name not in defined_fields:
                new_values[f"x-{field_name.replace('_', '-')}"] = values[field_name]
            else:
                new_values[field_name] = values[field_name]
        return new_values
    cls.model_config.update(ConfigDict(
        extra="allow"
    ))    
    return create_model(
        cls.__name__,
        __base__=cls,
        __module__=cls.__module__,
        __validators__= {
            "specification_extensions": specification_extensions
        }
    )