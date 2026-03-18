def print_board(board):
    """Visualizes the board in your terminal"""
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6: print("---------")

def check_winner(board):
    """Checks if someone won. Returns 'X', 'O', 'Tie', or None"""
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Cols
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != ' ':
            return board[combo[0]]
    
    if ' ' not in board:
        return 'Tie'
    return None

def get_available_moves(board):
    """Returns a list of empty indices (0-8)"""
    return [i for i, spot in enumerate(board) if spot == ' ']