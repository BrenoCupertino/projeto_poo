from tupy import *
from enum import Enum
from modules.objetos import Vazio

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

class Porta(BaseImage):
    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None) -> None:
        super().__init__(file, x, y)
        
class Personagem(Image):
    VELOCIDADE = 10
    GRAVIDADE = 5

    def __init__(self, x: int | None = None, y: int | None = None, elemento: str | None = None) -> None:
        self._elemento = elemento
        if self._elemento == "fogo":
            self._file = './assets/images/boyfrente0.png'
            self._tipo = 'boy'
            self._l1 = ["Up","Left","Right"]
        elif self._elemento == "agua":
            self._file = './assets/imagens/girlfrente0.png'
            self._tipo = 'girl'
            self._l1 = ["w", "a", "d"]
        self._campo=Vazio('./assets/images/imagem-vazia0.png',self._x,self._y)
        self._qtd_diamantes=0
        self.x = x
        self.y = y
        self._direcao="frente"
        self._contador=Contador(7)
        self._quadro: int=0
        self.velocidade_atual = Vetor(0,0)
        self.tempo_caindo = 0

    
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
    
    def gravidade(self) -> None:

        self.atualiza_posicao(Vetor(0, min(10, (self.tempo_caindo/30) * self.GRAVIDADE)))
        self.tempo_caindo += 2
    

    def update(self) -> None:
        self._contador.incrementa()
        self.velocidade_atual = self.obtem_velocidade()
        self._direcao = self.obtem_direcao(self.velocidade_atual)
        self.atualiza_posicao(self.velocidade_atual)
        self.atualiza_imagem()
        self.gravidade()

        if self.velocidade_atual == Vetor.ZERO:
            self._quadro = 0
        elif self._contador.esta_zerado():
            self._quadro = 1 - self._quadro
            self._contador_de_updates = 0
       

                        
    def atualiza_imagem(self) -> None:
        nome = self._direcao.value
        self._file = f'./assets/images/{self._tipo}{nome}{self._quadro}.png'

    def atualiza_posicao(self, velocidade: Vetor) -> None:
        if self._x > 820:
            self._x = 820
        elif self._x < 85:
            self._x = 85
        else:
            self._x += velocidade.x
        if self._y < 40:
            self._y = 40
        elif self._y > 520:
            self._y = 520
        else:
            self._y += velocidade.y
        self._campo._x=self._x
        self._campo._y=self._y