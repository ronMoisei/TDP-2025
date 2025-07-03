import mysql

from indovinaCorsi.database.dbConnect import dbConnect
from indovinaCorsi.model.Studente import Studente


class DAO():

    @staticmethod
    def getStudenti():

        cnx = dbConnect.connect()

        cursor = cnx.cursor(dictionary=True)

        query = cursor.execute("SELECT * FROM studente")
        cursor.execute(query)

        res = []

        for row in cursor:
            res.append(Studente(**row))

        cursor.close()
        cnx.close()
        return res


if __name__ == '__main__':
    prova = DAO.getStudenti()
    for studente in prova:

        print(studente)
