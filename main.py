from tupy import *
from modules.personagem import Personagem
from modules.botao import Botao
from assets import img

class botao1(Botao):
    def __init__(self,x,y,boy,girl):
        super().__init__(x,y)
        self._boy=boy
        self._girl=girl
        
    def update(self):
        if self._collides_with(self._boy):
            self._c1=True
        elif self._collides_with(self._girl):
            self._c1=True 
        super().update() 

class fireboy(Personagem):
    def __init__(self,x,y,fogo):
        self._file = './assets/img/boyfrente0.png'
        self._x = x
        self._y = y


class watergirl(Personagem):
    def __init__(self,x,y,agua):
        self._file = './assets/img/girlfrente0.png'
        self._x = x
        self._y = y

class plataforma(BaseImage):
    def __init__(self,x,y):
        self._file = './assets/img/plataforma.png'
        self._x = x
        self._y = y


if __name__ == '__main__':

    boy = Personagem(100,500, "fogo")
    girl = Personagem(200,500, "agua")
    l1 = [boy, girl]
    ptf = plataforma(300,300)
    bt = botao1(250,200,boy,girl)

    run(globals())