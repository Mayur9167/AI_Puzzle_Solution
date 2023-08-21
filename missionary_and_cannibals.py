# ... (import statements and utility functions)
from collections import deque
import heapq
import random


def is_valid(state):
    missionaries_left, cannibals_left, boat_left, missionaries_right, cannibals_right = state
    if missionaries_left < 0 or cannibals_left < 0 or missionaries_right < 0 or cannibals_right < 0:
        return False
    if missionaries_left > 3 or cannibals_left > 3 or missionaries_right > 3 or cannibals_right > 3:
        return False
    if (missionaries_left < cannibals_left and missionaries_left > 0) or \
       (missionaries_right < cannibals_right and missionaries_right > 0):
        return False
    return True

def move(state, m, c):
    missionaries_left, cannibals_left, boat_left, missionaries_right, cannibals_right = state
    if boat_left:
        new_state = (missionaries_left - m, cannibals_left - c, not boat_left,
                     missionaries_right + m, cannibals_right + c)
    else:
        new_state = (missionaries_left + m, cannibals_left + c, not boat_left,
                     missionaries_right - m, cannibals_right - c)
    
    if is_valid(new_state):
        return new_state
    return None



# Utility function to print a state
def print_state(state):
    missionaries_left, cannibals_left, boat_left, missionaries_right, cannibals_right = state
    print(f"ML: {missionaries_left} CL: {cannibals_left} | Boat: {'←' if boat_left else '→'} | MR: {missionaries_right} CR: {cannibals_right}")


# Encode arrow characters as Unicode escape sequences
arrow_left = '\u2192'
arrow_right = '\u2190'


# Breadth-First Search (BFS) algorithm
def bfs():
    start_state = (3, 3, True, 0, 0)
    visited = set()
    queue = deque([(start_state, [])])

    while queue:
        state, path = queue.popleft()
        visited.add(state)
        
        if state == (0, 0, False, 3, 3):
            return path
        
        for m, c in [(0, 1), (1, 0), (1, 1), (2, 0), (0, 2)]:
            new_state = move(state, m, c)
            if new_state and new_state not in visited:
                new_path = path + [(m, c, "←" if state[2] else "→")]
                queue.append((new_state, new_path))

    return None


# Depth-First Search (DFS) algorithm
def dfs(state, path, visited):
    if state == (0, 0, False, 3, 3):
        return path

    visited.add(state)
    
    for m, c in [(0, 1), (1, 0), (1, 1), (2, 0), (0, 2)]:
        new_state = move(state, m, c)
        if new_state and new_state not in visited:
            new_path = path + [(m, c, "←" if state[2] else "→")]
            result = dfs(new_state, new_path, visited)
            if result:
                return result

    return None


# Heuristic function for A* algorithm
def heuristic(state):
    missionaries_left, cannibals_left, _, missionaries_right, cannibals_right = state
    return missionaries_left + cannibals_left - missionaries_right - cannibals_right

# A* algorithm
def solve_n_queens_a_star():
    start_state = (3, 3, True, 0, 0)
    priority_queue = [(heuristic(start_state), start_state, [])]

    while priority_queue:
        _, state, path = heapq.heappop(priority_queue)
        
        if state == (0, 0, False, 3, 3):
            return path
        
        for m, c in [(0, 1), (1, 0), (1, 1), (2, 0), (0, 2)]:
            new_state = move(state, m, c)
            if new_state:
                new_path = path + [(m, c, "←" if state[2] else "→")]
                heapq.heappush(priority_queue, (heuristic(new_state) + len(new_path), new_state, new_path))

    return None


# Hill Climbing algorithm
def solve_n_queens_hill_climb(max_iterations=1000):
    def random_state():
        return (random.randint(0, 3), random.randint(0, 3), random.choice([True, False]),
                random.randint(0, 3), random.randint(0, 3))

    current_state = random_state()

    for _ in range(max_iterations):
        if current_state == (0, 0, False, 3, 3):
            return []

        best_successor = None
        best_successor_heuristic = float('inf')

        for m, c in [(0, 1), (1, 0), (1, 1), (2, 0), (0, 2)]:
            successor = move(current_state, m, c)
            if successor:
                successor_heuristic = heuristic(successor)
                if successor_heuristic < best_successor_heuristic:
                    best_successor = successor
                    best_successor_heuristic = successor_heuristic

        if best_successor:
            current_state = best_successor
        else:
            break

    return None


def main():
    print("BFS Solution:")
    bfs_path = bfs()
    if bfs_path:
        for action in bfs_path:
            arrow = arrow_left if action[2] == "←" else arrow_right
            encoded_arrow = arrow.encode('utf-8').decode('utf-8', 'ignore')  # Encode and decode to handle console encoding
            print(f"Action: Move {action[0]} missionaries and {action[1]} cannibals {encoded_arrow}")
        print("Solution found!")
    else:
        print("No solution found.")


    print("\nDFS Solution:")
    dfs_path = dfs((3, 3, True, 0, 0), [], set())
    if dfs_path:
        for action in dfs_path:
            arrow = arrow_left if action[2] == "←" else arrow_right
            print(f"Action: Move {action[0]} missionaries and {action[1]} cannibals {arrow}")
        print("Solution found!")
    else:
        print("No solution found.")

    print("\nA* Solution:")
    a_star_path = solve_n_queens_a_star()
    if a_star_path:
        for action in a_star_path:
            arrow = arrow_left if action[2] == "←" else arrow_right
            print(f"Action: Move {action[0]} missionaries and {action[1]} cannibals {arrow}")
        print("Solution found!")
    else:
        print("No solution found.")

    print("\nHill Climbing Solution:")
    hill_climb_solution = solve_n_queens_hill_climb()
    if hill_climb_solution:
        for action in hill_climb_solution:
            arrow = arrow_left if action[2] == "←" else arrow_right
            print(f"Action: Move {action[0]} missionaries and {action[1]} cannibals {arrow}")
        print("Solution found!")
    else:
        print("No solution found.")



if __name__ == "__main__":
    main()