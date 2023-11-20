import pytest
from ..decorators import specification_extensions_support
from ..errors import ReservedSpecificationExtentionError

class TestDecorators:
    def test_specification_extensions_support(self):
        @specification_extensions_support
        def test_function(**specification_extensions):
            for key in specification_extensions:
                assert key.startswith("x-")
        
        test_function(x="", y="", z="")

        with pytest.raises(ReservedSpecificationExtentionError):
            test_function(oas_a="test")
        
        with pytest.raises(ReservedSpecificationExtentionError):
            test_function(oai_a="test")