# write a function that takes in a targetSum and an array of numbers sa arguments
# the function should return the smallest number of values to sum if they exist (any option is ok, don't need all of them)
# we may use an element in the array as many times as needed and assume that all inputs are nonnegative

def best_sum(target, arr, cache={}):
    if target in cache:
        return cache[target]
    if target == 0:
        return []
    if target < 0:
        return None

    shortest_combination = None

    for num in arr:
        remainder = target - num
        combination = best_sum(remainder, arr, cache)
        if combination is not None:
            combination = [*combination, num]
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination
    cache[target] = shortest_combination
    return cache[target]


print(best_sum(6, [2]))
print(best_sum(7, [2, 3]))
print(best_sum(254, [2], {}))
print(best_sum(300, [7, 14], {}))
print(best_sum(100, [1, 2, 5, 25], {}))
