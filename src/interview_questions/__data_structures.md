# priority queue/ heap - 

tree structure where the head node is the smallest (min heap), this feature is recursive - so for a sub node, all nodes under it are bigger than it as well.

peak at minimum - o(1)
remove min - o(logn)
insertion - o(logn)
heapify - o(n)

# binary search tree
need to remember that a binary search tree is not garenteed to be balanced.

search - o(n) - worst - it will be the heigt of the tree
insert - o(n) - worst - it will be the heigt of the tree
delete - o(n) - worst - it will be the heigt of the tree

# AVL / height balanced tree

search - o(logn)
insert - o(logn)
delete - o(logn)


# AVL / height balanced tree

search - o(logn)

# Dijkstra's shortest path algorithm
not really a ds but an algorithm for finding shortest paths 
o(v2) but with priority queue it drops to o)v + elogv