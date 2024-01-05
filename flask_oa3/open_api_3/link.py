from typing import Optional, Dict, Any, Union, ClassVar
from typing_extensions import Annotated
from pydantic import Field, field_serializer
from .component import Component, ComponentType
from .runtime_expression import RuntimeExpression
from .server import Server


class Link(Component):
    component_type: ClassVar[ComponentType] = ComponentType.LINK

    operation_reference: Annotated[
        Optional[str],
        Field(
            default=None,
            alias="operationRef",
            description="A relative or absolute URI reference to an OAS operation. This field is mutually exclusive of the operationId field, and MUST point to an Operation Object. Relative operationRef values MAY be used to locate an existing Operation Object in the OpenAPI definition. See the rules for resolving Relative References.",
        ),
    ]
    operation_id: Annotated[
        Optional[str],
        Field(
            default=None,
            alias="operationId",
            description="The name of an existing, resolvable OAS operation, as defined with a unique operationId. This field is mutually exclusive of the operationRef field.",
        ),
    ]
    parameters: Annotated[
        Optional[Dict[str, Union[RuntimeExpression, Any]]],
        Field(
            default=None,
            description="A map representing parameters to pass to an operation as specified with operationId or identified via operationRef. The key is the parameter name to be used, whereas the value can be a constant or an expression to be evaluated and passed to the linked operation. The parameter name can be qualified using the parameter location [{in}.]{name} for operations that use the same parameter name in different locations (e.g. path.id).",
        ),
    ]
    request_body: Annotated[
        Optional[Union[RuntimeExpression, Any]],
        Field(
            default=None,
            alias="requestBody",
            description="A literal value or {expression} to use as a request body when calling the target operation.",
        ),
    ]
    description: Annotated[
        Optional[str],
        Field(
            default=None,
            description="	A description of the link. CommonMark syntax MAY be used for rich text representation.",
        ),
    ]
    server: Annotated[
        Optional[Server],
        Field(
            default=None,
            description="A server object to be used by the target operation.",
        ),
    ]

    @field_serializer("parameters")
    def parameters_serializer(
        self, parameters: Optional[Dict[str, Union[RuntimeExpression, Any]]], _info
    ) -> Union[Any, None]:
        if parameters is not None:
            return {
                parameter_name: value.expression
                if isinstance(value, RuntimeExpression)
                else value
                for parameter_name, value in parameters.items()
            }
        return None

    @field_serializer("request_body")
    def request_body_serializer(
        self, request_body: Optional[Union[RuntimeExpression, Any]], _info
    ) -> Union[Any, None]:
        if request_body is not None:
            return (
                request_body.expression
                if isinstance(request_body, RuntimeExpression)
                else request_body
            )
        return None

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Link Object' according to specifications

        Spec:
            https://spec.openapis.org/oas/v3.1.0#link-object

        Returns:
            dict: The Open API schema
        """
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)
