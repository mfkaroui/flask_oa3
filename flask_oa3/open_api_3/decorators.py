from typing import Dict, Any, Union
from pydantic import RootModel, BaseModel, model_validator, ConfigDict

def specification_extentions_support(cls: type[Union[RootModel, BaseModel]]):
    """Support for specification extentions
    
    This function adds support for specification extentions to a pydantic model.
    """
    @model_validator(mode="before")
    @classmethod
    def specification_extentions(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        defined_fields = [field_name for field_name, field in cls.model_fields.items() if field.alias != "extra"]  # to support alias

        new_values = {}
        for field_name in values:
            if field_name not in defined_fields:
                new_values[f"x-{field_name.replace('_', '-')}"] = values[field_name]
            else:
                new_values[field_name] = values[field_name]
        return new_values
    cls.specification_extentions = specification_extentions
    cls.model_config.update(ConfigDict(
        extra="allow"
    ))
    return cls