def bfs(maze, start, end):
    queue = [(start, [start])]
    visited = set()
    visited.add(start)

    while queue:
        current_position, path = queue.pop(0)
        x, y = current_position

        if (x, y) == end:
            return path, len(visited)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 1 and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))

    return None, len(visited)

def dfs(maze, start, end):
    stack = [(start, [start])]
    visited = set()
    visited.add(start)

    while stack:
        current_position, path = stack.pop()
        x, y = current_position

        if (x, y) == end:
            return path, len(visited)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 1 and (nx, ny) not in visited:
                stack.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))

    return None, len(visited)

if __name__ == "__main__":
    maze = [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1],
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
