from tupy import *

class Porta(BaseImage):
    def __init__(self, file: str | None = None, x: int | None = None, y: int | None = None, tipo:str|None=None) -> None:
        super().__init__(file, x, y)
        self._tipo=tipo
        self._c1=False
        self._contador_porta = 0
        self._posicao_porta = 0
    def update(self) -> None:
        if self._c1 is True:
            if self._contador_porta<30:
                self._contador_porta+=1
                if (self._contador_porta)%5==0:
                    if self._posicao_porta!=6:
                        self._posicao_porta+=1
        if self._c1 is False:
            if self._contador_porta>0:
                if self._contador_porta>0:
                    self._contador_porta-=1
                    if (self._contador_porta)%5==0:
                        if self._posicao_porta!=0:
                            self._posicao_porta-=1
        self._file=f'./assets/images/{self._tipo}gate{self._posicao_porta}.png'