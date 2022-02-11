# Fisher-Yates shuffle algorithm

from random import random


def randomize_array(arr):
    arr_length = len(arr)
    curr_num = arr_length - 1
    while curr_num >= 0:
        rand = round(random() * curr_num)
        arr[rand], arr[curr_num] = arr[curr_num], arr[rand]
        curr_num -= 1


arr = [1, 2, 4, 5, 6, 6, 7, 8, 9, 10]

randomize_array(arr)

print(arr)
