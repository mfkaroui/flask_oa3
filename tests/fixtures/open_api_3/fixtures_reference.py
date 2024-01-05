import pytest
from typing import Type, Optional
from typing_extensions import Annotated
from pydantic import BaseModel, Field

from flask_oa3.open_api_3.reference import Reference
from flask_oa3.open_api_3.schema import Schema


@pytest.fixture
def reference_schema_fixture(schema_class_fixture) -> Reference[Schema]:
    test_schema = Schema(schema_model=schema_class_fixture)
    yield Reference[Schema](component=test_schema)
