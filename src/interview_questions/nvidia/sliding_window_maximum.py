# Given an array and an integer K, find the maximum for each and every contiguous subarray of size k.

import collections
from typing import List


def sliding_window_max(nums: List[int], k: int) -> List[int]:

    res: List[int] = []
    l = r = 0  # window indexes

    deq = collections.deque()

    while r < len(nums):
        while deq and nums[deq[-1]] < nums[r]:
            deq.pop()
        deq.append(r)

        if l > deq[0]:
            deq.popleft()

        if (r + 1) >= k:
            res.append(nums[deq[0]])
            l += 1
        r += 1
    return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

expected_output = [3, 3, 5, 5, 6, 7]

assert(sliding_window_max(nums, k)) == expected_output
