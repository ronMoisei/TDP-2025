import random
from math import log2





class Model(object):
    def __init__(self, NMax = 2):
        self._NMax = NMax
        self._TMax = int(log2(6**self._NMax))
        self._T = self._TMax
        self._palette = ["R", "G", "B", "Y", "C", "M"]
        self._segreto = None


    def play(self, tentativo):
        self._T -= 1
        print(self._segreto)
        res = self.evaluate(tentativo)
        if self._T < 0:
            return 0 #hai perso
        if res == self._segreto:
            return 1
        return res

    def genera_colore(self, value):
        i = 0
        colore = ""
        while i < value:
            j = random.randint(0, len(self._palette)-1)
            colore+=self._palette[j]
            i += 1
        return colore

    @property
    def NMax(self):
        return self._NMax
    @property
    def TMax(self):
        return self._TMax
    @property
    def segreto(self):
        return self._segreto
    @property
    def palette(self):
        return self._palette

    @NMax.setter
    def NMax(self, value):

        self._NMax = value
    @TMax.setter
    def TMax(self, value):
        self._TMax = value

    def reset(self):
        print(self._segreto)
        self._segreto = self.genera_colore(self._NMax)
        self._T = self._TMax

    def evaluate(self, tent, i = None, B = 0):
        if i is None:
            i = len(tent) - 1
            self._origin_len = len(tent)

        if i < 0:
            #base-case: lista tutta "scansionata"
            return (B, self._origin_len - B)
        if self._segreto[i] == tent[i]:
            B += 1

        return self.evaluate(tent, i - 1, B)

if __name__ == '__main__':

    m = Model()
    print(m._T)
    print(m.play("BRGC"))
    print(m._segreto)
    print(m._T)