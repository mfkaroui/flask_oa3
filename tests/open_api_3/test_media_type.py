import os
from typing import List
import pytest
from json import load
from flask_oa3.open_api_3.media_type import MediaType, get_media_type_by_name


def get_predefined_media_types() -> List[dict]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    media_types_path = os.path.join(
        dir_path, "../../flask_oa3/open_api_3/media_type/media_types.json"
    )
    with open(media_types_path, encoding="utf8") as f:
        f.seek(0)
        return load(f)


class TestResponse:
    @pytest.mark.parametrize("predefined_media_type", get_predefined_media_types())
    def test_get_media_type_by_name(self, predefined_media_type: dict):
        media_type = get_media_type_by_name(predefined_media_type["media_type"])
        assert issubclass(media_type, MediaType)
        assert media_type.__MEDIA_TYPE__ == predefined_media_type["media_type"]
