# we're travelers in a 2d grid. Begin at the top left and the goal is to travel to the bottom right (can only move down and right)
# in how many ways can we travel to the goal on a grid of m*n?

def grid_traveler(m, n, cached={}) -> int:
    if m < 2 or n < 2:
        return min(m, n)
    if (m, n) in cached:
        return cached[(m, n)]
    if (n, m) in cached:
        return cached[(n, m)]
    cached[(m, n)] = grid_traveler(m-1, n, cached) + \
        grid_traveler(m, n-1, cached)
    return cached[(m, n)]
    # return grid_traveler(m-1, n) + grid_traveler(m, n-1)


print("should all be 1")
print(grid_traveler(2, 1))
print(grid_traveler(1, 1))
print(grid_traveler(3, 0))
print(grid_traveler(0, 4))
print(grid_traveler(5, 1))
print("3*2 grid")
print(grid_traveler(3, 2))

print("3*3 grid")
print(grid_traveler(3, 3))
print(grid_traveler(18, 18))
