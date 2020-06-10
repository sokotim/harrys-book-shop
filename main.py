from enum import Enum
from typing import Sequence


class Volume(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5


class BookInstance(object):
    def __init__(self, volume: Volume):
        self.volume = volume


class Basket(object):
    def __init__(self, items: Sequence[BookInstance] = []):
        self.items = items

    def get_total_price(self) -> int:
        return 0
