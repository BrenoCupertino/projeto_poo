from typing import Optional
from tupy import *
from modules.personagem import Personagem
from modules.botao import Botao
from modules.campo import Campo

""" class botao1(Botao):
    def __init__(self,x,y,boy,girl):
        super().__init__(x,y)
        self._boy=boy
        self._girl=girl
        
    def update(self):
        if self._collides_with(self._boy):
            self._c1=True
        elif self._collides_with(self._girl):
            self._c1=True 
        super().update()  """


class Plataforma(BaseImage):
    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None) -> None:
        super().__init__(file, x, y)
    
    def set_x(self, x: int) -> None:
        self._x = x

    def set_y(self, y: int) -> None:
        self._y = y

if __name__ == '__main__':
    nivel1: Campo = Campo('./assets/images/campo.jpg', 450, 250)
    urlMod: str = './assets/images/plataforma.png'
    urlOriginal: str = './assets/images/plataforma-original.png'
    urlRampa: str = './assets/images/rampa.png'
    urlRampa02: str = './assets/images/rampa02.png'
    boy: Personagem = Personagem(115, 450, 'fogo')
    plataformas: list[Plataforma] = [
        [
        Plataforma('./assets/images/plataforma01.png', 190, 405), Plataforma(urlOriginal, 815, 405), Plataforma(urlRampa, 776, 405)
        ], 

        [
        Plataforma('./assets/images/plataforma03.png', 227, 310), Plataforma(urlRampa02, 408, 310), Plataforma(urlRampa02, 437, 329),  Plataforma('./assets/images/plataforma02.png', 572, 347), Plataforma(urlRampa02, 710, 347)
        ]

        ]

    run(globals())