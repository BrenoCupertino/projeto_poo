from typing import Optional
from tupy import *
from modules.personagem import Personagem
from modules.porta import Porta
from modules.botao import Botao
from modules.campo import Campo
from modules.objetos import *

"""class botao1(Botao):
    def __init__(self,x,y,boy,girl):
        super().__init__(x,y)
        self._boy=boy
        self._girl=girl
        
    def update(self):
        if self._collides_with(self._boy):
            self._c1=True
        elif self._collides_with(self._girl):
            self._c1=True 
        super().update()"""

class Elevador(BaseImage):
    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None) -> None:
        super().__init__(file, x, y)
        
class Personagem(Personagem):

    def update(self):
        super().update()
        for lista in plataformas:
            for item in lista:
                if self._collides_with(item):
                    self.tempo_caindo = 0
        if self._collides_with(elevador):
            self.tempo_caindo = 0
        #Verificar se o personagem conseguiu diamantes
        for lista in diamantes:
            for item in lista:
                if self._collides_with(item):
                    if self._elemento=='fogo' and item._cor=='vermelho':
                        self._qtd_diamantes+=1
                        lista.remove(item)
                        item.destroy()
                        
                    elif self._elemento=='agua' and item._cor=='azul':
                        self._qtd_diamantes+=1
                        lista.remove(item)
                        item.destroy()

class Porta(Porta):
    
    def update(self):
        if self._collides_with(boy):
            if self._tipo=='fire':
                self._c1=True
        elif self._collides_with(girl):
            if self._tipo=='water':
                self._c1=True
        else:
            self._c1=False
        super().update()   
class Cubo(Cubo):

    def update(self) -> None:
        super().update()
        for lista in plataformas:
            for item in lista:
                if self._collides_with(item):
                    self.tempo_caindo_cubo = 0
        if self._collides_with(elevador):
            self.tempo_caindo_cubo = 0
        if self._collides_with(boy):
            self._x += (boy.velocidade_atual.x)
        if self._collides_with(girl):
            self._x += (girl.velocidade_atual.x)

if __name__ == '__main__':
    nivel1: Campo = Campo('./assets/images/campo-teste.png', 450, 250)
    urlOriginal: str = './assets/images/plataforma-original.png'
    urlRampa: str = './assets/images/rampa.png'
    urlRampa02: str = './assets/images/rampa02.png'
    porta0: Porta = Porta("./assets/images/firegate0.png", 110, 92)
    porta1: Porta = Porta("./assets/images/watergate0.png", 210, 92)
    boy: Personagem = Personagem(115, 439, 'fogo', porta1)
    girl: Personagem = Personagem(115, 363, 'agua', porta0)
    elevador: Elevador = Elevador("./assets/images/elevador.png",800, 230)
    botao0: Botao = Botao("./assets/images/botao.png",730,219)
    botao2: Botao = Botao("./assets/images/botao.png",700,125)
    cubo: Cubo = Cubo('./assets/images/cubo.png',200,300)
    plataformas: list[list[Plataforma]] = [
        [
        Plataforma('./assets/images/plataforma01.png', 190, 400), Plataforma(urlOriginal, 815, 410), Plataforma(urlRampa, 776, 410)
        ], 

        [
        Plataforma('./assets/images/plataforma03.png', 227, 325), Plataforma(urlRampa02, 408, 325), Plataforma(urlRampa02, 435, 340),  Plataforma('./assets/images/plataforma15.png', 473, 360), Plataforma('./assets/images/plataforma15.png',509, 360), Plataforma('./assets/images/plataforma15.png',632, 360), Plataforma('./assets/images/plataforma15.png',665, 360), Plataforma('./assets/images/rampa20.png', 704, 362), Plataforma(urlOriginal, 170, 230),
        ],

        [
        Plataforma(urlRampa, 132, 230), Plataforma(urlOriginal, 218, 230), Plataforma(urlRampa, 237, 216), Plataforma('./assets/images/plataforma01.png', 379, 216), Plataforma(urlRampa02, 524, 216), Plataforma(urlOriginal, 560, 230), Plataforma('./assets/images/plataforma04.png', 670, 230) 
        ],

        [
            Plataforma('./assets/images/plataforma01.png', 300, 135), Plataforma(urlRampa, 430, 120), Plataforma('./assets/images/plataforma04.png', 534, 105), Plataforma(urlRampa02, 639, 105), Plataforma(urlRampa02, 665, 120), Plataforma(urlOriginal, 700, 135), Plataforma(urlOriginal, 737, 135), Plataforma(urlOriginal, 150, 135), Plataforma(urlOriginal, 115, 135), Plataforma(urlOriginal, 87, 135)
        ],

        [
            Plataforma('./assets/images/plataforma01.png', 190, 475), Plataforma('./assets/images/plataforma01.png', 225, 475), Plataforma(urlOriginal, 470, 475), Plataforma(urlOriginal, 525, 475), Plataforma('./assets/images/plataforma01.png', 770, 475)
        ]
    ]
    diamantes: list[list[Diamante]] = [[Diamante('./assets/images/diamante-azul.png',592,450,"azul"),Diamante('./assets/images/diamante-azul.png',400,185,"azul"),Diamante('./assets/images/diamante-azul.png',509,330,"azul"),Diamante('./assets/images/diamante-azul.png',534,70,"azul")],
        [Diamante('./assets/images/diamante-vermelho.png',397,450,"vermelho"), Diamante('./assets/images/diamante-vermelho.png',210,200,"vermelho"), Diamante('./assets/images/diamante-vermelho.png',815,385,"vermelho"), Diamante('./assets/images/diamante-vermelho.png',650,200,"vermelho")]                               
        ]
    poison: Obstaculo = Obstaculo('./assets/images/poison0.png', 570, 362)
    fire: Obstaculo = Obstaculo('./assets/images/fire0.png', 397, 481)
    water: Obstaculo = Obstaculo('./assets/images/water0.png', 592, 481)
    for item in plataformas[4]:
        item._hide()

    run(globals())
