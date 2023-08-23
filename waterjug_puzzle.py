import time
from collections import deque
import heapq


print("Breadth-First Search")

start_time = time.time()

def water_jug_bfs(capacity_a, capacity_b, target):
    visited = set()
    queue = deque([(0, 0)])
    
    while queue:
        state = queue.popleft()
        a, b = state
        
        if state == target:
            print(target)
            return True
        
        visited.add(state)
        print(state)
        
        # Fill jug A
        if (capacity_a, b) not in visited:
            queue.append((capacity_a, b))
        
        # Fill jug B
        if (a, capacity_b) not in visited:
            queue.append((a, capacity_b))
        
        # Empty jug A
        if (0, b) not in visited:
            queue.append((0, b))
        
        # Empty jug B
        if (a, 0) not in visited:
            queue.append((a, 0))
        
        # Pour from A to B
        pour = min(a, capacity_b - b)
        if (a - pour, b + pour) not in visited:
            queue.append((a - pour, b + pour))
        
        # Pour from B to A
        pour = min(b, capacity_a - a)
        if (a + pour, b - pour) not in visited:
            queue.append((a + pour, b - pour))
    
    return False


# Example usage
capacity_a = 4
capacity_b = 3
target = (2, 0)

print("BFS Result:", water_jug_bfs(capacity_a, capacity_b, target))



end_time = time.time()

execution_time = end_time - start_time
print("Execution Time:", execution_time, "seconds")



print("\nDepth-First Search")
start_time = time.time()


def water_jug_dfs(capacity_a, capacity_b, target):
    visited = set()
    stack = [(0, 0)]
    
    while stack:
        state = stack.pop()
        a, b = state
        
        if state == target:
            print(target)
            return True
        
        visited.add(state)
        print(state)
        
        # Pour from A to B
        pour = min(a, capacity_b - b)
        if (a - pour, b + pour) not in visited:
            stack.append((a - pour, b + pour))
        
        # Pour from B to A
        pour = min(b, capacity_a - a)
        if (a + pour, b - pour) not in visited:
            stack.append((a + pour, b - pour))
        
        # Empty jug A
        if (0, b) not in visited:
            stack.append((0, b))
        
        # Empty jug B
        if (a, 0) not in visited:
            stack.append((a, 0))
        
        # Fill jug A
        if (capacity_a, b) not in visited:
            stack.append((capacity_a, b))
        
        # Fill jug B
        if (a, capacity_b) not in visited:
            stack.append((a, capacity_b))
    
    return False


    # Example usage
capacity_a = 4
capacity_b = 3
target = (2, 0)

print("DFS Result:", water_jug_dfs(capacity_a, capacity_b, target))



end_time = time.time()

execution_time = end_time - start_time
print("Execution Time:", execution_time, "seconds")



print("A* Search")

def water_jug_astar(capacity_a, capacity_b, target):
    def heuristic(state):
        return abs(state[0] - target[0]) + abs(state[1] - target[1])
    
    visited = set()
    open_set = [(heuristic((0, 0)), 0, (0, 0))]  # (f-value, g-value, state)
    
    while open_set:
        _, g, state = heapq.heappop(open_set)
        a, b = state
        
        if state == target:
            print(target)
            return True
        
        visited.add(state)
        print(state)
        
        # Fill jug A
        if (capacity_a, b) not in visited:
            heapq.heappush(open_set, (heuristic((capacity_a, b)) + g + 1, g + 1, (capacity_a, b)))
        
        # Fill jug B
        if (a, capacity_b) not in visited:
            heapq.heappush(open_set, (heuristic((a, capacity_b)) + g + 1, g + 1, (a, capacity_b)))
        
        # Empty jug A
        if (0, b) not in visited:
            heapq.heappush(open_set, (heuristic((0, b)) + g + 1, g + 1, (0, b)))
        
        # Empty jug B
        if (a, 0) not in visited:
            heapq.heappush(open_set, (heuristic((a, 0)) + g + 1, g + 1, (a, 0)))
        
        # Pour from A to B
        pour = min(a, capacity_b - b)
        if (a - pour, b + pour) not in visited:
            heapq.heappush(open_set, (heuristic((a - pour, b + pour)) + g + 1, g + 1, (a - pour, b + pour)))
        
        # Pour from B to A
        pour = min(b, capacity_a - a)
        if (a + pour, b - pour) not in visited:
            heapq.heappush(open_set, (heuristic((a + pour, b - pour)) + g + 1, g + 1, (a + pour, b - pour)))
    
    return False


# Example usage
capacity_a = 4
capacity_b = 3
target = (2, 0)

start_time = time.time()
print("A* Result:", water_jug_astar(capacity_a, capacity_b, target))
end_time = time.time()

execution_time = end_time - start_time
print("Execution Time:", execution_time, "seconds")




print("\nHill Climbing")

def water_jug_hill_climbing(capacity_a, capacity_b, target):
    def heuristic(state):
        return abs(state[0] - target[0]) + abs(state[1] - target[1])
    
    current_state = (0, 0)
    current_heuristic = heuristic(current_state)
    
    while current_state != target:
        neighbors = [
            (capacity_a, current_state[1]),
            (current_state[0], capacity_b),
            (0, current_state[1]),
            (current_state[0], 0),
            (min(current_state[0] + current_state[1], capacity_a), max(0, current_state[1] - (capacity_a - current_state[0]))),
            (max(0, current_state[0] - (capacity_b - current_state[1])), min(current_state[1] + current_state[0], capacity_b))
        ]
        
        best_neighbor = min(neighbors, key=heuristic)
        
        if heuristic(best_neighbor) >= current_heuristic:
            break
        
        current_state = best_neighbor
        current_heuristic = heuristic(current_state)
        print(current_state)
    
    return current_state == target

# Example usage
capacity_a = 4
capacity_b = 3
target = (2, 0)

start_time = time.time()
print("Hill Climbing Result:", water_jug_hill_climbing(capacity_a, capacity_b, target))
end_time = time.time()

execution_time = end_time - start_time
print("Execution Time:", execution_time, "seconds")

