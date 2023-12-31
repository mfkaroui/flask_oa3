import pytest
from typing import Type, Optional, Dict, List
from typing_extensions import Annotated, Literal
from pydantic import BaseModel, Field
from flask_oa3.open_api_3.schema import Schema, Discriminator


@pytest.fixture
def discriminator_fixture() -> Discriminator:
    return Discriminator(property_name="test_property")


@pytest.fixture
def discriminator_specification_extensions_fixture() -> Discriminator:
    return Discriminator(
        property_name="test_property",
        some_data_1="test",
        some_data_2="test",
        some_data_3="test",
    )


@pytest.fixture
def schema_class_fixture() -> Type[BaseModel]:
    class TestSchema(BaseModel):
        int_field: Annotated[int, Field(description="An integer field")]
        str_field: Annotated[str, Field(description="A string field")]
        optional_field: Annotated[
            Optional[str], Field(default=None, description="An optional field")
        ]

    yield TestSchema


@pytest.fixture
def schema_with_specification_extensions_fixture(schema_class_fixture) -> Schema:
    yield Schema(
        schema_model=schema_class_fixture,
        some_data_1="test",
        some_data_2="test",
        some_data_3="test",
    )


@pytest.fixture
def schema_class_python_inheritance_fixture(schema_class_fixture) -> Type[BaseModel]:
    class PythonInheritanceTestSchema(schema_class_fixture):
        int_field: Annotated[int, Field(description="An integer field override")]
        bool_field: Annotated[bool, Field(description="A boolean field")]

    yield PythonInheritanceTestSchema


@pytest.fixture
def schema_class_with_dict_fixture() -> Type[BaseModel]:
    class DictTestSchema(BaseModel):
        test_discriminator: Literal["dict", "list"] = "dict"
        dict_field: Annotated[Dict[str, int], Field(description="A dict field")]

    yield DictTestSchema


@pytest.fixture
def schema_class_with_list_fixture() -> Type[BaseModel]:
    class ListTestSchema(BaseModel):
        test_discriminator: Literal["dict", "list"] = "list"
        list_field: Annotated[List[str], Field(description="A list field")]

    yield ListTestSchema


@pytest.fixture
def schema_class_with_nested_model(schema_class_fixture) -> Type[BaseModel]:
    class NestedTestSchema(BaseModel):
        nested_field: schema_class_fixture
        list_field: Annotated[List[str], Field(description="A list field")]

    yield NestedTestSchema
