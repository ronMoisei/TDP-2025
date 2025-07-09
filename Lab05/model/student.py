

class Student:
    def __init__(self, matricola: int, cognome: str, nome: str, CDS: str):
        self.matricola = matricola
        self.cognome = cognome
        self.nome = nome
        self.CDS = CDS


    def __str__(self):
        return f"Studente: {self.matricola} - {self.cognome}, {self.nome}, presso corso: {self.CDS}"

    def __hash__(self):
        return hash(self.matricola)

    def __eq__(self, other):
        return self.matricola == other.matricola

    def __lt__(self, other):
        return self.matricola < other.matricola

