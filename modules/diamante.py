from tupy import *

class Diamante(BaseImage):
    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None, cor: str | None = None) -> None:
        super().__init__(file, x,y)
        self._cor=cor
