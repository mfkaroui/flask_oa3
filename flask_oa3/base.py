class Base:
    OPENAPI_VERSION = "3.1.0"
    def __init__(self, name: str) -> None:
        self.name = name

    @property
    def schema(self) -> dict:
        return {
            "openapi": self.OPENAPI_VERSION,
            
        }