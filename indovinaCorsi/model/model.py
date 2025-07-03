from indovinaCorsi.database.DAO import DAO

class Model:
    def __init__(self):
        pass

    def getStudenti(self):
        return DAO.getStudenti()

