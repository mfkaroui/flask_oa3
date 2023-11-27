import os
from json import loads
from typing import List


if __name__ == "__main__":
    run_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(run_dir, "status_codes.json"), "r", encoding="utf8") as file_handle:
        file_handle.seek(0)
        status_codes_json = loads(file_handle.read())
    status_codes_class = f"""### AUTO-GENERATED ###
from typing import Union
from .response import BaseResponse, ResponseType

"""
    for status_code in status_codes_json:
        status_codes_class = status_codes_class + f"""class {status_code['phrase'].replace(' ', '').replace('-', '')}Response(BaseResponse):
    \"\"\"
    {status_code['description']}

    SpecTitle:
        {status_code['spec_title']}
    
    SpecReference:
        {status_code['spec_href']}
    \"\"\"
    __STATUS_CODE__: int = {status_code['code']}
    __PHRASE__: str = "{status_code['phrase']}"

"""
    status_codes_class = status_codes_class + """
def get_response_by_status_code(status_code: int) -> Union[BaseResponse, None]:
    responses = {"""
    for status_code in status_codes_json:
        status_code_name = f"{status_code['phrase'].replace(' ', '').replace('-', '')}Response"
        status_codes_class = status_codes_class + f"""
            \"{status_code['code']}\": {status_code_name},"""
    status_codes_class = status_codes_class + """
    }
    return responses.get(str(status_code), None)
"""
    with open(os.path.join(run_dir, "__init__.py"), "w", encoding="utf8") as file_handle:
        file_handle.truncate(0)
        file_handle.seek(0)
        file_handle.write(status_codes_class)
    
    print("test")