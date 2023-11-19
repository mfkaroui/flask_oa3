from .base import Base

class Model(Base):
    def __init__(self, name: str):
        super().__init__(name)
