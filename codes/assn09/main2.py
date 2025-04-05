import heapq
import time
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

class Pathfinding:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    def is_valid(self, node):
        x, y = node
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] == 0
    
    def reconstruct_path(self, came_from, current):
        path = []
        while current:
            path.append(current)
            current = came_from.get(current)
        return path[::-1]
    
    def bfs(self):
        start_time = time.time()
        queue = deque([self.start])
        came_from = {self.start: None}
        nodes_explored = 0
        
        while queue:
            current = queue.popleft()
            nodes_explored += 1
            if current == self.goal:
                return self.reconstruct_path(came_from, current), nodes_explored, time.time() - start_time
            
            for dx, dy in self.directions:
                neighbor = (current[0] + dx, current[1] + dy)
                if self.is_valid(neighbor) and neighbor not in came_from:
                    queue.append(neighbor)
                    came_from[neighbor] = current
        
        return None, nodes_explored, time.time() - start_time
    
    def dfs(self):
        start_time = time.time()
        stack = [self.start]
        came_from = {self.start: None}
        nodes_explored = 0
        
        while stack:
            current = stack.pop()
            nodes_explored += 1
            if current == self.goal:
                return self.reconstruct_path(came_from, current), nodes_explored, time.time() - start_time
            
            for dx, dy in self.directions:
                neighbor = (current[0] + dx, current[1] + dy)
                if self.is_valid(neighbor) and neighbor not in came_from:
                    stack.append(neighbor)
                    came_from[neighbor] = current
        
        return None, nodes_explored, time.time() - start_time
    
    def a_star(self):
        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        start_time = time.time()
        open_set = [(0, self.start)]
        came_from = {self.start: None}
        g_score = {self.start: 0}
        nodes_explored = 0
        
        while open_set:
            _, current = heapq.heappop(open_set)
            nodes_explored += 1
            if current == self.goal:
                return self.reconstruct_path(came_from, current), nodes_explored, time.time() - start_time
            
            for dx, dy in self.directions:
                neighbor = (current[0] + dx, current[1] + dy)
                if self.is_valid(neighbor):
                    tentative_g_score = g_score[current] + 1
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        g_score[neighbor] = tentative_g_score
                        f_score = tentative_g_score + heuristic(neighbor, self.goal)
                        heapq.heappush(open_set, (f_score, neighbor))
                        came_from[neighbor] = current
        
        return None, nodes_explored, time.time() - start_time

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    goal = (4, 4)
    
    pathfinder = Pathfinding(grid, start, goal)
    bfs_result = pathfinder.bfs()
    dfs_result = pathfinder.dfs()
    a_star_result = pathfinder.a_star()
    
    print("BFS:", bfs_result)
    print("DFS:", dfs_result)
    print("A*:", a_star_result)