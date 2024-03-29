from enum import IntEnum
from typing import Dict, Union, ClassVar, Optional, Type
from typing_extensions import Annotated
from pydantic import Field, computed_field, model_serializer
from ..media_type import MediaType
from ..component import Component, ComponentType
from ..decorators import specification_extensions_support

class ResponseType(IntEnum):
    """
    An enumeration to categorize response types based on HTTP status codes.
    """

    X_CUSTOM = -1  # Represents a custom or undefined status code.
    INFORMATIONAL = 100  # Represents informational responses (100–199).
    SUCCESSFUL = 200  # Represents successful responses (200–299).
    REDIRECT = 300  # Represents redirection messages (300–399).
    CLIENT_ERROR = 400  # Represents client error responses (400–499).
    SERVER_ERROR = 500  # Represents server error responses (500–599).

@specification_extensions_support
class Response(Component):
    component_type: ClassVar[ComponentType] = ComponentType.RESPONSE

    __STATUS_CODE__: ClassVar[Union[int, None]] = None
    __PHRASE__: ClassVar[Union[str, None]] = None

    description: Annotated[
        Optional[str],
        Field(
            default=None,
            description="REQUIRED. A description of the response. CommonMark syntax MAY be used for rich text representation.",
        ),
    ]
    _content: Dict[str, Type[MediaType]] = {}

    @model_serializer(mode="wrap")
    def serialize_component(self, handler):
        exclude = ["_content"]
        d = handler(self)
        d = {k: v for k, v in d.items() if k not in exclude}
        return d

    @computed_field(
        alias="x-phrase",
        description="The phrase of the response reprisenting a short description / long name",
    )
    @property
    def phrase(self) -> str:
        return self.__PHRASE__

    @computed_field(
        description="A map containing descriptions of potential response payloads. The key is a media type or media type range and the value describes it. For responses that match multiple keys, only the most specific key is applicable. e.g. text/plain overrides text/*"
    )
    @property
    def content(self) -> Union[Dict[str, MediaType], None]:
        return None if len(self._content) == 0 else self._content

    def add_media_type(self, media_type: MediaType):
        """Adds a new media type to the content collection.

        This method inserts the given `media_type` into the collection,
        using its unique name as a key. It ensures that no duplicate media types
        are added to the collection.

        Args:
            media_type (MediaType): The media type object to be added.

        Raises:
            TypeError: If the media_type argument is not an instance of MediaType
            ValueError: If a media type with the same name already exists in the collection.
        """
        if not isinstance(media_type, MediaType):
            raise TypeError("Improper media type")
        media_type_name = media_type._get_name()
        if media_type_name in self._content:
            raise ValueError("Media type already exists.")
        self._content[media_type_name] = media_type

    @classmethod
    def _get_response_type(cls) -> ResponseType:
        """
        This method checks the class's status code and categorizes it into one of the defined response types.

        Returns:
            ResponseType: The type of response corresponding to the status code.

        Raises:
            ValueError: If the status code is not defined.
        """
        if cls.__STATUS_CODE__ is None:
            raise ValueError("Status code is not defined")
        if cls.__STATUS_CODE__ < 100 or cls.__STATUS_CODE__ >= 600:
            return ResponseType.X_CUSTOM
        else:
            return ResponseType(int(f"{str(cls.__STATUS_CODE__)[0]}00"))

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Response Object' according to specifications

        Spec:
            https://spec.openapis.org/oas/v3.1.0#response-object

        Returns:
            dict: The Open API schema
        """
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)
