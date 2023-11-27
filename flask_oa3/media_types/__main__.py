import os
from json import loads
from typing import List

def to_pascal_case(input_str: str) -> str:
    # Split the string by both '/' and '-'
    parts = input_str.replace("/", "-").replace("_", "-").split("-")

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
    with open(os.path.join(run_dir, "media_types.json"), "r", encoding="utf8") as file_handle:
        file_handle.seek(0)
        media_types_json = loads(file_handle.read())
    media_types_class = f"""### AUTO-GENERATED ###
from .media_type import BaseMediaType

"""
    for media_type in media_types_json:
        media_type_name = to_pascal_case(media_type["media_type"])

        media_types_class = media_types_class + f"""class {media_type_name}(BaseMediaType):
    \"\"\"
    Template:
        {media_type['template']}

    SpecTitle:
        {media_type['spec_title']}
    
    SpecReference:
        {media_type['spec_href']}
    \"\"\"
    __MEDIA_TYPE__: str = \"{media_type['media_type']}\"

"""
    with open(os.path.join(run_dir, "__init__.py"), "w", encoding="utf8") as file_handle:
        file_handle.truncate(0)
        file_handle.seek(0)
        file_handle.write(media_types_class)
    
    print("test")