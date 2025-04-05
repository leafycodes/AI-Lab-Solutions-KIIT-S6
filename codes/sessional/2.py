from collections import deque

def bfs(graph, start, end):
    queue = deque([(start, [start], 0)])
    visited = set()
    visited.add(start)

    while queue:
        node, path, cost = queue.popleft()

        if node == end:
            return path, cost, len(visited)

        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor], cost + weight))
                visited.add(neighbor)

    return None, float('inf'), len(visited)

graph = {
    'A': [('B', 8), ('F', 3)],
    'B': [('A', 8), ('C', 2), ('D', 1)],
    'C': [('B', 2), ('E', 5)],
    'D': [('B', 1), ('E', 8), ('I', 5)],
    'E': [('C', 5), ('D', 8), ('J', 5)],
    'F': [('A', 3), ('G', 6)],
    'G': [('F', 6), ('H', 7)],
    'H': [('G', 7), ('I', 2)],
    'I': [('D', 5), ('H', 2), ('J', 3)],
    'J': [('E', 5), ('I', 3)]
}

start = 'A'  
end = 'J'  

bfs_path, bfs_cost, bfs_explored = bfs(graph, start, end)

print("BFS Path:", bfs_path)
print("Total Path Cost:", bfs_cost)
print("BFS Nodes Explored:", bfs_explored)
