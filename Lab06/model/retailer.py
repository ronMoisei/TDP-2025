from dataclasses import dataclass

@dataclass
class Retailer:
    retailer_code: int
    retailer_name: str
    type: str
    country: str

    @property
    def retailer_code(self) -> int:
        return self._retailer_code

    @retailer_code.setter
    def retailer_code(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("retailer_code must be a non-negative int")
        self._retailer_code = value

    @property
    def retailer_name(self) -> str:
        return self._retailer_name

    @retailer_name.setter
    def retailer_name(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError("retailer_name must be a non-empty string")
        self._retailer_name = value

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError("type must be a non-empty string")
        self._type = value

    @property
    def country(self) -> str:
        return self._country

    @country.setter
    def country(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError("country must be a non-empty string")
        self._country = value

    def __str__(self) -> str:
        return f"[{self.retailer_code}] {self.retailer_name} ({self.type}) – {self.country}"

    def __repr__(self) -> str:
        return (
            f"Retailer(retailer_code={self.retailer_code!r}, "
            f"retailer_name={self.retailer_name!r}, "
            f"type={self.type!r}, "
            f"country={self.country!r})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Retailer):
            return NotImplemented
        return (
            self.retailer_code == other.retailer_code and
            self.retailer_name == other.retailer_name and
            self.type          == other.type and
            self.country       == other.country
        )

    def __lt__(self, other: "Retailer") -> bool:
        if not isinstance(other, Retailer):
            return NotImplemented
        # ordine per codice, poi nome
        return (
            (self.retailer_code, self.retailer_name) <
            (other.retailer_code, other.retailer_name)
        )

    def __hash__(self) -> int:
        return hash(self.retailer_code)


if __name__ == "__main__":
    r = Retailer(retailer_code=123, retailer_name="Acme", type="Online", country="Italy")
    print(str(r))
    print(repr(r))
    print({r})
