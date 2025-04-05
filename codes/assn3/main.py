from collections import deque

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path, len(visited)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1 and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))

    return None, len(visited)  # No path found

def dfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    stack = [(start, [start])]
    visited = set()
    visited.add(start)

    while stack:
        (x, y), path = stack.pop()

        if (x, y) == end:
            return path, len(visited)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1 and (nx, ny) not in visited:
                stack.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))

    return None, len(visited)  # No path found

if _name_ == "_main_":
    maze = [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    start = (0, 0)
    end = (4, 4)

    bfs_path, bfs_explored = bfs(maze, start, end)
    dfs_path, dfs_explored = dfs(maze, start, end)

    print("BFS Path:", bfs_path)
    print("BFS Nodes Explored:", bfs_explored)
    print("DFS Path:", dfs_path)
    print("DFS Nodes Explored:", dfs_explored)