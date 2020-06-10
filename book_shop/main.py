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
        different_titles:List[BookInstance] = []
        duplicate_titles:List[BookInstance] = []

        for book_instance in self.items:
            if book_instance.volume not in [book.volume for book in different_titles]:
                different_titles.append(book_instance)
            else:
                duplicate_titles.append(book_instance)

        amount_of_different_titles = len(different_titles)
        discount_for_different_titles = Basket.discounts.get(
            amount_of_different_titles, 0
        )
        different_titles_price = sum([book.price for book in different_titles])
        different_titles_price_discounted = different_titles_price * (
            1 - discount_for_different_titles
        )
        duplicate_titles_price = sum([book.price for book in duplicate_titles])

        total_price = different_titles_price_discounted + duplicate_titles_price

        return total_price
