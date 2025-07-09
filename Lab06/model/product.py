from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Product:
    product_number: int
    product_line: str
    product_type: str
    product: str
    product_brand: str
    product_color: str
    unit_cost: float
    unit_price: float

    @property
    def product_number(self) -> int:
        return self._product_number

    @product_number.setter
    def product_number(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("product_number must be a non-negative int")
        self._product_number = value

    @property
    def product_line(self) -> str:
        return self._product_line

    @product_line.setter
    def product_line(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError("product_line must be a non-empty string")
        self._product_line = value

    @property
    def product_type(self) -> str:
        return self._product_type

    @product_type.setter
    def product_type(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError("product_type must be a non-empty string")
        self._product_type = value

    @property
    def product(self) -> str:
        return self._product

    @product.setter
    def product(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError("product must be a non-empty string")
        self._product = value

    @property
    def product_brand(self) -> str:
        return self._product_brand

    @product_brand.setter
    def product_brand(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError("product_brand must be a non-empty string")
        self._product_brand = value

    @property
    def product_color(self) -> str:
        return self._product_color

    @product_color.setter
    def product_color(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError("product_color must be a non-empty string")
        self._product_color = value

    @property
    def unit_cost(self) -> float:
        return self._unit_cost

    @unit_cost.setter
    def unit_cost(self, value):
        if not isinstance(value, (int, float, Decimal)) or value < 0:
            raise ValueError("unit_cost must be a non-negative number")
        self._unit_cost = float(value)

    @property
    def unit_price(self) -> float:
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        if not isinstance(value, (int, float, Decimal)) or value < 0:
            raise ValueError("unit_price must be a non-negative number")
        self._unit_price = float(value)

    def __str__(self) -> str:
        return (
            f"Product[{self.product_number}]: {self.product} "
            f"({self.product_line}/{self.product_type}), "
            f"brand={self.product_brand}, color={self.product_color}, "
            f"cost={self.unit_cost:.2f}, price={self.unit_price:.2f}"
        )

    def __repr__(self) -> str:
        return (
            f"Product(product_number={self.product_number!r}, "
            f"product_line={self.product_line!r}, "
            f"product_type={self.product_type!r}, "
            f"product={self.product!r}, "
            f"product_brand={self.product_brand!r}, "
            f"product_color={self.product_color!r}, "
            f"unit_cost={self.unit_cost!r}, "
            f"unit_price={self.unit_price!r})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return (
            self.product_number == other.product_number and
            self.product_line   == other.product_line   and
            self.product_type   == other.product_type   and
            self.product        == other.product        and
            self.product_brand  == other.product_brand  and
            self.product_color  == other.product_color  and
            self.unit_cost      == other.unit_cost      and
            self.unit_price     == other.unit_price
        )

    def __lt__(self, other: "Product") -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.product_number < other.product_number

    def __hash__(self) -> int:
        return hash(self.product_number)


if __name__ == "__main__":
    p = Product(
        product_number=10123,
        product_line="Classic Cars",
        product_type="Convertible",
        product="1957 Chevy Bel Air",
        product_brand="AutoArt",
        product_color="Red",
        unit_cost=58.75,
        unit_price=95.50
    )
    print(str(p))
    print(repr(p))
