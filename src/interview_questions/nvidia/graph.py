class Graph:
    def __init__(self) -> None:
        self.adjacency_list = {}

    def get_vertex_targets(self, vertex):
        return self.adjacency_list.get(vertex)

    def add_vertex(self, val):
        self.adjacency_list[val] = []

    def add_edge(self, source, target):
        if target not in self.adjacency_list[source]:
            self.adjacency_list[source].append(target)


g = Graph()

g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')
g.add_vertex('e')

g.add_edge('a', 'b')
g.add_edge('a', 'c')
g.add_edge('c', 'b')
g.add_edge('b', 'e')
g.add_edge('c', 'd')
g.add_edge('e', 'a')


def bfs_inner(graph, elements, visited, return_arr):
    next = []
    for element in elements:
        if visited.get(element) is None:
            visited[element] = True
            return_arr.append(element)
            targets = graph.get_vertex_targets(element)
            next.extend(targets)

    if len(next) > 0:
        bfs_inner(graph, next, visited, return_arr)
    return return_arr


def bfs(graph, start_node):
    arr = bfs_inner(graph, [start_node], {}, [])
    print(arr)  # for debugging
    return arr


assert bfs(g, 'a') == ['a', 'b', 'c', 'e', 'd']
assert bfs(g, 'b') == ['b', 'e', 'a', 'c', 'd']
assert bfs(g, 'c') == ['c', 'b', 'd', 'e', 'a']
assert bfs(g, 'e') == ['e', 'a', 'b', 'c', 'd']
assert bfs(g, 'd') == ['d']


def dfs_inner(graph, start_node, visited, return_arr):
    if visited.get(start_node) is None:
        visited[start_node] = True
        return_arr.append(start_node)

        for node in graph.get_vertex_targets(start_node):
            dfs_inner(graph, node, visited, return_arr)

    return return_arr


def dfs(graph, start_node):
    arr = dfs_inner(graph, start_node, {}, [])
    print(arr)
    return arr


assert dfs(g, 'a') == ['a', 'b', 'e', 'c', 'd']
assert dfs(g, 'b') == ['b', 'e', 'a', 'c', 'd']
assert dfs(g, 'c') == ['c', 'b', 'e', 'a', 'd']
assert dfs(g, 'e') == ['e', 'a', 'b', 'c', 'd']
assert dfs(g, 'd') == ['d']
