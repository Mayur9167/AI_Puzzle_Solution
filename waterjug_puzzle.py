import time
from collections import deque



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