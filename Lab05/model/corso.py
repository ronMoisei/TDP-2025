
class Corso:
    def __init__(self, codins: str, crediti: int, nome: str, pd: int):
        self.codins = codins
        self.crediti = crediti
        self.nome = nome
        self.pd = pd


    def __str__(self):
        return f'Corso: {self.codins} - {self.nome} del {self.pd} periodo, vale: {self.crediti} CFU'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.codins == other.codins

    def __hash__(self):
        return hash(self.codins)
