import copy

# devide and conquer algorithm
# worst case is n^2 but it's rarely that, bit in big arrays more often merge sort is used
# it's inner loop can be efficiently implemented on most architectures and in most real world data
# this will not be n^2


def partition(arr, start, end):
    # let's start with picking the last element as the partition
    pivot = arr[end]
    last_index = end
    end -= 1
    pivot_index = start

    while start <= end:
        if arr[start] <= pivot:
            start += 1
            pivot_index += 1
        else:
            # swap
            arr[start], arr[end] = arr[end], arr[start]
            end -= 1
    arr[pivot_index], arr[last_index] = arr[last_index], arr[pivot_index]

    return pivot_index


def quick_sort(arr, low=0, high=0):
    if (low < high):
        p1 = partition(arr, low, high)
        quick_sort(arr, low, p1-1)
        quick_sort(arr, p1+1, high)


arr = [1, 34, 54, 6, 23, 7, 4, 2, 3, 5, 7, 8, 4, 23, 45, 7, 45, 23, 12, 45]

a1 = copy.deepcopy(arr)
a2 = copy.deepcopy(arr)

quick_sort(a1, 0, len(arr) - 1)
a2.sort()

assert a1 == a2


b = [3, 5, 3, 1, 5, 6, 9, 2]
b1 = copy.deepcopy(b)
b2 = copy.deepcopy(b)

quick_sort(b1, 0, len(b1) - 1)
b2.sort()

assert b1 == b2
