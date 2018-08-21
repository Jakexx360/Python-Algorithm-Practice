# Explores possible vertices (from a supplied root) down each branch before backtracking
# - Mark the current vertex as being visited.
# - Explore each adjacent vertex that is not included in the visited set

# Example graph
graph = {'A': {'B', 'C'},
         'B': {'A', 'D', 'E'},
         'C': {'A', 'F'},
         'D': {'B'},
         'E': {'B', 'F'},
         'F': {'C', 'E'}}


# Iterative depth-first search of a given graph
# If end is specified, returns visited nodes in order
#    and number of nodes traversed
# If end is NOT specified or found, returns visited nodes in order and -1
def dfs_iterative(g, start, end=None):
    visited, stack = set(), [start]
    path = list()
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            # Remove visited nodes from the vertex set
            # and extend the stack to explore with the remaining set
            stack.extend(g[vertex] - visited)
        # If we found the desired vertex, return
        if vertex == end:
            return path, len(visited)
    return path, -1


# Recursive depth-first search of a given graph
# Returns all visited nodes
def dfs_recursive(g, start, visited=None):
    # Recreate default argument
    if visited is None:
        visited = set()
    visited.add(start)
    # Remove visited nodes from the vertex set
    for next_node in g[start] - visited:
        # Explore the remaining set
        dfs_recursive(g, next_node, visited)
    return visited


print(dfs_iterative(graph, 'A', 'F'))  # 3 to 5
print(dfs_iterative(graph, 'F'))  # -1
print(dfs_iterative(graph, 'F', '2'))  # -1
print(dfs_iterative(graph, 'D', 'B'))  # 2
print(dfs_recursive(graph, 'A') == dfs_recursive(graph, 'F'))  # True
