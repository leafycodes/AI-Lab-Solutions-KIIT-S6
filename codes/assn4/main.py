def uniform_cost_search(graph, start, goal):
    frontier = [(0, start, [start])]
    visited = set()

    while frontier:
        frontier.sort()
        cost, node, path = frontier.pop(0)
        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return cost, path

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                frontier.append((cost + weight, neighbor, path + [neighbor]))

    return float("inf"), []

def bfs(graph, start, goal):
    queue = [(start, [start])]
    visited = set()

    while queue:
        node, path = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path

        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return []

graph = {
    "Delhi": [("Jaipur", 71), ("Kota", 151)],
    "Jaipur": [("Delhi", 71), ("Jodhpur", 75), ("Kota", 140)],
    "Jodhpur": [("Jaipur", 75), ("Ahmedabad", 118), ("Kota", 140)],
    "Ahmedabad": [("Jodhpur", 118), ("Nasik", 111)],
    "Nasik": [("Ahmedabad", 111), ("Mumbai", 70),],
    "Mumbai": [("Nasik", 70), ("Pune", 75)],
    "Pune": [("Mumbai", 75), ("Solapur", 120)],
    "Solapur": [("Pune", 120), ("Bhopal", 146), ("Amravati", 138),],
    "Kota": [("Delhi", 151), ("Jodhpur", 140), ("Jhansi", 99), ("Bhopal", 80)],
    "Jhansi": [("Kota", 99), ("Hyderabad", 211)],
    "Bhopal": [("Kota", 80), ("Solapur", 146), ("Amravati", 97)],
    "Amravati": [("Bhopal", 97), ("Solapur", 138), ("Hyderabad", 101)],
    "Hyderabad": [("Amravati", 101), ("Jhansi", 211), ("Kurnool", 90), ("Warangal", 85)],
    "Kurnool": [("Hyderabad", 90)],
    "Warangal": [("Hyderabad", 85), ("Visakapatnam", 98)],
    "Visakapatnam": [("Warangal", 98), ("Vijayawada", 86)],
    "Vijayawada": [("Visakapatnam", 86)],
    "Bhilai": [("Raipur", 92), ("Warangal", 142)],
    "Raipur": [("Bilaspur", 87), ("Bhilai", 92)],
    "Bilaspur": [("Raipur", 87)],
}

start, goal = "Delhi", "Vijayawada"

ucs_cost, ucs_path = uniform_cost_search(graph, start, goal)
print("Uniform Cost Search:")
print(f"Cost: {ucs_cost}")
print(f"Path: {' -> '.join(ucs_path)}")

bfs_path = bfs(graph, start, goal)
print("\nBreadth-First Search:")
print(f"Path: {' -> '.join(bfs_path)}")