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
    urlOriginal: str = './assets/images/plataforma-original.png'
    urlRampa: str = './assets/images/rampa.png'
    urlRampa02: str = './assets/images/rampa02.png'
    boy: Personagem = Personagem(115, 450, 'fogo')
    plataformas: list[list[Plataforma]] = [
        [
        Plataforma('./assets/images/plataforma01.png', 190, 410), Plataforma(urlOriginal, 815, 410), Plataforma(urlRampa, 776, 410)
        ], 

        [
        Plataforma('./assets/images/plataforma03.png', 227, 325), Plataforma(urlRampa02, 408, 325), Plataforma(urlRampa02, 435, 340),  Plataforma('./assets/images/plataforma02.png', 569, 354), Plataforma(urlRampa02, 706, 354), Plataforma(urlOriginal, 85, 310), Plataforma(urlRampa02, 123, 310)
        ],

        [
        Plataforma(urlRampa, 180, 230), Plataforma(urlOriginal, 218, 230), Plataforma(urlRampa, 237, 216), Plataforma('./assets/images/plataforma01.png', 379, 216), Plataforma(urlRampa02, 524, 216), Plataforma('./assets/images/plataforma02.png', 657, 230), Plataforma(urlOriginal, 804, 230), Plataforma(urlOriginal, 815, 230)
        ],

        [
            Plataforma('./assets/images/plataforma01.png', 300, 135), Plataforma(urlRampa, 430, 120), Plataforma('./assets/images/plataforma04.png', 534, 105), Plataforma(urlRampa02, 639, 105), Plataforma(urlRampa02, 665, 120), Plataforma(urlOriginal, 700, 135), Plataforma(urlOriginal, 748, 135)
        ]

        ]

    run(globals())