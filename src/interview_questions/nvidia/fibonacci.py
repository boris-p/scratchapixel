# The Fibonacci numbers, commonly denoted F(n) form a sequence,
# called the Fibonacci sequence, such that each number is the sum
# of the two preceding ones, starting from 0 and 1

def fibonacci(num):

    if num == 0:
        return 0
    prevprev = 0
    prev = 1
    for _ in range(2, num):
        tmp = prevprev
        prevprev = prev
        prev = tmp + prevprev
    res = prev + prevprev
    return res


cache = {}


def fibonacci_rec(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    if cache.get(num) is not None:
        return cache.get(num)
    val = fibonacci_rec(num - 1) + fibonacci_rec(num - 2)
    cache[num] = val
    return val


assert fibonacci(2) == 1  # f(1) + f(0) = 1 + 0 = 0
assert fibonacci(3) == 2  # f(2) + f(1) = 1 + 1 = 2
assert fibonacci(4) == 3  # f(3) + f(2) = 1 + 2 = 4
assert fibonacci(10) == 55
assert fibonacci(42) == 267914296


assert fibonacci_rec(3) == 2  # f(2) + f(1) = 1 + 1 = 2
assert fibonacci_rec(4) == 3  # f(3) + f(2) = 1 + 2 = 4
assert fibonacci_rec(10) == 55
assert fibonacci_rec(42) == 267914296
