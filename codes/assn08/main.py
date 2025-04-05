import heapq
from collections import deque

def check_winner(board):
    for line in board + list(map(list, zip(*board))) + [[board[i][i] for i in range(3)], [board[i][2-i] for i in range(3)]]:
        if line == ['X'] * 3: return 'X'
        if line == ['O'] * 3: return 'O'
    return None

def get_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def bfs(board, player):
    queue = deque([(board, [])])
    while queue:
        state, path = queue.popleft()
        if check_winner(state): return path
        for i, j in get_moves(state):
            new_state = [row[:] for row in state]
            new_state[i][j] = player
            queue.append((new_state, path + [(i, j)]))

def dfs(board, player):
    stack = [(board, [])]
    while stack:
        state, path = stack.pop()
        if check_winner(state): return path
        for i, j in get_moves(state):
            new_state = [row[:] for row in state]
            new_state[i][j] = player
            stack.append((new_state, path + [(i, j)]))

def heuristic(board, player):
    return sum(row.count(player) for row in board)

def a_star(board, player):
    heap = [(0, board, [])]
    while heap:
        _, state, path = heapq.heappop(heap)
        if check_winner(state): return path
        for i, j in get_moves(state):
            new_state = [row[:] for row in state]
            new_state[i][j] = player
            heapq.heappush(heap, (len(path) + heuristic(new_state, player), new_state, path + [(i, j)]))

def print_board(board):
    print("\n  0   1   2")
    print("  ┌───┬───┬───┐")
    for i, row in enumerate(board):
        print(f"{i} │ {' │ '.join(row)} │")
        if i < 2:
            print("  ├───┼───┼───┤")
    print("  └───┴───┴───┘\n")

def player_move(board):
    while True:
        try:
            move = tuple(map(int, input("Enter your move (row col): ").split()))
            if move in get_moves(board):
                return move
            print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter row and column numbers.")

def best_move(board, player):
    opponent = 'X' if player == 'O' else 'O'
    for move in get_moves(board):
        board[move[0]][move[1]] = player
        if check_winner(board) == player:
            board[move[0]][move[1]] = ' '
            return move
        board[move[0]][move[1]] = ' '
    for move in get_moves(board):
        board[move[0]][move[1]] = opponent
        if check_winner(board) == opponent:
            board[move[0]][move[1]] = ' '
            return move
        board[move[0]][move[1]] = ' '
    return get_moves(board)[0]

def play_game():
    board = [[' ']*3 for _ in range(3)]
    print_board(board)
    for turn in range(9):
        if turn % 2 == 0:
            move = player_move(board)
        else:
            move = best_move(board, 'O')
        board[move[0]][move[1]] = 'X' if turn % 2 == 0 else 'O'
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            return
    print("It's a draw!")

print("Comparing Search Strategies:")
board = [[' ']*3 for _ in range(3)]
print("BFS Path:", bfs(board, 'X'))
print("DFS Path:", dfs(board, 'X'))
print("A* Path:", a_star(board, 'X'))

play_game()
