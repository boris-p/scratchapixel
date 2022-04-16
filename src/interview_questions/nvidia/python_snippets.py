from collections import deque
import heapq
from typing import List

# deque
print('-------------------------deque-------------------------')

q = deque(['name', 'age', 'position'])

print(q)

q.append("years_of_experience")
q.appendleft("id")


# heap queue

print('-------------------------heap queue-------------------------')

# initialize list
l = [4, 5, 6, 8, 9, 3]
heapq.heapify(l)
print(l)


while len(l):
    print(heapq.heappop(l))

heapq.heappush(l, 4)
heapq.heappush(l, 7)
heapq.heappush(l, 18)
heapq.heappush(l, 2)
heapq.heapreplace(l, 6)

while len(l):
    print(heapq.heappop(l))

print('-------------------------set-------------------------')
s = set()

s.add(34)
s.add(5)
s.add(6)
for i in s:
    print(i)


# build adj list


x = 3
prerequisites: List

prereq = {c: [] for c in range(x)}
for crs, pre in prerequisites:
    prereq[crs].append(pre)
