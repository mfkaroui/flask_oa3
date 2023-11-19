import os
from json import loads
from typing import List


if __name__ == "__main__":
    run_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(run_dir, "licenses.json"), "r", encoding="utf8") as file_handle:
        file_handle.seek(0)
        licenses_json = loads(file_handle.read())
    license_keys = []
    for license in licenses_json["licenses"]:
        license_keys.extend(list(license.keys()))
    license_keys = list(set(license_keys))
    license_class = f"""### AUTO-GENERATED ###
class License:
    VERSION: str = "{licenses_json['licenseListVersion']}"
    RELEASE_DATE: str = "{licenses_json['releaseDate']}"
    
    def __init__(self, {', '.join(license_keys)}):
"""
    for key in license_keys:
        license_class = license_class + f"""        self.{key} = {key}
"""
    license_class = license_class + """

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