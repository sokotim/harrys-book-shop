from enum import Enum
from typing import List


class Volume(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5


class BookInstance(object):
    price = 8

    def __init__(self, volume: Volume) -> None:
        self.volume = volume


class Basket(object):
    discounts = {2: 0.05, 3: 0.10, 4: 0.20, 5: 0.25}

    def __init__(self, items: List[BookInstance] = []) -> None:
        self.items = items

    def get_total_price(self) -> float:
        sets: List[List[BookInstance]] = []

        for book_instance in self.items:
            create_new_set = True
            for set in sets:
                if book_instance.volume not in [book.volume for book in set]:
                    set.append(book_instance)
                    create_new_set = False
                    break
            if create_new_set:
                sets.append([book_instance])

        total_price = 0

        for set in sets:
            num_books_in_set = len(set)
            set_discount = self.discounts[num_books_in_set]
            set_price = sum([book.price for book in set])
            set_price_discounted = set_price * (1 - set_discount)
            total_price += set_price_discounted

        return total_price
