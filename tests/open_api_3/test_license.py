import os
from typing import List
import pytest
from json import load
from flask_oa3.open_api_3.license import License, PredefinedLicense, get_license_by_id


def get_predefined_licences() -> List[dict]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    licenses_path = os.path.join(
        dir_path, "../../flask_oa3/open_api_3/license/licenses.json"
    )
    with open(licenses_path, encoding="utf8") as f:
        f.seek(0)
        return load(f)["licenses"]


class TestPredefinedLicense:
    @pytest.mark.parametrize("predefined_license", get_predefined_licences())
    def test_get_license_by_id(self, predefined_license: dict):
        license = get_license_by_id(predefined_license["licenseId"])
        assert issubclass(license, PredefinedLicense)
        assert license()._name == predefined_license["longName"]
        assert license()._identifier == predefined_license["licenseId"]
        assert license()._reference == predefined_license["reference"]
        assert (
            license()._referenceNumber
            == predefined_license["referenceNumber"]
        )
        assert (
            license()._isDeprecatedLicenseId
            == predefined_license["isDeprecatedLicenseId"]
        )
        assert (
            license()._isOsiApproved == predefined_license["isOsiApproved"]
        )
