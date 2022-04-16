A few of my lessons learned from the last few days of getting deeper into coding questions.
This is just my personal take on approaches I think worth taking.

## sliding window
Whenever we have a problem we can translate to an array where we need to find a range, a continouous range in the array,
a sliding window might make sense.
Something we can preprocess an array and then do it.

## Topologiacl sort
whenever we have dependencies and we need to calculate in which order things will happen Topologiacl sort might make sense.
We need to remember to check that there are no cycles when doing this

## priority queue/heap
if we need min/max of a list of items that are updating a priority queue/heap will be a good bet.

## graph algorithms
When there are many options for how things can happen and we can draw a decision tree, graph algorithms make sense. 
Even if at first things seem really inefficient sometimes we can use caching (dynamic programming) to really speed things up.

## stack/ queue
when things happen in order and we need to decide what to do based on the next thing that happens a stack or a queue might make sense.

In any case draw out the solution and think of the data structures that can represent the solution, even if not efficient, often times there's a 
way to use some trick to make things more efficient

# Data structures and complexities

## priority queue/ heap - 

tree structure where the head node is the smallest (min heap), this feature is recursive - so for a sub node, all nodes under it are bigger than it as well.

peak at minimum - o(1)
remove min - o(logn)
insertion - o(logn)
heapify - o(n)

## binary search tree
need to remember that a binary search tree is not garenteed to be balanced.

search - o(n) - worst - it will be the heigt of the tree
insert - o(n) - worst - it will be the heigt of the tree
delete - o(n) - worst - it will be the heigt of the tree

## AVL / height balanced tree

search - o(logn)
insert - o(logn)
delete - o(logn)


## AVL / height balanced tree

search - o(logn)

## List

append/pop complecity is o(n). At least in python

## Deque
Double ended queue
append & pop complecity o(1)

# Algos and approaches

## Dijkstra's shortest path algorithm
Finding shortest paths 
o(v2) but with priority queue it drops to o(v + ologv)

## Sliding window