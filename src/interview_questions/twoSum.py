# Given an array of integers nums and an integer target, return indices of
# the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    my_dict = dict()
    for i, val in enumerate(nums):
        my_dict[val] = i

    for num in nums:
        if target - num in my_dict and target - num != num:
            return [my_dict[num], my_dict[target - num]]
    return []


nums = [3, 2, 4]
target = 6

assert twoSum(nums, target) == [1, 2]
