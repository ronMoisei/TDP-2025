from Lab05.model.corso import Corso
from Libretto.scuola import Student
from Lab05.database.dbConnect import dbConnect as db
from Lab05.model.student import Student
from Lab05.model.corso import Corso

class DAO:

    @staticmethod
    def getStudenti():

        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)

        query = cursor.execute("SELECT * FROM studente")
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Student(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCorso(codins):
        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)

        query =("""SELECT c.* 
                    FROM corso as c
                    WHERE c.codins = %s""")
        cursor.execute(query, (codins, ))

        res = []
        for row in cursor:
            res.append(Corso(**row))

        cursor.close()
        cnx.close()
        print(res)
        return res
    @staticmethod
    def getCorsi():
        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)

        query = cursor.execute("SELECT * FROM corso")
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Corso(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getStudentByCorso(codins):
        cnx = db.connect()
        cursor = cnx.cursor(dictionary = True)

        query = """SELECT s.*
                   FROM studente AS s
                   JOIN iscrizione AS i
                     ON s.matricola = i.matricola
                   WHERE i.codins = %s;"""
        cursor.execute(query, (codins, ))

        res = []
        for row in cursor:
            res.append(Student(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCorsobyPd(periodo):
        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)

        query = ("""SELECT c.* 
                            FROM corso as c
                            WHERE c.pd = %s""")
        cursor.execute(query, (periodo,))

        res = []
        for row in cursor:
            res.append(Corso(**row))

        cursor.close()
        cnx.close()

        return res


if __name__ == '__main__':
    prova = DAO.getCorsobyPd(2)
    for corso in prova:
        print(corso)
