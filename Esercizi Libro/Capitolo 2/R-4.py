"""Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number
of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type."""
from typing import Union


class Flower:
    def __init__(self, name: str, petals: int, price: float):
        self._name = name
        self._petals = petals
        self._price = price

    @property
    def name(self) -> str:
        return self._name
    @property
    def petals(self) -> int:
        return self._petals
    @property
    def price(self) -> float:
        return self._price
    @name.setter
    def name(self, name: str):
        if not(isinstance(name, str)):
            raise TypeError("Name must be a string")
        self._name = name

    @petals.setter
    def petals(self, petals: int):
        if not(isinstance(petals, int)) or petals <= 0:
            raise TypeError("Petals must be a positive integer")
        self._petals = petals

    @price.setter
    def price(self, price: Union[float, int]):
        if not(isinstance(price, (float, int))) or price <= 0:
            raise TypeError("Price must be a positive number")


    def __str__(self):
        desc = f"The name of the flower is {self.name}, it has {self.petals} petals and it costs{self.price}"
        return desc

    def __repr__(self):
        tech_descr = {"name": self.name, "petals": self.petals, "price": self.price}
        return str(tech_descr)

if __name__ == "__main__":

    m = Flower("Margherita", 6, 8)
    print(m.__str__())
    print(m.__repr__())