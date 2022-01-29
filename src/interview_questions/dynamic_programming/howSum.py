# write a function that takes in a targetSum and an array of numbers as arguments
# the function should return the values to sum if they exist (any option is ok, don't need all of them)
# we may use an element in the array as many times as needed and assume that all inputs are nonnegative

def how_sum(target, arr, cache={}):
    if target in cache:
        return cache[target]
    if target == 0:
        return []
    if target < 0:
        return None
    for num in arr:
        remainder = target - num
        remainder_res = how_sum(remainder, arr, cache)
        if isinstance(remainder_res, list):
            cache[remainder] = [*remainder_res, num]
            return cache[remainder]
    return None


print(how_sum(7, [2, 3]))
print(how_sum(6, [2]))
print(how_sum(254, [2], {}))
print(how_sum(7, [2, 4]))
print(how_sum(7, [1], {}))
print(how_sum(254, [3, 5, 67, 2], {}))
print(how_sum(300, [7, 14], {}))
