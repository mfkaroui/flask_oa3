from typing import Optional, Dict, ClassVar
from typing_extensions import Annotated
from pydantic import Field, computed_field
from .component import Component, ComponentType
from .media_type import MediaType

class RequestBody(Component):
    component_type: ClassVar[ComponentType] = ComponentType.REQUEST_BODY

    description: Annotated[Optional[str], Field(default=None, description="A brief description of the request body. This could contain examples of use. CommonMark syntax MAY be used for rich text representation.")]
    required: Annotated[Optional[bool], Field(default=None, description="Determines if the request body is required in the request. Defaults to false.")]
    _content: ClassVar[Dict[str, MediaType]] = {}

    @computed_field(description="REQUIRED. The content of the request body. The key is a media type or media type range and the value describes it. For requests that match multiple keys, only the most specific key is applicable. e.g. text/plain overrides text/*")
    @property
    def content(self) -> Dict[str, MediaType]:
        return self._content
    
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

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Request Body Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#request-body-object
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)