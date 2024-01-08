import pytest
from flask_oa3.open_api_3.runtime_expression import RuntimeExpression

@pytest.mark.parametrize(
    "expression",
    [
        "$url",
        "$method",
        "$request.path.eventType",
        "$request.query.queryUrl",
        "$request.header.content-Type",
        "$request.body#/failedUrl",
        "$request.body#/successUrls/2",
        "$response.header.Location",
    ],
)
def test_parse_expression_success(expression):
    try:
        RuntimeExpression(expression=expression)
    except Exception as e:
        pytest.fail(f"Failed to parse expression: {expression}. Error: {str(e)}")

@pytest.mark.parametrize(
    "expression",
    [
        "$request.source",
        "$response.source",
        "header.token",
        "query.name",
        "path.name",
        "body",
        "body#json-pointer",
        "json-pointer",
        "unescaped",
        "escaped",
        "CHAR",
        "tchar",
    ],
)
def test_parse_expression_failure(expression):
    with pytest.raises(Exception):
        RuntimeExpression(expression=expression)
