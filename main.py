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


class Plataforma(Image):
    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None) -> None:
        super().__init__(file, x, y)
    
    def set_x(self, x: int) -> None:
        self._x = x

    def set_y(self, y: int) -> None:
        self._y = y

class Obstaculo(Image):
    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None, tipo: str | None = None) -> None:
        super().__init__(file, x, y)
        self.tipo=tipo

#Plataforma(urlOriginal, 804, 230), Plataforma(urlOriginal, 815, 230)

class Porta(BaseImage):
    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None) -> None:
        super().__init__(file, x, y)

class Elevador(BaseImage):
    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None) -> None:
        super().__init__(file, x, y)
if __name__ == '__main__':
    nivel1: Campo = Campo('./assets/images/campo-teste.png', 450, 250)
    urlOriginal: str = './assets/images/plataforma-original.png'
    urlRampa: str = './assets/images/rampa.png'
    urlRampa02: str = './assets/images/rampa02.png'
    boy: Personagem = Personagem(115, 450, 'fogo')
    girl: Personagem = Personagem(115, 370, 'agua')
    porta0: Porta = Porta("./assets/images/firegate0.png", 110, 92)
    porta1: Porta = Porta("./assets/images/watergate0.png", 210, 92)
    elevador: Elevador = Elevador("./assets/images/elevador.png",800, 230)
    
    plataformas: list[list[Plataforma]] = [
        [
        Plataforma('./assets/images/plataforma01.png', 190, 410), Plataforma(urlOriginal, 815, 410), Plataforma(urlRampa, 776, 410)
        ], 

        [
        Plataforma('./assets/images/plataforma03.png', 227, 325), Plataforma(urlRampa02, 408, 325), Plataforma(urlRampa02, 435, 340),  Plataforma('./assets/images/plataforma15.png', 473, 360), Plataforma('./assets/images/plataforma15.png',509, 360), Plataforma('./assets/images/plataforma15.png',632, 360), Plataforma('./assets/images/plataforma15.png',665, 360), Plataforma('./assets/images/rampa20.png', 704, 362), Plataforma(urlOriginal, 85, 310), Plataforma(urlRampa02, 123, 310)
        ],

        [
        Plataforma(urlRampa, 180, 230), Plataforma(urlOriginal, 218, 230), Plataforma(urlRampa, 237, 216), Plataforma('./assets/images/plataforma01.png', 379, 216), Plataforma(urlRampa02, 524, 216), Plataforma(urlOriginal, 560, 230), Plataforma('./assets/images/plataforma04.png', 670, 230) 
        ],

        [
            Plataforma('./assets/images/plataforma01.png', 300, 135), Plataforma(urlRampa, 430, 120), Plataforma('./assets/images/plataforma04.png', 534, 105), Plataforma(urlRampa02, 639, 105), Plataforma(urlRampa02, 665, 120), Plataforma(urlOriginal, 700, 135), Plataforma(urlOriginal, 737, 135), Plataforma(urlOriginal, 150, 135), Plataforma(urlOriginal, 115, 135), Plataforma(urlOriginal, 87, 135)
        ]
    ]
    poison: Obstaculo = Obstaculo('./assets/images/poison0.png', 570, 362)
    fire: Obstaculo = Obstaculo('./assets/images/fire0.png', 397, 475)
    water: Obstaculo = Obstaculo('./assets/images/water0.png', 592, 475)
    run(globals())