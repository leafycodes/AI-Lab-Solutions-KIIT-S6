import heapq

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def best_first_search(rows, cols, start, goal):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pq = []
    heapq.heappush(pq, (manhattan_distance(*start, *goal), start))
    
    visited = set()
    parent = {}

    while pq:
        _, (x, y) = heapq.heappop(pq)
        
        if (x, y) == goal:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            return path[::-1]
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                heapq.heappush(pq, (manhattan_distance(nx, ny, *goal), (nx, ny)))
                parent[(nx, ny)] = (x, y)
    
    return None

rows, cols = 6, 6
start = (0, 0)
goal = (5, 5)

path = best_first_search(rows, cols, start, goal)

print("Path to Treasure:", path)