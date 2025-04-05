import heapq
import math

grid = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (5, 5)



def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def a_star_search(grid, start, goal, heuristic):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return None

def bfs_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    queue = [(start, [start])]
    visited = set()

    while queue:
        (current, path) = queue.pop(0)
        if current == goal:
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0 and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

def ucs_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0, start, [start]))
    visited = set()

    while open_set:
        cost, current, path = heapq.heappop(open_set)

        if current == goal:
            return path

        if current in visited:
            continue
        visited.add(current)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                heapq.heappush(open_set, (cost + 1, neighbor, path + [neighbor]))
    return None

path_a_star_manhattan = a_star_search(grid, start, goal, manhattan_distance)
print("A* (Manhattan) Path:", path_a_star_manhattan)

path_a_star_euclidean = a_star_search(grid, start, goal, euclidean_distance)
print("A* (Euclidean) Path:", path_a_star_euclidean)

path_bfs = bfs_search(grid, start, goal)
print("BFS Path:", path_bfs)

path_ucs = ucs_search(grid, start, goal)
print("UCS Path:", path_ucs)
