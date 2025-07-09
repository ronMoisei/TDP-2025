from dataclasses import dataclass

@dataclass
class Connessione:
    id_connessione : int
    id_linea: int
    id_stazP: int
    id_stazA: int

    def __hash__(self):
        return hash(self.id_connessione)

    def __str__(self):
        return f"""conn n:{self.id_connessione}. {self.id_stazP}-{self.id_stazA}. linea: {self.id_linea}"""