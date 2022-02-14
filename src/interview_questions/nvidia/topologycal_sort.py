# we can order DAGS
# the graph cannot have cycles to
# algo runs in o(V + E)

# we're going to solve Course Schedule II - Topological Sort - Leetcode 210
# the solution is topological sort and we also need to detect cycles


from typing import List, Literal


class Solution:
    def find_order(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:

        # build adjacency list of prerequisites

        prereq = {c: [] for c in range(num_courses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(num_courses):
            if dfs(c) == False:
                return []

        return output
