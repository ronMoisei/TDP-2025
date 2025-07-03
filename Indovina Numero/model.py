import random

class Model(object):
    def __init__(self):
        self._NMax = 100
        self._TMax = 6
        self._T = self._TMax
        self._segreto = None

    def reset(self):
        # Questo metodo resetta il gioco in qualsiasi momento
        self._segreto = random.randint(0, self._NMax)
        self._T = self._TMax
        print(self._segreto)

    def play(self, guess):
        """
        Funzione che esegue uno step del gioco
        :param guess: int
        :return: 0 se vinto,
        -1 se segreto è più piccolo,
        1 se segreto è più grandde,
        2 se ho finito le vite
        """
        # da fuori ci arriva un tentativo, confrontiamo
        # il tentatvo con il segreto

        self._T -= 1

        if guess == self._segreto:
            return 0 # ho vinto!!

        if self._T == 0:
            return 2 # ho perso definitivamente

        if guess > self._segreto:
            return -1 # il segreto è più piccolo

        return 1 #il segreto è più grande

    @property
    def NMax(self):
        return self._NMax

    @NMax.setter
    def NMax(self, value):
        self._NMax = value

    @property
    def TMax(self):
        return self._TMax

    @NMax.setter
    def TMax(self, value):
        self._TMax = value

    @property
    def T(self):
        return self._T

    @property
    def segreto(self):
        return self._segreto

if __name__ == "__main__":
    m = Model()
    m.reset()
    print(m.play(80))
    print(m.play(10))