from typing import Union, TYPE_CHECKING

class BaseMediaType:
    if TYPE_CHECKING:
        from ..model import Model

    __MEDIA_TYPE__: Union[str, None] = None

    def __init__(self, model: Union[Model, None] = None) -> None:
        self.model = model

    def apply_model(self, model: Model):
        self.model = model

    @classmethod
    def _get_name(cls) -> str:
        if cls.__MEDIA_TYPE__ is None:
            raise ValueError(f"The media type was not set")
        return cls.__MEDIA_TYPE__