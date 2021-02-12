# as an iteration

print("as iteration")


def iterative_fibonnaci(num: int):
    prev = 0
    curr = 1
    if num == 0:
        return num
    else:
        for _ in range(1, num):
            tmp = prev + curr
            prev = curr
            curr = tmp
    return curr


print(iterative_fibonnaci(35))

# as a recursive method


print("as recursive method")


def rec_fibonacci(num: int):
    if (num <= 1):
        return num
    else:
        return rec_fibonacci(num - 1) + rec_fibonacci(num - 2)


print(rec_fibonacci(35))


print("as recursive method with memoization")


def rec_dynamic_fibonacci(num: int, cached={}):
    if (num <= 1):
        return num
    if num in cached:
        return cached[num]
    else:
        cached[num] = rec_dynamic_fibonacci(
            num - 1, cached) + rec_dynamic_fibonacci(num - 2, cached)
        return cached[num]


for i in range(36):
    print(rec_dynamic_fibonacci(i))
