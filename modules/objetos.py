from tupy import *

class Diamante(BaseImage):
    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None, cor: str | None = None) -> None:
        super().__init__(file, x,y)
        self._cor=cor

class Plataforma(Image):
    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None) -> None:
        super().__init__(file, x, y)
    def set_x(self, x: int) -> None:
        self._x = x

    def set_y(self, y: int) -> None:
        self._y = y

class Obstaculo(BaseImage):
    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None, tipo: str | None = None) -> None:
        super().__init__(file, x, y)
        self.tipo=tipo

class Cubo(Image):
    GRAVIDADE = 5

    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None) -> None:
        super().__init__(file, x, y)
        self.tempo_caindo_cubo = 0
        self._campo=Vazio('./assets/images/imagem-vazia1.png',self.x,self.y)
    def update(self) -> None:
        self.y += min(10, (self.tempo_caindo_cubo/30) * self.GRAVIDADE)
        self.tempo_caindo_cubo += 2
        self._campo._x=self._x
        self._campo._y=self._y
class Vazio(Image):
    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None) -> None:
        super().__init__(file, x, y)