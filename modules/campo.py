from tupy import *

class Campo(BaseImage):

    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None) -> None:
        super().__init__(file, x, y)