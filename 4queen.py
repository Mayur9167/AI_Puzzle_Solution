import heapq
import random

def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def print_solution(solution):
    for queen_col in solution:
        line = ["Q" if i == queen_col else "." for i in range(len(solution))]
        print(" ".join(line))
    print()

def solve_n_queens_bfs(n):
    queue = []
    queue.append([])
    iterations = 0

    while queue:
        iterations += 1
        board = queue.pop(0)
        if len(board) == n:
            return board, iterations

        col = len(board)
        for row in range(n):
            if is_safe(board, row, col):
                new_board = board + [row]
                queue.append(new_board)

def solve_n_queens_dfs(n):
    def backtrack(row, board, iterations):
        if row == n:
            return [board[:]], iterations

        solutions = []
        for col in range(n):
            iterations += 1
            if is_safe(board, row, col):
                board[row] = col
                sol, iterations = backtrack(row + 1, board, iterations)
                solutions.extend(sol)
                board[row] = -1

        return solutions, iterations

    board = [-1] * n
    return backtrack(0, board, 0)

def heuristic(board):
    conflicts = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

def solve_n_queens_a_star(n):
    initial_board = [-1] * n
    priority_queue = [(heuristic(initial_board), initial_board)]
    iterations = 0

    while priority_queue:
        iterations += 1
        _, board = heapq.heappop(priority_queue)
        if board.count(-1) == 0:
            return board, iterations

        row = board.index(-1)
        for col in range(n):
            if is_safe(board, row, col):
                new_board = board[:]
                new_board[row] = col
                heapq.heappush(priority_queue, (heuristic(new_board), new_board))

def solve_n_queens_hill_climb(n, max_iterations=1000):
    def random_board():
        return [random.randint(0, n - 1) for _ in range(n)]

    def conflicts(board):
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                    count += 1
        return count

    current_board = random_board()
    current_conflicts = conflicts(current_board)
    iterations = 0

    for _ in range(max_iterations):
        iterations += 1
        if current_conflicts == 0:
            return current_board, iterations

        neighbor_boards = []
        for i in range(n):
            for j in range(n):
                if current_board[i] != j:
                    neighbor_board = current_board[:]
                    neighbor_board[i] = j
                    neighbor_boards.append(neighbor_board)

        random.shuffle(neighbor_boards)
        next_board = min(neighbor_boards, key=lambda board: conflicts(board))
        next_conflicts = conflicts(next_board)

        if next_conflicts >= current_conflicts:
            return current_board, iterations

        current_board = next_board
        current_conflicts = next_conflicts

    return current_board, iterations

n = 4

print("Solutions using BFS:")
bfs_solution, bfs_iterations = solve_n_queens_bfs(n)
print_solution(bfs_solution)
print("BFS Iterations:", bfs_iterations)

print("Solutions using DFS:")
dfs_solutions, dfs_iterations = solve_n_queens_dfs(n)
for solution in dfs_solutions:
    print_solution(solution)
print("DFS Iterations:", dfs_iterations)

print("Solution using A*:")
a_star_solution, a_star_iterations = solve_n_queens_a_star(n)
print_solution(a_star_solution)
print("A* Iterations:", a_star_iterations)

print("Solution using Hill Climbing:")
hill_climb_solution, hill_climb_iterations = solve_n_queens_hill_climb(n)
print_solution(hill_climb_solution)
print("Hill Climbing Iterations:", hill_climb_iterations)
