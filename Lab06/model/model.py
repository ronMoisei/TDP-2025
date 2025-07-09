# Lab06/model/model.py

from Lab06.database.DAO import DAO
from Lab06.model.method import OrderMethod
from Lab06.model.product import Product
from Lab06.model.retailer import Retailer
from Lab06.model.dailySales import DailySale

class Model:
    """
    Fa da intermediario tra il DAO (accesso al DB) e
    il controller/view: carica e fornisce i dati in memoria.
    """
    def __init__(self):
        self.reload_all()

    def reload_all(self):
        """Ricarica da database tutte le collezioni."""
        self._order_methods = DAO.get_order_methods()
        self._products      = DAO.get_products()
        self._retailers     = DAO.get_retailers()
        self._dailySales = DAO.get_sales()

    @property
    def order_methods(self) -> list[OrderMethod]:
        return list(self._order_methods)  # restituisce copia

    @property
    def products(self) -> list[Product]:
        return list(self._products)

    @property
    def retailers(self) -> list[Retailer]:
        return list(self._retailers)

    def find_method_by_code(self, code: int) -> OrderMethod | None:
        for m in self._order_methods:
            if m.order_method_code == code:
                return m
        return None

    def find_products_by_brand(self, brand: str) -> list[Product]:
        return [p for p in self._products if p.product_brand == brand]

    def find_retailers_by_code(self, code: int) -> list[Retailer]:
        return [r for r in self._retailers if r.retailer_code == code]

    def find_sales(self,
                   year: int | None = None,
                   brand: str | None = None,
                   retailer: str | None = None
                   ) -> list[DailySale]:
        """
        year=None → nessun filtro anno
        brand=None → nessun filtro brand
        retailer=None → nessun filtro retailer
        """
        # Pre‐calcola i set di validità
        if brand:
            valid_products = set()
            for p in self._products:
                if p.product_brand == brand:
                    valid_products.add(p)
        else:
            valid_products = None

        # valid_retailers
        if retailer:
            valid_retailers = set()
            for r in self._retailers:
                if r.retailer_name == retailer:
                    valid_retailers.add(r)
        else:
            valid_retailers = None

        if year:
            valid_years = set()
            for y in self._dailySales:
                if y.date.year == year:
                    valid_years.add(y)
        else:
            valid_years = None

        filtered: list[DailySale] = []
        for sale in self._dailySales:
            # filtro anno
            if year is not None and sale.date.year == year:
                continue

            # filtro brand (solo se valid_products non è None)
            if valid_products is not None and sale.product_number not in valid_products:
                continue

            # filtro retailer (solo se valid_retailers non è None)
            if valid_retailers is not None and sale.retailer_code not in valid_retailers:
                continue

            filtered.append(sale)
            return sorted(
                filtered,
                key=lambda s: s.unit_sale_price * s.quantity,
                reverse=True
            )

if __name__ == "__main__":
    model = Model()

    # Inline tests for find_sales
    print("\n-- All sales (no filters) --")
    all_sales = model.find_sales()
    print(f"Count: {len(all_sales)}")

    print("\n-- Year filter: 2024 --")
    sales_2024 = model.find_sales(year=2024)
    print(f"Count: {len(sales_2024)}")

    print("\n-- Brand filter: 'TrailChef' --")
    sales_brand = model.find_sales(brand="TrailChef")
    print(f"Count: {len(sales_brand)}")

    print("\n-- Retailer filter: 'Italy' --")
    sales_retailer = model.find_sales(retailer="Italy")
    print(f"Count: {len(sales_retailer)}")

    print("\n-- Combined filters: year=2024, brand='TrailChef' --")
    sales_comb = model.find_sales(year=2024, brand="TrailChef")
    print(f"Count: {len(sales_comb)}")

    print("\n-- Combined filters: year=2024, brand='TrailChef', retailer='Italy' --")
    sales_comb2 = model.find_sales(year=2024, brand="TrailChef", retailer="Italy")
    print(f"Count: {len(sales_comb2)}")