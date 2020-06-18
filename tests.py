from book_shop.main import Volume, BookInstance, Basket


def test_total_price():
    two_copies_of_first_book = [BookInstance(Volume.FIRST) for _ in range(2)]
    two_copies_of_second_book = [BookInstance(Volume.SECOND) for _ in range(2)]
    two_copies_of_third_book = [BookInstance(Volume.THIRD) for _ in range(2)]
    one_copy_of_fourth_book = [BookInstance(Volume.FOURTH)]
    one_copy_of_fifth_book = [BookInstance(Volume.FIFTH)]

    items = (
        two_copies_of_first_book
        + two_copies_of_second_book
        + two_copies_of_third_book
        + one_copy_of_fourth_book
        + one_copy_of_fifth_book
    )

    basket = Basket(items)

    assert basket.get_total_price() == 51.20


def test_total_price_unsortet():
    all_five_volumes = [BookInstance(volume) for volume in list(Volume)]
    just_the_first_three_volumes = [
        BookInstance(volume) for volume in [Volume.FIRST, Volume.SECOND, Volume.THIRD]
    ]
    items = all_five_volumes + just_the_first_three_volumes
    basket = Basket(items)

    assert basket.get_total_price() == 51.20


if __name__ == "__main__":
    test_total_price()
    test_total_price_unsortet()
