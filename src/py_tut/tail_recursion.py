# let's write a program that calculated the factorial in normal recursion

def factorial(n: int):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n


print("factorial of 1:", factorial(1))
print("factorial of 4:", factorial(4))
print("factorial of 6:", factorial(6))

# now let's write it as a tail recursion


def tail_factorial(n: int, acc: int = 1):
    if n == 0:
        return acc
    else:
        return tail_factorial(n-1, acc * n)


print("tail factorial of 1:", factorial(1))
print("tail factorial of 4:", factorial(4))
print("tail factorial of 6:", factorial(6))


# actally though, tail recursion is not supported in python unless we do some fancier things
# with exceptions and catching them in a decorator
# https://chrispenner.ca/posts/python-tail-recursion
# though maybe there's some other ways as well
