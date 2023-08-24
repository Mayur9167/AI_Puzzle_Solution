from collections import deque
import heapq


# Function to print a state in matrix format
def print_state_matrix(state):
    for row in state:
        print(row)
    print()

# Function to print solutions in matrix format
def print_solution_matrix(solution):
    for i in range(0, len(solution), 3):
        for j in range(3):
            if i + j < len(solution):
                print_state_matrix(solution[i + j])
        print()


# Helper function to swap tiles
def swap_tiles(state, i1, j1, i2, j2):
    new_state = [row[:] for row in state]
    new_state[i1][j1], new_state[i2][j2] = new_state[i2][j2], new_state[i1][j1]
    return new_state

# Check if the state is the goal state
def is_goal(state, goal_state):
    return state == goal_state

# Generate all possible successor states
def generate_successors(state):
    successors = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                empty_row, empty_col = i, j

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    for move in moves:
        new_row, new_col = empty_row + move[0], empty_col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = swap_tiles(state, empty_row, empty_col, new_row, new_col)
            successors.append(new_state)

    return successors

# Breadth-First Search
def bfs(initial_state, goal_state):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        visited.add(tuple(map(tuple, current_state)))

        if is_goal(current_state, goal_state):
            return path

        successors = generate_successors(current_state)
        for successor in successors:
            if tuple(map(tuple, successor)) not in visited:
                queue.append((successor, path + [successor]))

    return None

# Depth-First Search
def dfs(initial_state, goal_state, depth_limit=10):
    stack = [(initial_state, [])]
    visited = set()

    while stack:
        current_state, path = stack.pop()
        visited.add(tuple(map(tuple, current_state)))

        if is_goal(current_state, goal_state):
            return path

        if len(path) < depth_limit:
            successors = generate_successors(current_state)
            for successor in successors:
                if tuple(map(tuple, successor)) not in visited:
                    stack.append((successor, path + [successor]))

    return None




# Helper function to calculate the Manhattan distance heuristic
def manhattan_distance(state, goal_state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_i, goal_j = divmod(value - 1, 3)
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

# A* Search
def astar(initial_state, goal_state):
    open_list = [(manhattan_distance(initial_state, goal_state), initial_state, [])]
    visited = set()

    while open_list:
        _, current_state, path = heapq.heappop(open_list)
        visited.add(tuple(map(tuple, current_state)))

        if is_goal(current_state, goal_state):
            return path

        successors = generate_successors(current_state)
        for successor in successors:
            if tuple(map(tuple, successor)) not in visited:
                heapq.heappush(open_list, (len(path) + manhattan_distance(successor, goal_state), successor, path + [successor]))

    return None

# Hill Climbing
def hill_climbing(initial_state, goal_state, max_iterations=1000):
    current_state = initial_state
    for _ in range(max_iterations):
        successors = generate_successors(current_state)
        best_successor = min(successors, key=lambda successor: manhattan_distance(successor, goal_state))

        if manhattan_distance(best_successor, goal_state) >= manhattan_distance(current_state, goal_state):
            return None

        if is_goal(best_successor, goal_state):
            return [initial_state] + [best_successor]

        current_state = best_successor

    return None

# Example puzzle and goal state
initial_state = [
    [7, 2, 4],
    [5, 0, 6],
    [8, 3, 1]
]


goal_state = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]


# Solve using BFS
bfs_solution = bfs(initial_state, goal_state)
print("BFS Solution:")
if bfs_solution:
    for step in bfs_solution:
        print(step)
else:
    print("No solution found.")

print()

# Solve using DFS
dfs_solution = dfs(initial_state, goal_state)
print("\nDFS Solution:")
if dfs_solution:
    for step in dfs_solution:
        print(step)
else:
    print("No solution found.")

# Solve using A*
astar_solution = astar(initial_state, goal_state)
print("\nA* Solution:")
if astar_solution:
    print_solution_matrix(astar_solution)
else:
    print("No solution found.")

print()

# Solve using Hill Climbing
hillclimb_solution = hill_climbing(initial_state, goal_state)
print("Hill Climbing Solution:")
if hillclimb_solution:
    print_solution_matrix(hillclimb_solution)
else:
    print("No solution found.")