from typing import Optional, Any, ClassVar
from typing_extensions import Annotated
from pydantic import Field, AnyUrl
from .component import Component, ComponentType

class Example(Component):
    component_type: ClassVar[ComponentType] = ComponentType.EXAMPLE

    summary: Annotated[Optional[str], Field(default=None, description="Short description for the example.")]
    description: Annotated[Optional[str], Field(default=None, description="Long description for the example. CommonMark syntax MAY be used for rich text representation.")]
    value: Annotated[Optional[Any], Field(default=None, description="Embedded literal example. The value field and externalValue field are mutually exclusive. To represent examples of media types that cannot naturally represented in JSON or YAML, use a string value to contain the example, escaping where necessary.")]
    external_value: Annotated[Optional[AnyUrl], Field(default=None, alias="externalValue", description="A URI that points to the literal example. This provides the capability to reference examples that cannot easily be included in JSON or YAML documents. The value field and externalValue field are mutually exclusive. See the rules for resolving Relative References.")]

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Example Object' according to specifications
        
        Spec:
            https://spec.openapis.org/oas/v3.1.0#example-object
        
        Returns:
            dict: The Open API schema
        """        
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)