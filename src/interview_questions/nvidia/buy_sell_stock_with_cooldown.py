# Best Time to Buy and Sell Stock with Cooldown of one day - Leetcode 309 - Python
# the idea here is to have a graph of all the options and use dynamic programming to cahce the results

from typing import List


class Solution:

    def max_profit(self, prices: List[int]) -> int:
        dp = {}  # key (i, buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        return dfs(0, True)
