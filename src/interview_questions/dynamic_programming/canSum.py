# write a function that takes in a targetSum and an array of numbers sa arguments
# the function should return true if it's possible to generate the sum from some of the arguments
# we may use an element in the array as many times as needed and assume that all inputs are nonnegative

def can_sum(target, arr, cache={}):
    if target in cache:
        return cache[target]
    if target == 0:
        return True
    if target < 0:
        return False
    # if True in [can_sum(target - i, arr, cache) for i in arr]:
    for i in arr:
        s = can_sum(target - i, arr, cache)
        cache[target - i] = s
        if s is True:
            return True
    return False


print(can_sum(7, [2, 4]))
print(can_sum(7, [1], {}))
print(can_sum(254, [1, 3, 5, 67], {}))
print(can_sum(300, [7, 14], {}))
