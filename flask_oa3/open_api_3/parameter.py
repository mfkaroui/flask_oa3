from typing import Optional, ClassVar, Dict, Union
from typing_extensions import Annotated
from enum import Enum
from pydantic import Field
from .component import Component, ComponentType
from .example import Example
from .reference import Reference
from .schema import Schema


class ParameterLocation(Enum):
    PATH = "path"  # Used together with Path Templating, where the parameter value is actually part of the operation’s URL. This does not include the host or base path of the API. For example, in /items/{itemId}, the path parameter is itemId.
    QUERY = "query"  # Parameters that are appended to the URL. For example, in /items?id=###, the query parameter is id.
    HEADER = "header"  # Custom headers that are expected as part of the request. Note that [RFC7230] states header names are case insensitive.
    COOKIE = "cookie"  # Used to pass a specific cookie value to the API.


class ParameterStyle(Enum):
    MATRIX = "matrix"  # Path-style parameters defined by [RFC6570], that is, using ; rather than /. This option replaces collectionFormat with a csv (when explode is false) or multi (when explode is true) value from OpenAPI 2.0.
    LABEL = "label"  # Label style parameters defined by [RFC6570], that is, using .labelname. This option replaces collectionFormat with a csv (when explode is false) or multi (when explode is true) value from OpenAPI 2.0.
    FORM = "form"  # Form style parameters defined by [RFC6570], that is, using & and a semicolon-separated list of keys. This option replaces collectionFormat with a csv (when explode is false) or multi (when explode is true) value from OpenAPI 2.0.
    SIMPLE = "simple"  # Simple style parameters defined by [RFC6570], that is, using a comma-separated list of values. This option replaces collectionFormat with commas. openapi 3.0.0
    SPACE_DELIMITED = "spaceDelimited"  # Space separated array values. This option replaces collectionFormat equal to ssv from OpenAPI 2.0.
    PIPE_DELIMITED = "pipeDelimited"  # Pipe separated array values. This option replaces collectionFormat equal to pipes from OpenAPI 2.0.
    DEEP_OBJECT = "deepObject"  # Provides a simple way of rendering nested objects using form parameters. openapi 3.0.0


class Parameter(Component):
    component_type: ClassVar[ComponentType] = ComponentType.PARAMETER
    name: Annotated[
        str,
        Field(
            default=None,
            description="REQUIRED. The name of the parameter. Parameter names are case sensitive.",
        ),
    ]
    in_location: Annotated[
        Optional[ParameterLocation],
        Field(
            default=None,
            alias="in",
            description='REQUIRED. The location of the parameter. Possible values are "query", "header", "path" or "cookie".',
        ),
    ]
    description: Annotated[
        Optional[str],
        Field(
            default=None,
            description="A brief description of the parameter. This could contain examples of use. CommonMark syntax MAY be used for rich text representation.",
        ),
    ]
    required: Annotated[
        Optional[str],
        Field(
            default=None,
            description='Determines whether this parameter is mandatory. If the parameter location is "path", this property is REQUIRED and its value MUST be true. Otherwise, the property MAY be included and its default value is false.',
        ),
    ]
    deprecated: Annotated[
        Optional[str],
        Field(
            default=None,
            description="Specifies that a parameter is deprecated and SHOULD be transitioned out of usage. Default value is false.",
        ),
    ]
    style: Annotated[
        Optional[ParameterStyle],
        Field(
            default=None,
            description="Describes how the parameter value will be serialized depending on the type of the parameter value. Default values (based on value of in): for query - form; for path - simple; for header - simple; for cookie - form.",
        ),
    ]
    explode: Annotated[
        Optional[bool],
        Field(
            default=None,
            description="When this is true, parameter values of type array or object generate separate parameters for each value of the array or key-value pair of the map. For other types of parameters this property has no effect. When style is form, the default value is true. For all other styles, the default value is false.",
        ),
    ]
    allow_reserved: Annotated[
        Optional[bool],
        Field(
            default=None,
            alias="allowReserved",
            description="Determines whether the parameter value SHOULD allow reserved characters, as defined by [RFC3986] :/?#[]@!$&'()*+,;= to be included without percent-encoding. This property only applies to parameters with an in value of query. The default value is false.",
        ),
    ]
    schema: Annotated[
        Optional[Schema],
        Field(
            default=None,
            description="The schema defining the type used for the parameter.",
        ),
    ]
    examples: Annotated[
        Optional[Dict[str, Union[Example, Reference[Example]]]],
        Field(
            default=None,
            description="Examples of the parameter’s potential value. Each example SHOULD contain a value in the correct format as specified in the parameter encoding. The examples field is mutually exclusive of the example field. Furthermore, if referencing a schema that contains an example, the examples value SHALL override the example provided by the schema.",
        ),
    ]

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Parameter Object' according to specifications

        Spec:
            https://spec.openapis.org/oas/v3.1.0#parameter-object

        Returns:
            dict: The Open API schema
        """
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)
