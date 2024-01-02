from typing import List, ClassVar, Annotated
from pydantic import BaseModel, Field, model_validator
from abnf import Rule

class RuntimeExpression(BaseModel):
    """Runtime expressions allow defining values based on information that will only be available within the HTTP message in 
    an actual API call. This mechanism is used by Link Objects and Callback Objects.
    
    Spec:
    https://spec.openapis.org/oas/v3.1.0#runtimeExpression
    """
    grammar: ClassVar[List[str]] = [
        Rule.create('expression = ( "$url" / "$method" / "$statusCode" / "$request." source / "$response." source )'),
        Rule.create('source = ( header-reference / query-reference / path-reference / body-reference )'),
        Rule.create('header-reference = "header." token'),
        Rule.create('query-reference = "query." name'),
        Rule.create('path-reference = "path." name'),
        Rule.create('body-reference = "body" ["#" json-pointer ]'),
        Rule.create('json-pointer    = *( "/" reference-token )'),
        Rule.create('reference-token = *( unescaped / escaped )'),
        Rule.create('unescaped       = %x00-2E / %x30-7D / %x7F-10FFFF'),
        Rule.create('escaped         = "~" ( "0" / "1" )'),
        Rule.create('name = *( CHAR )'),
        Rule.create('token = 1*tchar'),
        Rule.create('tchar = "!" / "#" / "$" / "%" / "&" / "\'" / "*" / "+" / "-" / "." / "^" / "_" / "`" / "|" / "~" / DIGIT / ALPHA')
    ]

    expression: Annotated[str, Field(description="")]

    @model_validator(mode="before")
    @classmethod
    def check_expression(cls, values):
        cls.grammar[0].parse(values["expression"], 0)
        return values
