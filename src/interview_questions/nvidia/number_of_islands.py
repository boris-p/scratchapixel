# we are given 2d grid map of 1's and 0's and we need to cound the number of islands (connected 1's)


from typing import List


def number_of_islands(map: List[List[int]]) -> int:
    rows = len(map)
    cols = len(map[0])

    islands = 0
    visited = {}

    def dfs(i: int, j: int):
        if map[i][j] == 0:
            return False

        if visited.get((i, j)):
            return False

        visited[(i, j)] = True

        # left
        if i-1 >= 0:
            dfs(i-1, j)
        # top
        if j-1 >= 0:
            dfs(i, j-1)
        # right
        if i+1 < rows:
            dfs(i + 1, j)
        # bottom
        if j+1 < cols:
            dfs(i, j + 1)
        return True

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j) is True:
                islands += 1

    print('islands', islands)
    return islands


input = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
]

assert (number_of_islands(input)) == 2
