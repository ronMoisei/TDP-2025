from dataclasses import dataclass, field
from typing import List

@dataclass
class pizza():
    ingredients: List = field(default_factory = lambda: ["dow", "tomatoes"])