from tupy import *
from enum import Enum
from typing import Any
from modules.objetos import *

class Vetor:

    def __init__(self, x: int, y: int | float) -> None:
        self.x = x
        self.y = y

    def __eq__(self, outro: Any) -> bool:

        return isinstance(outro, Vetor) and \
            self.x == outro.x and \
            self.y == outro.y

vetor_Zero = Vetor(0, 0)
class Contador:

    def __init__(self, maximo: int) -> None:
        self._maximo: int = maximo
        self._contador: int = 0

    def incrementa(self) -> None:

        self._contador += 1
        if self._contador == self._maximo:
            self._contador = 0
    
    def esta_zerado(self) -> bool:
        return self._contador == 0

class Direcao(Enum):
    CIMA = "pulo"
    BAIXO = "queda"
    ESQUERDA = "esquerda"
    DIREITA = "direita"
    NULO = "frente"
        
class Personagem(BaseImage):
    VELOCIDADE = 10
    GRAVIDADE = 5

    def __init__(self, x: int, y: int, elemento: str) -> None:
        
        self._elemento = elemento
        if self._elemento == "fire":
            self._file = './assets/images/boyfrente0.png'
            self._tipo = 'boy'
            self._l1 = ["Up","Left","Right"]
        elif self._elemento == "water":
            self._file = './assets/imagens/girlfrente0.png'
            self._tipo = 'girl'
            self._l1 = ["w", "a", "d"]
        self._campo = Vazio('./assets/images/imagem-vazia0.png', self._x, self._y)
        self._qtd_diamantes = 0
        self._x = x
        self._y = y
        self._direcao: Direcao = Direcao.NULO
        self._contador = Contador(7)
        self._quadro: int = 0
        self.tempo_caindo = 0
        self.velx = 0
        self.vely = 0
        self.velocidade_atual = Vetor(self.velx, self.vely)
        self._contador_de_pulos = 0

    @property
    def x(self) -> int | float:
        return self._x
    
    @property
    def y(self) -> int | float:
        return self._y
    
    def obtem_velocidade(self) -> None:
        
        self.velx = 0
        self.vely = 0
        if keyboard.is_key_down(self._l1[0]):
            if self._contador_de_pulos < 5:
                self.vely -= Personagem.VELOCIDADE
                self._contador_de_pulos += 1
        if keyboard.is_key_down(self._l1[1]):
            self.velx -= Personagem.VELOCIDADE
        if keyboard.is_key_down(self._l1[2]):
            self.velx += Personagem.VELOCIDADE
        self.velocidade_atual.x = self.velx
        self.velocidade_atual.y = self.vely
    
    def obtem_direcao(self, vel: Vetor) -> None:
        if vel.y < 0:
            self._direcao = Direcao.CIMA
        elif vel.x > 0:
            self._direcao = Direcao.DIREITA
        elif vel.x < 0:
            self._direcao = Direcao.ESQUERDA
        elif self.tempo_caindo > 0:
            self._direcao = Direcao.BAIXO
        else:
            self._direcao = Direcao.NULO
    
    def gravidade(self) -> None:

        self.atualiza_posicao(Vetor(0, min(10, (self.tempo_caindo/30) * self.GRAVIDADE)))
        self.tempo_caindo += 2
                        
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
            self._y += int(velocidade.y)
        self._campo._x = self._x
        self._campo._y = self._y + 5
    
    def colisao_obstaculo(self, obstaculo: Obstaculo) -> None:

        if self._campo._collides_with(obstaculo):
            if obstaculo._tipo == "poison" and self._campo._y + self._campo._height*0.5 > obstaculo._y - obstaculo._height*0.5:
                    toast("Fim de jogo",10000)
                    self._destroy()
            elif self._elemento == 'fire' and obstaculo._tipo == "water":
                toast("Fim de jogo",10000)
                self._destroy()
            elif self._elemento == 'water' and obstaculo._tipo == "fire":
                toast("Fim de jogo",10000)
                self._destroy()

    def colisao_plataformas(self, plataformas: list[list[Plataforma]]) -> None:

        for lista in plataformas:
            for item in lista:
                if self._campo._collides_with(item) and self._y < item._y:
                    self._y = int(item._y - self._campo._height*0.75)
                    self._campo._y = self._y
                    self.tempo_caindo = 0
                    self._contador_de_pulos = 0
                elif self._campo._collides_with(item) and self._y > item._y:
                    self.atualiza_posicao(Vetor(0, -self.vely))
    
    def colisao_elevador(self, elevador: Elevador) -> None:

        if self._campo._collides_with(elevador) and self._y < elevador._y:
            self._y = int(elevador._y - self._campo._height*0.75)
            self._campo._y = self._y
            self.tempo_caindo = 0
            self._contador_de_pulos = 0
        elif self._campo._collides_with(elevador) and self._y > elevador._y:
            self.atualiza_posicao(Vetor(0, -self.vely))
    
    def colisao_diamantes(self, diamantes: list[list[Diamante]]) -> None:

        #Verificar se o personagem conseguiu diamantes
        for lista in diamantes:
            for item in lista:
                if self._campo._collides_with(item):
                    if self._elemento=='fire' and item._cor=='vermelho':
                        self._qtd_diamantes += 1
                        lista.remove(item)
                        item.destroy()
                        
                    elif self._elemento=='water' and item._cor=='azul':
                        self._qtd_diamantes+=1
                        lista.remove(item)
                        item.destroy()
    
    def colisao_cubo(self, cubo: Cubo) -> None:

        if self._campo._collides_with(cubo._campo) and self._campo._y < cubo._campo.y - cubo._campo._height:
            self._y = cubo._campo.y*0.85
            self._campo._y = self._y
            self.tempo_caindo = 0
            self._contador_de_pulos = 0
        if self._campo._collides_with(cubo._campo) and cubo.x > 820:
            self.atualiza_posicao(Vetor(-self.velx, 0))
        elif self._campo._collides_with(cubo._campo) and cubo.x < 85:
            self.atualiza_posicao(Vetor(-self.velx, 0))

            
    def update(self) -> None:
        self._contador.incrementa()
        self.obtem_velocidade()
        self.obtem_direcao(self.velocidade_atual)
        self.atualiza_posicao(self.velocidade_atual)
        self.atualiza_imagem()
        self.gravidade()

        if self.velocidade_atual == vetor_Zero:
            self._quadro = 0
        elif self._contador.esta_zerado():
            self._quadro = 1 - self._quadro