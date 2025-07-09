from dataclasses import dataclass

@dataclass
class OrderMethod:
    order_method_code: int
    order_method_type: str

    @property
    def order_method_code(self) -> int:
        return self._order_method_code

    @order_method_code.setter
    def order_method_code(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("order_method_code must be a non-negative int")
        self._order_method_code = value

    @property
    def order_method_type(self) -> str:
        return self._order_method_type

    @order_method_type.setter
    def order_method_type(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError("order_method_type must be a non-empty string")
        self._order_method_type = value

    def __str__(self) -> str:
        return f"OrderMethod(code={self.order_method_code}, type='{self.order_method_type}')"

    def __repr__(self) -> str:
        return (f"OrderMethod(order_method_code={self.order_method_code!r}, "
                f"order_method_type={self.order_method_type!r})")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, OrderMethod):
            return NotImplemented
        return (self.order_method_code == other.order_method_code and
                self.order_method_type == other.order_method_type)

    def __lt__(self, other: "OrderMethod") -> bool:
        if not isinstance(other, OrderMethod):
            return NotImplemented
        # define ordering by code, then by type
        if self.order_method_code != other.order_method_code:
            return self.order_method_code < other.order_method_code
        return self.order_method_type < other.order_method_type

    def __hash__(self) -> int:
        return hash((self.order_method_code, self.order_method_type))


if __name__ == "__main__":
    om1 = OrderMethod(1, "Online")
    om2 = OrderMethod(2, "Retail")
    print(str(om1))   # OrderMethod(code=1, type='Online')
    print(repr(om2))  # OrderMethod(order_method_code=2, order_method_type='Retail')
    print(om1 == om2) # False
    print(om1 < om2)  # True
    s = {om1, om2}    # uses __hash__
    print(s)

