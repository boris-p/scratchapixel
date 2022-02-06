# Given an array of integers A, every element appears twice except for one. Find that single one.

# Your algorithm should have a linear runtime complexity. Could you implement it without
# using extra memory?

# input: First and only argument of input contains an integer array A.
# output: Return a single integer denoting the single element.


def single_number(arr):
    existing_numbers = dict()
    for i in arr:
        if i in existing_numbers:
            del existing_numbers[i]
        else:
            existing_numbers[i] = i
    return list(existing_numbers.values())[0]


print(single_number([1, 2, 1, 3, 3]))
