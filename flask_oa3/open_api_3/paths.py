from typing import Dict
from typing_extensions import Annotated
from pydantic import RootModel, Field, field_validator
from .path_item import PathItem


class Paths(RootModel):
    root: Annotated[
        Dict[str, PathItem],
        Field(
            description="A relative path to an individual endpoint. The field name MUST begin with a forward slash (/). The path is appended (no relative URL resolution) to the expanded URL from the Server Object’s url field in order to construct the full URL. Path templating is allowed. When matching URLs, concrete (non-templated) paths would be matched before their templated counterparts. Templated paths with the same hierarchy but different templated names MUST NOT exist as they are identical. In case of ambiguous matching, it's up to the tooling to decide which one to use."
        ),
    ]

    @field_validator("root")
    def check_paths(cls, v):
        for path in v:
            if not path.startswith("/"):
                raise ValueError("The field name MUST begin with a forward slash (/).")
            if "{" in path:
                templated_path = path.split("{")[0]
                if any(
                    other_path.startswith(templated_path)
                    for other_path in v
                    if other_path != path
                ):
                    raise ValueError(
                        "Templated paths with the same hierarchy but different templated names MUST NOT exist as they are identical."
                    )
        return v

    @property
    def oa3_schema(self) -> dict:
        """Constructs the Open API 'Paths Object' according to specifications

        Spec:
            https://spec.openapis.org/oas/v3.1.0#paths-object

        Returns:
            dict: The Open API schema
        """
        return self.dict(by_alias=True, exclude_none=True)
