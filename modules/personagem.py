from tupy import *
from enum import Enum

class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, outro):
        return isinstance(outro, Vetor) and \
            self.x == outro.x and \
            self.y == outro.y

Vetor.ZERO = Vetor(0, 0)

class Teste:
    pass

class Contador:
    def __init__(self, maximo):
        self._maximo = maximo
        self._contador = 0

    def incrementa(self):
        self._contador += 1
        if self._contador == self._maximo:
            self._contador = 0
    
    def esta_zerado(self):
        return self._contador == 0

class Direcao(Enum):
    CIMA = "pulo"
    ESQUERDA = "esquerda"
    DIREITA = "direita"
    NULO= "frente"


class Personagem(BaseImage):
    VELOCIDADE = 10

    def __init__(self, x, y, elemento ):
        self._elemento = elemento
        if self._elemento == "fogo":
            self._file = './assets/images/boyfrente0.png'
            self._tipo = 'boy'
            self._l1 = ["Up","Left","Right"]
        elif self._elemento == "agua":
            self._file = './assets/imagens/girlfrente0.png'
            self._tipo = 'girl'
            self._l1 = ["w", "a", "d"]
        self._x = x
        self._y = y
        self._direcao="frente"
        self._contador=Contador(7)
        self._quadro: int=0

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    def obtem_velocidade(self) -> Vetor:
        velx = 0
        vely = 0
        if keyboard.is_key_down(self._l1[0]):
            vely -= Personagem.VELOCIDADE
        if keyboard.is_key_down(self._l1[1]):
            velx -= Personagem.VELOCIDADE
        if keyboard.is_key_down(self._l1[2]):
            velx += Personagem.VELOCIDADE
        return Vetor(velx,vely)
    
    def obtem_direcao(self, vel: Vetor) -> Direcao:
        if vel.y < 0:
            return Direcao.CIMA
        elif vel.x < 0:
            return Direcao.ESQUERDA
        elif vel.x > 0:
            return Direcao.DIREITA
        else:
            return Direcao.NULO

    def update(self):
        self._contador.incrementa()
        velocidade = self.obtem_velocidade()
        self._direcao = self.obtem_direcao(velocidade)
        self.atualiza_posicao(velocidade)
        self.atualiza_imagem()

        if velocidade == Vetor.ZERO:
            self._quadro = 0
        elif self._contador.esta_zerado():
            self._quadro = 1 - self._quadro
            self._contador_de_updates = 0

    def atualiza_imagem(self):
        nome = self._direcao.value
        self._file = f'./assets/images/{self._tipo}{nome}{self._quadro}.png'

    def atualiza_posicao(self, velocidade):
        self._x += velocidade.x
        self._y += velocidade.y