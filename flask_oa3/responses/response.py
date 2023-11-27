from enum import IntEnum
from typing import Any, Dict, Union
from ..media_types import MediaType

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

class BaseResponse:
    """
    A base class for creating responses with a status code and data.

    Attributes:
        __STATUS_CODE__ (Union[int, None]): A class-level attribute that defines the status code for the response.
        data (Any): The data to be included in the response.
    """
    __api_docs__: Dict[str, str] = {}
    __STATUS_CODE__: Union[int, None] = None
    __PHRASE__: Union[str, None] = None

    def __init__(self, description: Union[str, None] = None):
        """
        Initializes a new instance of BaseResponse.

        Args:
            data (Any): The data to be included in the response.
        """
        self.description = description
        self.content: Dict[str, MediaType] = {}
    
    def add_media_type(self, media_type: MediaType):
        """Adds a new media type to the content collection.

        This method inserts the given `media_type` into the collection,
        using its unique name as a key. It ensures that no duplicate media types
        are added to the collection.

        Args:
            media_type (MediaType): The media type object to be added.

        Raises:
            ValueError: If a media type with the same name already exists in the collection.
        """        
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
    def schema(self) -> dict:
        """Constructs the Open API 'Response Object' according to specifications

        Returns:
            dict: The Open API schema
        """     
        schema = {}
        if self.description is not None:
            schema["description"] = self.description
        if len(self.content) > 0:
            schema["content"] = {media_type_name: media_type.schema for media_type_name, media_type in self.content.items()}
        return schema