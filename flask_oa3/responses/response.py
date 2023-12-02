from enum import IntEnum
from typing import Any, Dict, Union, ClassVar, Optional
from typing_extensions import Annotated
from pydantic import BaseModel, Field, computed_field
from ..media_types import MediaType
from ..component import Component, ComponentType

class ResponseType(IntEnum):
    """
    An enumeration to categorize response types based on HTTP status codes.

    Attributes:
        X_CUSTOM (int): Represents a custom or undefined status code.
        INFORMATIONAL (int): Represents informational responses (100–199).
        SUCCESSFUL (int): Represents successful responses (200–299).
        REDIRECT (int): Represents redirection messages (300–399).
        CLIENT_ERROR (int): Represents client error responses (400–499).
        SERVER_ERROR (int): Represents server error responses (500–599).
    """

    X_CUSTOM = -1
    INFORMATIONAL = 100
    SUCCESSFUL = 200
    REDIRECT = 300
    CLIENT_ERROR = 400
    SERVER_ERROR = 500

class Response(Component):
    """
    A base class for creating responses with a status code and data.

    Attributes:
        __STATUS_CODE__ (Union[int, None]): A class-level attribute that defines the status code for the response.
        data (Any): The data to be included in the response.
    """
    component_type: ClassVar[ComponentType] = ComponentType.RESPONSE

    __api_docs__: ClassVar[Dict[str, str]] = {}
    __STATUS_CODE__: ClassVar[Union[int, None]] = None
    __PHRASE__: ClassVar[Union[str, None]] = None

    description: Annotated[Optional[str], Field(default=None, description="REQUIRED. A description of the response. CommonMark syntax MAY be used for rich text representation.")]
    content: Annotated[Optional[Dict[str, MediaType]], Field(default=None, description="A map containing descriptions of potential response payloads. The key is a media type or media type range and the value describes it. For responses that match multiple keys, only the most specific key is applicable. e.g. text/plain overrides text/*")]
    
    @computed_field(alias="x-phrase", description="The phrase of the response reprisenting a short description / long name")
    @property
    def phrase(self) -> str:
        return self.__PHRASE__

    def add_media_type(self, media_type: type[MediaType]):
        """Adds a new media type to the content collection.

        This method inserts the given `media_type` into the collection,
        using its unique name as a key. It ensures that no duplicate media types
        are added to the collection.

        Args:
            media_type (BaseMediaType): The media type object to be added.

        Raises:
            TypeError: If the media_type argument is not an instance of BaseMediaType
            ValueError: If a media type with the same name already exists in the collection.
        """        
        if not issubclass(media_type, MediaType):
            raise TypeError("Improper media type")
        media_type_name = media_type._get_name()
        if media_type_name in self.content:
            raise ValueError("Media type already exists.")
        self.content[media_type_name] = media_type

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