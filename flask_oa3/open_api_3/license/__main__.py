import os
from json import loads

def to_pascal_case(input_str: str) -> str:
    # Split the string by both '/' and '-'
    parts = input_str.replace("/", "-").replace("_", "-").replace(".", "_").replace("+", "-plus").split("-")

    # Capitalize the first letter of each part. If a part starts with a digit,
    # capitalize the first letter after the digit.
    pascal_parts = []
    for part in parts:
        if part[0].isdigit():
            # Find the index of the first non-digit character
            for i, char in enumerate(part):
                if not char.isdigit():
                    break
            # Capitalize the first non-digit character
            pascal_part = part[:i] + part[i].upper() + part[i+1:]
        else:
            pascal_part = part.capitalize()
        pascal_parts.append(pascal_part)
    return ''.join(pascal_parts)

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
        license_keys[key] = f"{license_keys[key]}"
    license_class = f"""### AUTO-GENERATED ###
from pydantic import Field, computed_field
from typing import ClassVar, Optional, List, Tuple, Dict, Union
from typing_extensions import Annotated

from .license import License

class PredefinedLicense(License):
    VERSION: ClassVar[str] = "{licenses_json['licenseListVersion']}"
    RELEASE_DATE: ClassVar[str] = "{licenses_json['releaseDate']}"

    name: ClassVar[None] = None
    identifier: ClassVar[None] = None
    
    @computed_field(alias=\"name\", description="REQUIRED. The license name used for the API.")
    @property
    def _name(self) -> str:
        return self.{licenses_json['oa3_schema']['name']}
    
    @computed_field(alias=\"identifier\", description="An SPDX license expression for the API. The identifier field is mutually exclusive of the url field.")
    @property
    def _identifier(self) -> str:
        return self.{licenses_json['oa3_schema']['identifier']}

""" + """
    @property
    def oa3_schema(self):
        schema = super().oa3_schema
        schema.update({"""
    for key in licenses_json["oa3_schema_extentions"]:
        license_class = license_class + f"""
            \"{licenses_json['oa3_schema_extentions'][key]}\": self.{key},"""
    license_class = license_class + """
        })
        return schema
"""

    for l in licenses_json["licenses"]:
        class_name = to_pascal_case(f"License_{l['licenseId']}")        
        license_class = license_class + f"""
class {class_name}(PredefinedLicense):
"""
        for key in l:
            if isinstance(l[key], str):
                value = l[key].replace('"', "'")
                license_class = license_class + f"""    {key}: ClassVar[{license_keys[key]}] = \"{value}\"
"""
            else:
                license_class = license_class + f"""    {key}: ClassVar[{license_keys[key]}] = {l[key]}
"""
            
#        license_class = license_class + f"""    license_{l['licenseId'].lower().replace('-', '_').replace('.', '_').replace('+', 'plus')} = License("""
#        for key in l:
#            if isinstance(l[key], str):
#                value = l[key].replace('"', "'")
#                license_class = license_class + f"{key}=\"{value}\", "
#            else:
#                license_class = license_class + f"{key}={l[key]}, "
#        license_class = license_class[:-2] + """)
#"""
    with open(os.path.join(run_dir, "__init__.py"), "w", encoding="utf8") as file_handle:
        file_handle.truncate(0)
        file_handle.seek(0)
        file_handle.write(license_class)
    
    print("test")