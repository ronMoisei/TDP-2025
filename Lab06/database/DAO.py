from numba.core.typing.builtins import Print

from Lab06.database.dbConnect import dbConnect as db
from Lab06.model.method    import OrderMethod
from Lab06.model.product   import Product
from Lab06.model.retailer  import Retailer
from Lab06.model.dailySales import DailySale

class DAO:

    @staticmethod
    def get_order_methods() -> list[OrderMethod]:
        cnx    = db.connect()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM go_methods")
        res = []
        for row in cursor:
            # Trasforma le chiavi in lowercase per farle combaciare con gli attributi
            normalized = { k.lower(): v for k, v in row.items() }
            res.append(OrderMethod(**normalized))
        cursor.close()
        cnx.close()
        return res


    @staticmethod
    def get_products() -> list[Product]:
        cnx = db.connect()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM go_products")
        res = []
        for row in cursor:
            row = {k.lower(): v for k, v in row.items()}
            res.append(Product(**row))
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def get_retailers() -> list[Retailer]:
        cnx    = db.connect()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM go_retailers")
        res = []
        for row in cursor:
            row = {k.lower(): v for k, v in row.items()}
            print(row.keys())
            print(row.items())
            res.append(Retailer(**row))
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def get_sales() -> list[DailySale]:
        cnx    = db.connect()
        cursor = cnx.cursor()   # default: tuple-cursor
        cursor.execute("""
            SELECT
              Retailer_code,
              Product_number,
              Order_method_code,
              Date,
              Quantity,
              Unit_price,
              Unit_sale_price
            FROM go_daily_sales
        """)
        res = []
        for row in cursor:
            # row è una tuple: (retailer_code, product_number, ..., unit_sale_price)
            # basta passare *row al costruttore
            # NB: convertiamo i Decimal in float
            rc, pn, omc, dt, qty, up, usp = row
            res.append(
                DailySale(
                    retailer_code      = rc,
                    product_number     = pn,
                    order_method_code  = omc,
                    date               = dt,
                    quantity           = qty,
                    unit_price         = float(up),
                    unit_sale_price    = float(usp),
                )
            )
        cursor.close()
        cnx.close()
        return res


if __name__ == "__main__":
    print("Order methods:")
    for m in DAO.get_order_methods():
        print(" ", m)
    print("\nProducts:")
    for p in DAO.get_products():
        print(" ", p)
    print("\nRetailers:")
    for r in DAO.get_retailers():
        print(" ", r)
    sales = DAO.get_sales()
    for s in sales:
        print(" ", s)
    print(f"\nTotal sales loaded: {len(sales)}")