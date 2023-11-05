from tupy import *

class Elevador(BaseImage):
    def __init__(self,x,y):
        self._x=x
        self._y=y
        self._file = 'elevador.png'

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
class Botao(BaseImage):
    def __init__(self,x,y):
        self._x=x
        self._y=y
        self._elevador=Elevador(450,300)
        self._c1=False
        self._t=0
        self._file='botao.png'
        
    def uptade(self):
        if self._c1 is True:
            while self._elevador.x<=self._elevador.x+15:
                self._elevador.y-=5
                self._t+=1
        else:
            if self._t>0:
                while self._t>0:
                    self._t-=1
                    self._elevador.y+=5