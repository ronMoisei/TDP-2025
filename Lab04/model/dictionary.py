import copy

from charset_normalizer import md


class Dictionary:
    def __init__(self, language: str, path: str):
        self._language = language
        self._dict = set()
        self.load_dictionary(path)

    @property
    def dict(self):
        return self._dict.copy()


    def load_dictionary(self, path: str):
        """Carica le parole dal file 'path' per la lingua specificata:
        - Se la lingua non esiste ancora in self._dic, la inizializza a set().
        - Aggiunge tutte le parole non vuote al set corrispondente."""
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                value = line.strip()
                self._dict.add(value)





    def printAll(self):
        for lang, words in self._dict.items():
            print(f"===={lang}: {len(words)} parole)")
            for w in sorted(words):
                print(f"\t{w}")

    def __str__(self):
        return f"dizionario di: {self._language}\n---\n{self._dict}"

    def __repr__(self):
        return f"{self._language} dictionary"

    def copy(self):
        return copy.copy(self)

if __name__ == "__main__":
    d = Dictionary("english","C:/Users/ronal/PycharmProjects/TDP-2025/TDP-2025/Lab04/dictionaries/english.txt")
    print(d)