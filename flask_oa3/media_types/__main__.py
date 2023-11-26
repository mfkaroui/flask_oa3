import os
from json import loads
from typing import List


if __name__ == "__main__":
    run_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(run_dir, "media_types.json"), "r", encoding="utf8") as file_handle:
        file_handle.seek(0)
        media_types_json = loads(file_handle.read())
    media_type_keys = []
    for media_type in media_types_json["media_types"]:
        media_type_keys.extend(list(media_type.keys()))
    media_type_keys = list(set(media_type_keys))
    media_type_class = f"""### AUTO-GENERATED ###
from typing import Union
from ..model import Model

class MediaType:    
    def __init__(self, {' = None, '.join(media_type_keys)} = None):
        self.model: Union[Model, None] = None
"""
    for key in media_type_keys:
        media_type_class = media_type_class + f"""        self.{key} = {key}
"""
    media_type_class = media_type_class + """
    def register_model(self, model: Model):
        self.model = model

    @property
    def schema(self):
        if self.model is None:
            raise ValueError("No model was registered to the media type. Unable to generate the schema")
        return {""" + f"""
            self.{media_types_json["oa3_schema"]["media_type"]}: """ + """{
                "schema": {
                    "$ref": self.model._get_component_name()
                }
            }
        }

class MediaTypes:
"""
    for m in media_types_json["media_types"]:
        media_type_name = m["media_type"].split("/")[-1].lower().replace("-", "_")
        media_type_class = media_type_class + f"""    media_type_{media_type_name} = MediaType("""
        for key in m:
            if isinstance(m[key], str):
                value = m[key].replace('"', "'")
                media_type_class = media_type_class + f"{key}=\"{value}\", "
            else:
                media_type_class = media_type_class + f"{key}={m[key]}, "
        media_type_class = media_type_class[:-2] + """)
"""
    with open(os.path.join(run_dir, "__init__.py"), "w", encoding="utf8") as file_handle:
        file_handle.truncate(0)
        file_handle.seek(0)
        file_handle.write(media_type_class)
    
    print("test")