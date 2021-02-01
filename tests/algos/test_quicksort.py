from src.algos.quicksort import quicksort


def test_quicksort_1():
    arr = [1, 6, 2]
    res = quicksort(arr)
    expexted_arr = [1, 2, 6]
    assert res == expexted_arr


def test_quicksort_2():
    arr = [1, 4, 6, 2, 7, 7, 7, 5, 2, 3, 2, 1, 8, 0, 9]
    res = quicksort(arr)
    expexted_arr = [0, 1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9]
    assert res == expexted_arr
