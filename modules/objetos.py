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
    GRAVIDADE = 2

    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None) -> None:
        super().__init__(file, x, y)
        self.tempo_caindo_cubo = 0

    def update(self):
        self.y += min(4.9, (self.tempo_caindo_cubo/30)*self.GRAVIDADE)
        self.tempo_caindo_cubo += 2
        for lista in plataformas:
            for item in lista:
                if self._collides_with(item):
                    self.tempo_caindo_cubo = 0
        if self._collides_with(elevador):
            self.tempo_caindo_cubo = 0
        if self._collides_with(boy):
            self.x += boy.velocidade_atual.x
        if self._collides_with(girl):
            self.x += girl.velocidade_atual.x
