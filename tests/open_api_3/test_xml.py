import pytest
from flask_oa3.open_api_3.xml import XML
from pydantic_core import ValidationError

class TestXML:
    def test_xml_required_field(self):
        """Tests that XML has no required fields. Should raise no exceptions."""
        XML()

    def test_xml_specification_extensions(self, xml_specification_extensions_fixture):
        expected_schema: dict = {
            "x-some-data-1": "test",
            "x-some-data-2": "test",
            "x-some-data-3": "test"
        }
        assert xml_specification_extensions_fixture.oa3_schema == expected_schema
