import os
from json import loads
from typing import List
from pydantic import create_model

if __name__ == "__main__":
    run_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(run_dir, "licenses.json"), "r", encoding="utf8") as file_handle:
        file_handle.seek(0)
        licenses_json = loads(file_handle.read())
    license_keys = {}
    for license in licenses_json["licenses"]:
        for key, value in license.items():
            if key not in license_keys:
                license_keys[key] = []
            key_type = type(value).__name__
            if key_type == "list":
                if len(value) > 0:
                    list_types = []
                    for item in value:
                        list_types.append(type(item).__name__)
                    list_types = list(set(list_types))
                    if len(list_types) == 1:
                        license_keys[key].append(f"List[{list_types[0]}]")
                    else:
                        license_keys[key].append(f"List[Union[{','.join(list_types)}]]")
            elif key_type == "tuple":
                pass
            elif key_type == "dict":
                pass
            else:
                license_keys[key].append(key_type)
            license_keys[key] = list(set(license_keys[key]))
    for key in license_keys:
        if len(license_keys[key]) == 1:
            license_keys[key] = license_keys[key][0]
        else:
            license_keys[key] = f"Union[{','.join(license_keys[key])}]"
        license_keys[key] = f"Optional[{license_keys[key]}]"
    license_class = f"""### AUTO-GENERATED ###
from pydantic import BaseModel
from typing import ClassVar, List, Dict, Tuple, Union, Optional

class License(BaseModel):
    VERSION: ClassVar[str] = "{licenses_json['licenseListVersion']}"
    RELEASE_DATE: ClassVar[str] = "{licenses_json['releaseDate']}"
    
"""
    for key in license_keys:
        license_class = license_class + f"""    {key}: {license_keys[key]}
"""
    license_class = license_class + """
    @property
    def oa3_schema(self):
        return {
"""
    for key in licenses_json["oa3_schema"]:
        license_class = license_class + f"""            '{key}': self.{licenses_json["oa3_schema"][key]},
"""
    license_class = license_class + """        }

class Licenses:
"""
    for l in licenses_json["licenses"]:
        license_class = license_class + f"""    license_{l['licenseId'].lower().replace('-', '_').replace('.', '_').replace('+', 'plus')} = License("""
        for key in l:
            if isinstance(l[key], str):
                value = l[key].replace('"', "'")
                license_class = license_class + f"{key}=\"{value}\", "
            else:
                license_class = license_class + f"{key}={l[key]}, "
        license_class = license_class[:-2] + """)
"""
    with open(os.path.join(run_dir, "__init__.py"), "w", encoding="utf8") as file_handle:
        file_handle.truncate(0)
        file_handle.seek(0)
        file_handle.write(license_class)
    
    print("test")