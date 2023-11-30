from enum import StrEnum

class APIProvider(StrEnum):
    DJANGO = "django"
    FASTAPI = "fastapi"
    FLASK = "flask"