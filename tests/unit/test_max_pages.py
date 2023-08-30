

from lib.paginator import get_max_pages


def test_get_max_pages():

    size_conditions = [
        (10, 10, 1),
        (10, 5, 2),
        (10, 3, 4),
        (10, 1, 10),
        (10, 0, 1),
        (90, 10, 9),
        (68595, 10, 6860),
        (68595, 100, 686),
        (68595, 8, 8575),
    ]

    for total_items, size, expected in size_conditions:
        assert get_max_pages(total_items, size) == expected
