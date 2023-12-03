import pytest
from ..api import API
from ..licenses import Licenses, License

class TestAPI:
    @pytest.mark.parametrize(("init_args, expected_state"), [
        (("test_api",), {
            "title": "test_api",
            "summary": None,
            "description": None,
            "terms_of_service": None,
            "contact": None,
            "license": None,
            "version": "dev",
            "namespaces": []
        }),
        (("test_api", None), {
            "title": "test_api",
            "summary": None,
            "description": None,
            "terms_of_service": None,
            "contact": None,
            "license": None,
            "version": "dev",
            "namespaces": []
        }),
        (("test_api", "1.0.0"), {
            "title": "test_api",
            "summary": None,
            "description": None,
            "terms_of_service": None,
            "contact": None,
            "license": None,
            "version": "1.0.0",
            "namespaces": []
        })
    ])
    def test__init__(self, init_args, expected_state):
        api = API(*init_args)
        for key in expected_state:
            assert api.__dict__[key] == expected_state[key]

    @pytest.mark.parametrize(("license"), [
        value for value in Licenses.__dict__.values() if isinstance(value, License)
    ])
    def test_set_spdx_license_info(self, license):
        api = API("test_api")
        api.set_spdx_license_info(license, "https://google.com")
        assert "url" in api.license and api.license["url"] == "https://google.com"
        for key, value in license.schema.items():
            assert key in api.license and value == api.license[key]