# you are given a nXn matrix representing an image.
# rotate it by 90 degreees clockwise in place

# 0,0 -> 0,n-1
# 0,n-1 -> n-1, n-1
# n-1,n-1 -> n-1, 0
# n-1, 0 -> 0,0

# 0,1 -> 1, n-1

from typing import List


def rotate_image(matrix: List[List[int]]):

    for current_rect in range(len(matrix) // 2):

        end = len(matrix) - current_rect - 1
        for i in range(end):
            first_elm = matrix[current_rect][i]
            second_elm = matrix[i][end]
            third_elm = matrix[end][end - i]
            forth_elm = matrix[end-i][current_rect]

            matrix[current_rect][i] = forth_elm
            matrix[i][end] = first_elm
            matrix[end][end - i] = second_elm
            matrix[end-i][current_rect] = third_elm


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

rotate_image(matrix)
assert(matrix) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
