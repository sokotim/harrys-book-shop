from enum import IntEnum, unique
from typing import List


@unique
class Volume(IntEnum):
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

    def get_sets(self) -> List[List[BookInstance]]:
        self.items.sort(key=lambda book_instance: book_instance.volume)
        sets: List[List[BookInstance]] = []
        for book_instance in self.items:
            set_candidate_indices: List[int] = []

            for set_num, set in enumerate(sets):
                if book_instance.volume not in [book.volume for book in set]:
                    set_candidate_indices.append(set_num)
            if len(set_candidate_indices) > 1:
                min_total_price: float = float("inf")
                best_candidate_index: int = 0
                for set_candidate_index in set_candidate_indices:
                    total_price_with_book_in_this_set: float = 0.0
                    for set_index, set in enumerate(sets):
                        if set_index == set_candidate_index:
                            set_with_book = set + [book_instance]
                            total_price_with_book_in_this_set += self.get_discounted_set_price(
                                set_with_book
                            )
                        else:
                            total_price_with_book_in_this_set += self.get_discounted_set_price(
                                set
                            )
                    if total_price_with_book_in_this_set < min_total_price:
                        min_total_price = total_price_with_book_in_this_set
                        best_candidate_index = set_candidate_index
                sets[best_candidate_index].append(book_instance)

            elif len(set_candidate_indices) == 1:
                sets[set_candidate_indices[0]].append(book_instance)
            else:
                sets.append([book_instance])
        return sets

    def get_discounted_set_price(self, set: List[BookInstance]) -> float:
        num_books_in_set = len(set)
        set_discount = self.discounts.get(num_books_in_set, 0.0)
        set_price = sum([book.price for book in set])
        set_price_discounted = set_price * (1 - set_discount)
        return set_price_discounted

    def get_total_price(self) -> float:
        total_price: float = 0

        for set in self.get_sets():
            total_price += self.get_discounted_set_price(set)

        return total_price
