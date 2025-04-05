import heapq

GOAL_STATE = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

def misplaced_tiles(state):
    return sum(1 for i in range(3) for j in range(3) if state[i][j] and state[i][j] != GOAL_STATE[i][j])

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_row, goal_col = divmod(state[i][j] - 1, 3)
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance

def get_neighbors(state):
    neighbors = []
    zero_row, zero_col = next((r, c) for r in range(3) for c in range(3) if state[r][c] == 0)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in moves:
        new_row, new_col = zero_row + dr, zero_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [list(row) for row in state]
            new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]
            neighbors.append(tuple(tuple(row) for row in new_state))
    
    return neighbors

def a_star_search(initial_state, heuristic):
    open_list = []
    heapq.heappush(open_list, (heuristic(initial_state), 0, initial_state, []))
    closed_set = set()
    
    while open_list:
        _, g, current_state, path = heapq.heappop(open_list)
        
        if current_state == GOAL_STATE:
            return path + [current_state], len(closed_set)
        
        if current_state in closed_set:
            continue
        
        closed_set.add(current_state)
        
        for neighbor in get_neighbors(current_state):
            if neighbor not in closed_set:
                heapq.heappush(open_list, (g + 1 + heuristic(neighbor), g + 1, neighbor, path + [current_state]))
    
    return None, len(closed_set)

initial_state = ((1, 2, 3), (5, 6, 0), (7, 8, 4))

solution_misplaced, nodes_explored_misplaced = a_star_search(initial_state, misplaced_tiles)
print("Solution using Misplaced Tiles:", solution_misplaced)
print("Nodes explored using Misplaced Tiles:", nodes_explored_misplaced)
print("Solution depth using Misplaced Tiles:", len(solution_misplaced) - 1)

solution_manhattan, nodes_explored_manhattan = a_star_search(initial_state, manhattan_distance)
print("Solution using Manhattan Distance:", solution_manhattan)
print("Nodes explored using Manhattan Distance:", nodes_explored_manhattan)
print("Solution depth using Manhattan Distance:", len(solution_manhattan) - 1)