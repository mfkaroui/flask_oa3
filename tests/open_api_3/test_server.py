import pytest
from flask_oa3.open_api_3.server import Server
from pydantic_core import ValidationError


class TestServer:
    def test_server_required_field(self):
        with pytest.raises(ValidationError) as validation_error:
            Server()
        server_errors = validation_error.value.errors()
        assert len(server_errors) == 1
        assert server_errors[0]["type"] == "missing"
        assert server_errors[0]["loc"] == ("url",)

    def test_server_specification_extensions(
        self, server_specification_extensions_fixture
    ):
        expected_schema: dict = {
            "url": "http://test.com/",
            "x-some-data-1": "test",
            "x-some-data-2": "test",
            "x-some-data-3": "test",
        }
        assert server_specification_extensions_fixture.oa3_schema == expected_schema

    def test_server_oa3_schema(self, server_with_description_server_variables_fixture):
        expected_schema: dict = {
            "url": "http://{test}.com/",
            "description": "test description",
            "variables": {
                "test": {
                    "enum": ["test1", "test2"],
                    "default": "test1",
                    "description": "test description",
                }
            },
        }
        assert (
            server_with_description_server_variables_fixture.oa3_schema
            == expected_schema
        )

    @pytest.mark.parametrize(
        ("url",),
        [
            ("http://test.com/{test}/",),
            ("http://{username}:{password}@{test}.com/",),
            ("http://{test}.com/",),
            ("http://test.com/{test}/{test2}/",),
            ("{protocol}://test.com/{test}/{test2}/",),
            ("http://{host_name}:{port-number}.com/{test}/{test2}/",),
        ],
    )
    def test_server_no_variables_match_fail(self, url):
        with pytest.raises(NameError) as validation_error:
            Server(url=url)

    @pytest.mark.parametrize(
        ("url",),
        [
            ("http://test.com/{test}/",),
            ("http://{username}:{password}@{test}.com/",),
            ("http://{test}.com/",),
            ("http://test.com/{test}/{test2}/",),
            ("{protocol}://test.com/{test}/{test2}/",),
            ("http://{host_name}:{port-number}.com/{test}/{test2}/",),
        ],
    )
    def test_server_variables_match_fail(self, url):
        with pytest.raises(NameError) as validation_error:
            Server(url=url, variables={"test_unused": {"default": "test"}})

    @pytest.mark.parametrize(
        ("url",),
        [
            ("http://test.com/",),
            ("http://test.com/{test}/",),
            ("http://{username}:{password}@{test}.com/",),
            ("http://{test}.com/",),
            ("http://test.com/{test}/{test2}/",),
            ("{protocol}://test.com/{test}/{test2}/",),
            ("http://{host_name}:{port-number}.com/{test}/{test2}/",),
        ],
    )
    def test_server_variables_match_pass(self, url):
        Server(
            url=url,
            variables={
                "test": {"default": "test"},
                "test2": {"default": "test"},
                "username": {"default": "test"},
                "password": {"default": "test"},
                "protocol": {"default": "test"},
                "host_name": {"default": "test"},
                "port-number": {"default": "test"},
            },
        )
