import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda t: t[0])

        res, min_heap = [], []
        i, cur_time = 0, tasks[0][0]

        while min_heap or i < len(tasks):
            while i < len(tasks) and cur_time >= tasks[i][0]:
                heapq.heappush(min_heap, [tasks[i][1], tasks[i][2]])

            if not min_heap:
                cur_time += tasks[i][0]
            else:
                proc_time, index = heapq.heappop(min_heap)
                cur_time += proc_time
                res.append(index)

        return res
