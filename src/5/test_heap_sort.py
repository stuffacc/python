import random
import pytest
from heap_sort import heap_sort


@pytest.fixture
def random_arr():
    random_size = random.randint(0, 1000)

    arr = [random.randint(-1000, 1000) for _ in range(random_size)]

    return arr


def test_empty_array():
    arr = []
    heap_sort(arr)

    assert arr == []


def test_single_element():
    arr = [42]
    heap_sort(arr)

    assert arr == [42]


def test_sorted_array():
    arr = [1, 2, 3, 4, 5]
    heap_sort(arr)

    assert arr == [1, 2, 3, 4, 5]


def test_reverse_sorted_array():
    arr = [5, 4, 3, 2, 1]
    heap_sort(arr)

    assert arr == [1, 2, 3, 4, 5]


def test_duplicate_elements():
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    heap_sort(arr)

    assert arr == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]


def test_negative_numbers():
    arr = [5, -2, 0, -8, 3, 1, -1]
    heap_sort(arr)

    assert arr == [-8, -2, -1, 0, 1, 3, 5]


def test_all_identical():
    arr = [7, 7, 7, 7, 7]
    heap_sort(arr)

    assert arr == [7, 7, 7, 7, 7]


def test_random_with_build_in_sort(random_arr):
    random_arr2 = random_arr.copy()

    heap_sort(random_arr)
    random_arr2.sort()

    assert random_arr == random_arr2


if __name__ == '__main__':
    pytest.main()
