from queue import PriorityQueue
from queue import Queue
import heapq

class RoboCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.position = (0, 0)
        
    def is_valid(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] != 'X'
    
    def bfs(self):
        visited = set()
        queue = Queue()
        queue.put(self.position)
        
        while not queue.empty():
            row, col = queue.get()
            if (row, col) in visited:
                continue
            
            visited.add((row, col))
            print(f"Cleaning tile at ({row}, {col})")
            
            for dr, dc in self.directions:
                new_row, new_col = row + dr, col + dc
                if self.is_valid(new_row, new_col):
                    queue.put((new_row, new_col))
    
    def dfs(self):
        visited = set()
        stack = [self.position]
        
        while stack:
            row, col = stack.pop()
            if (row, col) in visited:
                continue
            
            visited.add((row, col))
            print(f"Cleaning tile at ({row}, {col})")
            
            for dr, dc in self.directions:
                new_row, new_col = row + dr, col + dc
                if self.is_valid(new_row, new_col):
                    stack.append((new_row, new_col))
    
    def a_star(self):
        start = self.position
        goal = (self.rows - 1, self.cols - 1)
        
        def heuristic(node):
            return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
        
        visited = set()
        open_list = PriorityQueue()
        open_list.put((0, start))
        
        while not open_list.empty():
            cost, (row, col) = open_list.get()
            if (row, col) in visited:
                continue
            
            visited.add((row, col))
            print(f"Cleaning tile at ({row}, {col})")
            
            if (row, col) == goal:
                break
            
            for dr, dc in self.directions:
                new_row, new_col = row + dr, col + dc
                if self.is_valid(new_row, new_col):
                    new_cost = cost + 1 + heuristic((new_row, new_col))
                    open_list.put((new_cost, (new_row, new_col)))

    def hill_climbing(self):
        current_node = self.position
        while True:
            neighbors = []
            
            for dr, dc in self.directions:
                new_row, new_col = current_node[0] + dr, current_node[1] + dc
                if self.is_valid(new_row, new_col):
                    neighbors.append((new_row, new_col))
            
            best_neighbor = min(neighbors, key=lambda n: self.heuristic(n))
            
            if self.heuristic(best_neighbor) >= self.heuristic(current_node):
                break
            
            print(f"Cleaning tile at {best_neighbor}")
            current_node = best_neighbor
    
    def heuristic(self, node):
        goal = (self.rows - 1, self.cols - 1)
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    
    def print_grid(self):
        for row in self.grid:
            print(" ".join(row))


# Example grid layout (replace it with your own):
grid = [
    ['0', '0', 'X', '0', 'X'],
    ['0', 'X', '0', '0', '0'],
    ['0', '0', '0', 'X', '0'],
    ['X', '0', 'X', '0', '0'],
    ['0', '0', '0', '0', 'X']
]

robo_cleaner = RoboCleaner(grid)
print("Original grid:")
robo_cleaner.print_grid()

print("\nStarting BFS cleaning:")
robo_cleaner.bfs()

print("\nStarting DFS cleaning:")
robo_cleaner.dfs()

# Call A* cleaning
print("\nStarting A* cleaning:")
robo_cleaner.a_star()

# Call Hill Climbing cleaning
print("\nStarting Hill Climbing cleaning:")
robo_cleaner.hill_climbing()

print("\nGrid after cleaning:")
robo_cleaner.print_grid()



