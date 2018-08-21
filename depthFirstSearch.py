# Example graph
graph = {'A': {'B', 'C'},
         'B': {'A', 'D', 'E'},
         'C': {'A', 'F'},
         'D': {'B'},
         'E': {'B', 'F'},
         'F': {'C', 'E'}}


# Depth-first search of a given graph
# If end is specified, returns visited nodes
#    and number of nodes traversed
# If end is NOT specified or found, returns visited nodes and -1
def dfs(g, start, end=None):
    visited, stack = set(), [start]
    path = list()
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            stack.extend(g[vertex] - visited)
        if vertex == end:
            return path, len(visited)
    return path, -1


print(dfs(graph, 'A', 'F'))  # 3 to 5
print(dfs(graph, 'F'))  # -1
print(dfs(graph, 'F', '2'))  # -1
print(dfs(graph, 'D', 'B'))  # 2
