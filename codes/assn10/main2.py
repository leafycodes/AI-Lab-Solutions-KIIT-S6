import math

def is_valid_state(x, y, A, B):
    return 0 <= x <= A and 0 <= y <= B

def generate_moves(x, y, A, B):
    return [
        (A, y), (x, B), (0, y), (x, 0),
        (max(0, x - (B - y)), min(B, y + x)),  # Pour from A to B
        (min(A, x + y), max(0, y - (A - x)))   # Pour from B to A
    ]

def is_terminal_state(x, y, target):
    return x == target or y == target

def utility(x, y, target, is_ai):
    if is_terminal_state(x, y, target):
        return 1 if is_ai else -1
    return 0

def minimax(x, y, depth, is_ai, alpha, beta, A, B, target):
    if is_terminal_state(x, y, target) or depth == 0:
        return utility(x, y, target, is_ai)

    moves = [(nx, ny) for nx, ny in generate_moves(x, y, A, B) if is_valid_state(nx, ny, A, B)]

    if is_ai:
        max_eval = -math.inf
        for nx, ny in moves:
            eval = minimax(nx, ny, depth-1, False, alpha, beta, A, B, target)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for nx, ny in moves:
            eval = minimax(nx, ny, depth-1, True, alpha, beta, A, B, target)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def best_move(x, y, A, B, target):
    moves = [(nx, ny) for nx, ny in generate_moves(x, y, A, B) if is_valid_state(nx, ny, A, B)]
    best_val = -math.inf
    best_state = None

    for nx, ny in moves:
        move_val = minimax(nx, ny, 6, False, -math.inf, math.inf, A, B, target)
        if move_val > best_val:
            best_val = move_val
            best_state = (nx, ny)
    return best_state

def play_game(A, B, T):
    x, y = 0, 0
    print(f"Initial State: ({x}, {y})")
    is_ai_turn = True

    while True:
        if is_terminal_state(x, y, T):
            print(f"{'AI' if is_ai_turn else 'Human'} wins!")
            break

        if is_ai_turn:
            print("AI is thinking...")
            x, y = best_move(x, y, A, B, T)
        else:
            print("Your Turn. Enter next state (x, y): ")
            try:
                x, y = map(int, input().split())
            except ValueError:
                print("Invalid Input.")
                continue

        if not is_valid_state(x, y, A, B):
            print("Invalid State! Try Again.")
            continue

        print(f"Current State: ({x}, {y})")
        is_ai_turn = not is_ai_turn

A = int(input("Enter Jug A Capacity: "))
B = int(input("Enter Jug B Capacity: "))
T = int(input("Enter Target Volume: "))
play_game(A, B, T)