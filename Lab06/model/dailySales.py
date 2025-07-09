from dataclasses import dataclass
from datetime import date
from decimal import Decimal

@dataclass
class DailySale:
    retailer_code: int
    product_number: int
    order_method_code: int
    date: date
    quantity: int
    unit_price: float
    unit_sale_price: float

    @property
    def retailer_code(self) -> int:
        return self._retailer_code

    @retailer_code.setter
    def retailer_code(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("retailer_code must be a non-negative int")
        self._retailer_code = value

    @property
    def product_number(self) -> int:
        return self._product_number

    @product_number.setter
    def product_number(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("product_number must be a non-negative int")
        self._product_number = value

    @property
    def order_method_code(self) -> int:
        return self._order_method_code

    @order_method_code.setter
    def order_method_code(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("order_method_code must be a non-negative int")
        self._order_method_code = value

    @property
    def date(self) -> date:
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, date):
            raise ValueError("date must be a datetime.date")
        self._date = value

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("quantity must be a non-negative int")
        self._quantity = value

    @property
    def unit_price(self) -> float:
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        # accetta int, float o Decimal
        if not isinstance(value, (int, float, Decimal)) or value < 0:
            raise ValueError("unit_price must be a non-negative number")
        self._unit_price = float(value)

    @property
    def unit_sale_price(self) -> float:
        return self._unit_sale_price

    @unit_sale_price.setter
    def unit_sale_price(self, value):
        # accetta int, float o Decimal
        if not isinstance(value, (int, float, Decimal)) or value < 0:
            raise ValueError("unit_sale_price must be a non-negative number")
        self._unit_sale_price = float(value)

    def __str__(self) -> str:
        return (f"Sale[{self.date}]: retailer={self.retailer_code}, "
                f"product={self.product_number}, method={self.order_method_code}, "
                f"qty={self.quantity}, price={self.unit_price:.2f}, "
                f"sale_price={self.unit_sale_price:.2f}")

    def __repr__(self) -> str:
        return (f"DailySale(retailer_code={self.retailer_code!r}, "
                f"product_number={self.product_number!r}, "
                f"order_method_code={self.order_method_code!r}, "
                f"date={self.date!r}, "
                f"quantity={self.quantity!r}, "
                f"unit_price={self.unit_price!r}, "
                f"unit_sale_price={self.unit_sale_price!r})")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DailySale):
            return NotImplemented
        return (
            self.retailer_code    == other.retailer_code and
            self.product_number   == other.product_number and
            self.order_method_code== other.order_method_code and
            self.date             == other.date and
            self.quantity         == other.quantity and
            self.unit_price       == other.unit_price and
            self.unit_sale_price  == other.unit_sale_price
        )

    def __lt__(self, other: "DailySale") -> bool:
        if not isinstance(other, DailySale):
            return NotImplemented
        # ordina per ricavo = quantità * prezzo di vendita
        return (self.quantity * self.unit_sale_price) < (other.quantity * other.unit_sale_price)

