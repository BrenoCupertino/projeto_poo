from typing import Optional
from tupy import *
from modules.personagem import *
from modules.porta import Porta
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

class Campo(Campo):
    def update(self):
        if porta_fogo._file=='./assets/images/firegate6.png' and porta_agua._file=='./assets/images/watergate6.png':
            toast("Fim de jogo",10000)
            boy.destroy() #Pra travar o jogo apos terminar
            girl.destroy()
class Elevador(Elevador):
    def update(self):
        if boy._campo._collides_with(botao_baixo) or girl._campo._collides_with(botao_baixo._campo):
            if self._y>135:
                self._y-=5
            self._pilha=1
        elif boy._campo._collides_with(botao_cima) or girl._campo._collides_with(botao_cima._campo):
            if self._y<230:
                self._y+=5
            self._pilha=2
        elif self._pilha==1:
            if self._y<230:
                self._y+=5
        elif self._pilha==2:
            if self._y>135:
                self._y-=5


class Botao(Botao):
    def update(self):
        if boy._campo._collides_with(self._campo) or girl._campo._collides_with(self._campo):
            self.file='./assets/images/imagem-vazia2.png'
        else:
            self.file='./assets/images/botao.png'

        
class Personagem(Personagem):

    def checaColisoes(self):

        if (self._y <= 340 and self._y >= 300)  and (self._x >= 540 and self._x <= 600):
            self._destroy()
            toast("Fim de jogo",5000)
        elif self._elemento == 'fogo':
            if (self._y <= 481 and self._y >= 430) and (self._x >= 565 and self._x <= 618):
                self._destroy()
                toast("Fim de jogo",5000)
        elif self._elemento == 'agua':
            if (self._y <= 481 and self._y >= 430) and (self._x >= 370 and self._x <= 420):
                self._destroy()
                toast("Fim de jogo",5000)

    def update(self):
        super().update()
        if self._campo._collides_with(elevador):
            self.y=(elevador._y)-40
            #self.tempo_caindo = 0
        for lista in plataformas:
            for item in lista:
                if self._campo._collides_with(item):
                    self.tempo_caindo = 0
       
        #Verificar se o personagem conseguiu diamantes
        for lista in diamantes:
            for item in lista:
                if self._campo._collides_with(item):
                    if self._elemento=='fogo' and item._cor=='vermelho':
                        self._qtd_diamantes+=1
                        lista.remove(item)
                        item.destroy()
                        
                    elif self._elemento=='agua' and item._cor=='azul':
                        self._qtd_diamantes+=1
                        lista.remove(item)
                        item.destroy()
                    
        self.checaColisoes()

class Porta(Porta):
    
    def update(self):
        if self._collides_with(boy._campo):
            if self._tipo=='fire':
                self._c1=True
        elif self._collides_with(girl._campo):
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
                if self._campo._collides_with(item):
                    self.tempo_caindo_cubo = 0
        if self._campo._collides_with(elevador):
            self.tempo_caindo_cubo = 0
        if self._campo._collides_with(boy._campo):
            self._x += (boy.velocidade_atual.x)
        if self._campo._collides_with(girl._campo):
            self._x += (girl.velocidade_atual.x)

if __name__ == '__main__':
    nivel1: Campo = Campo('./assets/images/campo-teste.png', 450, 250)
    urlOriginal: str = './assets/images/plataforma-original.png'
    urlRampa: str = './assets/images/rampa.png'
    urlRampa02: str = './assets/images/rampa02.png'
    porta_fogo: Porta = Porta("./assets/images/firegate0.png", 110, 92, 'fire')
    porta_agua: Porta = Porta("./assets/images/watergate0.png", 210, 92, 'water')
    boy: Personagem = Personagem(115, 439, 'fogo')
    girl: Personagem = Personagem(115, 363, 'agua')
    elevador: Elevador = Elevador("./assets/images/elevador.png",800, 230)
    botao_baixo: Botao = Botao("./assets/images/botao.png",730,219)
    botao_cima: Botao = Botao("./assets/images/botao.png",700,125)
    cubo: Cubo = Cubo('./assets/images/cubo.png',200,300)
    plataformas: list[list[Plataforma]] = [
        [
        Plataforma('./assets/images/plataforma1.1.png',211,481), Plataforma('./assets/images/plataforma1.2.png',495,481), Plataforma('./assets/images/plataforma1.3.png',733,481),Plataforma('./assets/images/plataforma01.png', 190, 400), Plataforma(urlOriginal, 815, 410), Plataforma(urlRampa, 776, 410)
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
