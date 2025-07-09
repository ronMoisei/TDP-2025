import time
import copy

import Lab04.model.dictionary as d
from Lab04.model.dictionary import Dictionary


class Model():
    def __init__(self):
        self.dictionaries = {
            "english": Dictionary("english",
                                  "C:/Users/ronal/PycharmProjects/TDP-2025/TDP-2025/Lab04/dictionaries/english.txt"),
            "italian": Dictionary("italian",
                                  "C:/Users/ronal/PycharmProjects/TDP-2025/TDP-2025/Lab04/dictionaries/italian.txt") ,
            "spanish": Dictionary("spanish",
                                  "C:/Users/ronal/PycharmProjects/TDP-2025/TDP-2025/Lab04/dictionaries/spanish.txt"),
        }

    def add_dictionary(self, dictionary):
            self.dictionaries.append(dictionary)


    def languageList(self):
        languages = []
        for dictionary in self.dictionaries:
            languages.append(dictionary)
        return languages

    def get_dictionary(self, language):
        dictionary = self.dictionaries[language]
        return dictionary


    def checkLanguage(self, sentence, language):
        dic = set()
        if language in self.dictionaries:
            dic = self.dictionaries[language].dict
        sbagliate = []
        words = sentence.split()
        for word in words:
            if word not in dic:
                sbagliate.append(word)

        return sbagliate

if __name__ == '__main__':
    m = Model()
    print(m.dictionaries)

    i = "Helo hou are yu"
    s = m.checkLanguage(i.lower(), "english")

    print(s)

    for i in m.dictionaries:
        print(i)