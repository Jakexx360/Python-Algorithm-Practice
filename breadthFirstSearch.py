# Breath-First search provides us with the ability to return the same results as DFS
# but with the added guarantee to return the shortest-path first
# - Mark the current vertex as being visited.
# - Explore each adjacent vertex that is not included in the visited set

# Example graph
graph = {'A': {'B', 'C'},
         'B': {'A', 'D', 'E'},
         'C': {'A', 'F'},
         'D': {'B'},
         'E': {'B', 'F'},
         'F': {'C', 'E'}}


# Iterative breadth-first search of a given graph O(n*log(n))
# If end is specified, returns shortest path and number of nodes traversed
# If end is NOT specified or found, returns empty path and -1
def bfs(g, start, end=None):
    queue = [(start, [start])]
    while queue:  # O(n)
        (vertex, path) = queue.pop(0)
        # Remove visited nodes from the vertex set
        # and extend the stack to explore with the remaining set
        for next_vertex in g[vertex] - set(path):  # O(log(n))
            # If we reached the goal, return shortest path and its length
            if next_vertex == end:
                path = path + [next_vertex]
                return path, len(path)
            else:
                queue.append((next_vertex, path + [next_vertex]))
    return [], -1


print(bfs(graph, "A", "F") == (['A', 'C', 'F'], 3))  # True
print(bfs(graph, "A", "D") == (['A', 'B', 'D'], 3))  # True
print(bfs(graph, "F", "D") == (['F', 'E', 'B', 'D'], 4))  # True
print(bfs(graph, "D", "B") == (['D', 'B'], 2))  # True
print(bfs(graph, "D") == ([], -1))  # True
