from tupy import *

class Diamante(BaseImage):

    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None, cor: str | None = None) -> None:
        
        super().__init__(file, x,y)
        self._cor = cor

class Obstaculo(BaseImage):

    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None, tipo: str | None = None) -> None:
        
        super().__init__(file, x, y)
        self._tipo = tipo

class Cubo(Image):
    GRAVIDADE = 5

    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None) -> None:
        
        super().__init__(file, x, y)
        self.tempo_caindo_cubo = 0
        self._campo = Vazio('./assets/images/imagem-vazia1.png',self.x,self.y)

    def update(self) -> None:
        
        self.y += min(10, (self.tempo_caindo_cubo/30) * self.GRAVIDADE)
        self.tempo_caindo_cubo += 2
        self._campo.x = self.x
        self._campo.y = self.y

class Vazio(Image):

    def __init__(self, file: str, x: int, y: int) -> None:
        
        super().__init__(file, x, y)

class Botao(Image):

    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None, cor: str | None = None) -> None:
        
        super().__init__(file, x,y)
        self._campo = Vazio('./assets/images/imagem-vazia2.png',self.x,self.y)

class Elevador(BaseImage):

    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None) -> None:
        
        super().__init__(file, x, y)
        self._pilha = 0

class Plataforma(Image):
    
    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None) -> None:
        
        super().__init__(file, x, y)

    def set_x(self, x: int) -> None:
        
        self._x = x

    def set_y(self, y: int) -> None:
        
        self._y = y