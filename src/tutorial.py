from graph import *

edges = [
    (1, 2), (1, 3), (1, 5), 
    (2, 4), (2, 6), (3, 7), 
    (3, 8), (4, 9), (4, 10), 
    (5, 6), (6, 7), (7, 10), 
    (8, 9), (9, 10), (2, 7),
    (5, 9), (3, 6)
]

G = create_graph(edges)


print(f'degree of node : {get_degree(G, 1)}')

print(f'dfs traversal : {dfs_traversal(G, 1)}')

# BFS Traversal
print(f'bfs traversal : {bfs_traversal(G, 1)}')

# Shortest path
print(f'shortest path : {find_shortest_path(G, 1, 4)}')

# Visualize
visualize_graph(G)
