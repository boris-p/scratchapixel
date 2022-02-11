# Finding sum of digits of a number until sum becomes single digit

# examples
# Input : 1234
# Output : 1  Explenation: 1 + 2 + 3 + 4 = 10 -> 1 + 0 = 1

def dig_sum(num):
    if num < 10:
        return num

    while num >= 10:
        num = num % 10 + dig_sum(num // 10)
    return num


assert dig_sum(10) == 1
assert dig_sum(11) == 2
assert dig_sum(1234) == 1
assert dig_sum(99) == 9

# there's also a o(1) solution for this
# If a number n is divisible by 9, then the sum of its digit until sum becomes single digit is always 9.
# A number can be of the form 9x or 9x + k. For the first case, answer is always 9. For the second case, and is always k.

# so:
# If n == 0
#    return 0;

# If n % 9 == 0
#     digSum(n) = 9
# Else
#     digSum(n) = n % 9
