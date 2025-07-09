import pathlib
import mysql.connector



class dbConnect:
    def __init__(self):
        raise RuntimeError("dbConnect should not be instantiated")

    _myPool = None

    @classmethod
    def connect(cls):
        if cls._myPool is None:
            try:
                cls._myPool = mysql.connector.pooling.MySQLConnectionPool(
                    pool_size=3,
                    pool_name="myPool",
                    option_files=f"{pathlib.Path(__file__).resolve().parent}/connection.cfg"
                )
            except mysql.connector.Error as err:
                print("Something is wrong with MySQL connection")
                print(err)
                return None
            return cls._myPool.get_connection()
        else:
            return cls._myPool.get_connection()
