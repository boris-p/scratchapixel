# Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].

import math


def binary_search(arr, search_num, offset=0):
    middle_index = math.floor(len(arr) / 2)
    if arr[middle_index] == search_num:
        return middle_index + offset

    if middle_index == 0:
        return None

    if arr[middle_index] > search_num:
        return binary_search(arr[:middle_index], search_num, offset)
    else:
        return binary_search(arr[middle_index:], search_num, offset + middle_index)


arr = [1, 3, 5, 8, 12, 16, 19, 222, 324, 564, 753, 874]

assert binary_search(arr, 5) == 2
assert binary_search(arr, 5) == 2
assert binary_search(arr, 874) == 11
assert binary_search(arr, 1) == 0

assert binary_search(arr, 123) is None


arr = [1, 3, 5, 8, 12, 16, 19, 222, 324, 564, 753, 874, 900]
assert binary_search(arr, 16) == 5
assert binary_search(arr, 564) == 9
assert binary_search(arr, 999) is None

# binary search iterative


def binary_search_iterative(arr, search_num):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == search_num:
            return mid

        if arr[mid] > search_num:
            high = mid - 1
        else:
            low = mid + 1
    return None


arr = [1, 3, 5, 8, 12, 16, 19, 222, 324, 564, 753, 874]


assert binary_search_iterative(arr, 5) == 2
assert binary_search_iterative(arr, 5) == 2
assert binary_search_iterative(arr, 874) == 11
assert binary_search_iterative(arr, 1) == 0

assert binary_search_iterative(arr, 123) is None


arr = [1, 3, 5, 8, 12, 16, 19, 222, 324, 564, 753, 874, 900]
assert binary_search_iterative(arr, 16) == 5
assert binary_search_iterative(arr, 564) == 9
assert binary_search_iterative(arr, 999) is None
