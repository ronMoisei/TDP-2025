"""Draw a class inheritance diagram for the following set of classes:
• Class Goat extends object and adds an instance variable tail and
methods milk( ) and jump().
• Class Pig extends object and adds an instance variable nose and
methods eat(food) and wallow( ).
• Class Horse extends object and adds instance variables height and
color, and methods run() and jump( ).
• Class Racer extends Horse and adds a method race( ).
• Class Equestrian extends Horse, adding an instance variable weight
and methods trot( ) and is trained( )."""

class Goat:
    def __init__(self, name: str, age: int, location: str):
        self._name = name
        self._age = age
        self._location = location
        self._tail = True

    def milk(self):
        return "milked"
    def jump(self):
        return "jumped"

class Pig:
    def __init__(self, name: str, age: int, location: str):
        self._name = name
        self._age = age
        self._location = location
        self._nose = True

    def eat(self, food):
        return "eaten"
    def wallow(self):
        return "wallowed"

class Horse:
    def __init__(self, name: str, age: int, location: str, height: float, color: str):
        self._name = name
        self._age = age
        self._location = location
        self._height = height
        self._color = color

    def run(self):
        return "run"
    def jump(self):
        return "raced"

class Racer(Horse):
    def __init__(self, name: str, age: int, location: str, height: float, color: str):
        super().__init__(name,age,location, height, color)

    def race(self):
        return "raced"

class Equestrian(Horse):
    def __init__(self, name: str, age: int, location: str, height: float, color: str, weight: float):
        super().__init__(name, age, location, height, color)
        self._weight = weight

    def trot(self):
        return "troted"
    def is_trained(self):
        return True


