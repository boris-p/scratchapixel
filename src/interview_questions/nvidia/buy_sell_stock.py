# can only perform one transaction

from typing import List


def buy_sell_stock(prices: List[int]) -> int:

    left, right = 0, 0
    maxP = 0

    while right < len(prices):
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]
            maxP = max(maxP, profit)
        else:
            left = right
        right += 1

    return maxP


input = [7, 1, 5, 3, 6, 4]
expected_output = 5


assert(buy_sell_stock(input)) == expected_output
