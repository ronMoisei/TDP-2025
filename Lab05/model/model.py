from Lab05.database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getAllCorsi(self):
        return DAO.getCorsi()

    def getStudenti(self):
        return DAO.getStudenti()

    def getCorso(self, codins):
        return DAO.getCorso(codins)

    def getStudentByCorso(self, corso):
        return DAO.getStudentByCorso(corso)

    def getCorsobyPD(self, periodo):
        return DAO.getCorsobyPd(periodo)


if __name__ == '__main__':
    pass