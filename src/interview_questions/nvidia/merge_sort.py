import copy


def merge_sort(arr):
    arr_len = len(arr)
    if arr_len < 2:
        return arr

    left = merge_sort(arr[:arr_len // 2])
    right = merge_sort(arr[arr_len // 2:])

    left_len = len(left)
    right_len = len(right)
    left_i = 0
    right_i = 0

    tmp_arr = []
    while left_i < left_len and right_i < right_len:
        if left[left_i] <= right[right_i]:
            tmp_arr.append(left[left_i])
            left_i += 1
        else:
            tmp_arr.append(right[right_i])
            right_i += 1

    # leftovers
    return tmp_arr + left[left_i:] + right[right_i:]


arr = [1, 34, 54, 6, 23, 7, 4, 2, 3, 5, 7, 8, 4, 23, 45, 7, 45, 23, 12, 45]

a1 = copy.deepcopy(arr)
a2 = copy.deepcopy(arr)

a1 = merge_sort(a1)
print(a1)
a2.sort()

assert a1 == a2


b = [3, 5, 3, 1, 5, 6, 9, 2]
b1 = copy.deepcopy(b)
b2 = copy.deepcopy(b)

b1 = merge_sort(b1)
b2.sort()

assert b1 == b2
