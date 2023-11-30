import os
from json import loads
from typing import List

def to_pascal_case(input_str: str) -> str:
    # Split the string by both '/' and '-'
    parts = input_str.replace("/", "-").replace("_", "-").replace(" ", "-").split("-")

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
    with open(os.path.join(run_dir, "status_codes.json"), "r", encoding="utf8") as file_handle:
        file_handle.seek(0)
        status_codes_json = loads(file_handle.read())
    status_codes_class = f"""### AUTO-GENERATED ###
from typing import Union
from .response import Response, ResponseType

"""
    for status_code in status_codes_json:
        response_class_name = to_pascal_case(status_code["phrase"])
        status_codes_class = status_codes_class + f"""class Response{response_class_name}(Response):
    \"\"\"
    {status_code['description']}

    StatusCode:
        {status_code['code']}

    SpecTitle:
        {status_code['spec_title']}
    
    SpecReference:
        {status_code['spec_href']}
    \"\"\"
    __STATUS_CODE__: int = {status_code['code']}
    __PHRASE__: str = "{status_code['phrase']}"

"""
    status_codes_class = status_codes_class + """
def get_response_by_status_code(status_code: int) -> Union[type[Response], None]:
    \"\"\"
    Retrieves a Response object corresponding to a given HTTP status code.

    This function maps standard HTTP status codes to their respective Response class objects. It provides a convenient way to access Response objects based on the status code encountered in HTTP communication. 

    Args:
        status_code (int): The HTTP status code for which the corresponding Response object is required. 

    Returns:
        Union[type[Response], None]: Returns the Response class associated with the given status code. If the status code is not recognized, it returns None.
    \"\"\"

    responses = {"""
    for status_code in status_codes_json:
        response_class_name = to_pascal_case(status_code["phrase"])
        status_codes_class = status_codes_class + f"""
        \"{status_code['code']}\": Response{response_class_name},"""
    status_codes_class = status_codes_class + """
    }
    return responses.get(str(status_code), None)
"""
    with open(os.path.join(run_dir, "__init__.py"), "w", encoding="utf8") as file_handle:
        file_handle.truncate(0)
        file_handle.seek(0)
        file_handle.write(status_codes_class)
    
    print("test")