from enum import IntEnum
from typing import Any, Union

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

    __STATUS_CODE__: Union[int, None] = None
    __PHRASE__: Union[str, None] = None

    def __init__(self, data: Any):
        """
        Initializes a new instance of BaseResponse.

        Args:
            data (Any): The data to be included in the response.
        """
        self.data = data

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
