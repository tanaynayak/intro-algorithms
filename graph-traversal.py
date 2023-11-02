# Graph represented as adjacency list
adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'E'],
    'D': ['B', 'C'],
    'E': ['C']
}

# Graph represented as adjacency matrix
adj_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0]
]

vertices = ['A', 'B', 'C', 'D', 'E']

# DFS using adjacency list
def dfs_list(graph, node, visited=[]):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs_list(graph, neighbour, visited)
    return visited

print("DFS using Adjacency List:")
dfs_list(adj_list, 'A')
print("\n")

# BFS using adjacency list
def bfs_list(graph, start):
    visited, queue = [], [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            queue.extend([n for n in graph[node] if n not in visited])

print("BFS using Adjacency List:")
bfs_list(adj_list, 'A')
print("\n")

# DFS using adjacency matrix
def dfs_matrix(matrix, node, visited=[]):
    if node not in visited:
        print(vertices[node], end=" ")
        visited.append(node)
        for index, value in enumerate(matrix[node]):
            if value == 1 and index not in visited:
                dfs_matrix(matrix, index, visited)
    return visited

print("DFS using Adjacency Matrix:")
dfs_matrix(adj_matrix, 0)
print("\n")

# BFS using adjacency matrix
def bfs_matrix(matrix, start):
    visited, queue = [], [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(vertices[node], end=" ")
            visited.append(node)
            neighbours = [i for i, value in enumerate(matrix[node]) if value == 1 and i not in visited]
            queue.extend(neighbours)

print("BFS using Adjacency Matrix:")
bfs_matrix(adj_matrix, 0)
print("\n")
