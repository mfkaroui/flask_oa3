from typing import Union, TYPE_CHECKING

class BaseMediaType:
    __MEDIA_TYPE__: Union[str, None] = None

    def __init__(self, model = None) -> None:
        self.model = model

    def apply_model(self, model):
        self.model = model

    @classmethod
    def _get_name(cls) -> str:
        if cls.__MEDIA_TYPE__ is None:
            raise ValueError(f"The media type was not set")
        return cls.__MEDIA_TYPE__
    
    @property
    def schema(self) -> dict:
        """Constructs the Open API 'Media Type Object' according to specifications

        Returns:
            dict: The Open API schema
        """     
        schema = {
            "schema": {
                "$ref": self.model._get_component_name()
            }
        }
        examples = self.model._get_examples()
        if len(examples) > 0:
            schema["examples"] = {
                example_name: {
                    "$ref": example._get_component_name()
                } for example_name, example in examples
            }
        return schema