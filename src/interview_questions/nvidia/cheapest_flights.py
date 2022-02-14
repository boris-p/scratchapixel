# shortest path given a start node and a destination node

# can do this using dijkstra, but can also use
# an algorithm called Bellman-Ford which calculates
# shortest paths in a weighted graph by goiong over all the edges

# for an input of
# n: num of cities
# flights: [
# [0,1,100],
# [1,2,100]
# [0,2,500]
# ]
# src: 0
# dst: 2
# k: 1

# expected output is 200  (0 -> 1 -> 2)


from typing import List


def find_cheapest_flight(n: int, flights: List[List[int]], src: int, dst: int, k: int):
    prices = [float("inf")] * n
    prices[src] = 0

    for _ in range(k + 1):
        tmp_prices = prices.copy()
        for s, d, p in flights:  # s=source, d=destination, p=price
            if prices[s] == float("inf"):
                continue
            if prices[s] + p < tmp_prices[d]:
                tmp_prices[d] = prices[s] + p
        prices = tmp_prices
    return -1 if prices[dst] == float("inf") else prices[dst]
