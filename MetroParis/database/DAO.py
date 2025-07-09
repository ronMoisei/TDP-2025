

from MetroParis.database.dbConnect import dbConnect as db
from MetroParis.model.connessione import Connessione
from MetroParis.model.fermata import Fermata

class DAO:

    @staticmethod
    def get_Fermate():
        conn = db.connect()

        res = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM fermata"
        cursor.execute(query)

        for row in cursor:
            res.append(Fermata(**row))

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def has_Connessione(partenza, arrivo):
        conn = db.connect()

        res = []

        cursor = conn.cursor(dictionary=True)
        query = """
        SELECT *
        FROM connessione c
        WHERE c.id_stazP = %s and c.id_stazA = %s
        """
        cursor.execute(query, (partenza.id_fermata, arrivo.id_fermata))


        for row in cursor:
            res.append(row)

        cursor.close()
        conn.close()
        return len(res) > 0

    @staticmethod
    def get_Connessioni():
        conn = db.connect()

        res = []

        cursor = conn.cursor(dictionary=True)
        query = """
        SELECT *
        FROM connessione c
        """
        cursor.execute(query)

        for row in cursor:
            res.append(Connessione(**row))


        cursor.close()
        conn.close()
        return res

if __name__ == "__main__":

    fermate = DAO.get_Fermate()
    print(fermate[10])
    connessioni = DAO.get_Connessioni()
    for connessione in connessioni:
        print(connessione)

