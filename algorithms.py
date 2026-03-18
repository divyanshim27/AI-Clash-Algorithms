# algorithms.py - AI Players: BFS vs Minimax + Alpha-Beta

import copy
from engine import check_winner, get_available_moves

# Global counters (reset per move)
nodes_bfs = 0
nodes_minimax = 0

def bfs_player(board, player='X'):
    """BFS: Finds shortest path to win (ignores opponent intelligence)"""
    global nodes_bfs
    nodes_bfs = 0

    from collections import deque

    queue = deque([(copy.deepcopy(board), [])])  # (state, path of moves)

    visited = set()
    visited.add(tuple(board))

    while queue:
        current_board, path = queue.popleft()
        nodes_bfs += 1

        winner = check_winner(current_board)
        if winner == player:
            # Found winning path - return first move in path
            return path[0] if path else None

        for move in get_available_moves(current_board):
            new_board = copy.deepcopy(current_board)
            new_board[move] = player
            new_tuple = tuple(new_board)
            if new_tuple not in visited:
                visited.add(new_tuple)
                new_path = path + [move]
                queue.append((new_board, new_path))

    # No win found → pick any move (or handle draw/loss)
    moves = get_available_moves(board)
    return moves[0] if moves else None


def minimax_alpha_beta(board, depth, alpha, beta, maximizing, player='X', opponent='O'):
    """Minimax with Alpha-Beta Pruning + node counter"""
    global nodes_minimax
    nodes_minimax += 1

    winner = check_winner(board)
    if winner == player:
        return 10 - depth  # Prefer quicker wins
    if winner == opponent:
        return -10 + depth
    if winner == 'Tie':
        return 0

    if maximizing:
        max_eval = -float('inf')
        for move in get_available_moves(board):
            new_board = copy.deepcopy(board)
            new_board[move] = player
            eval = minimax_alpha_beta(new_board, depth + 1, alpha, beta, False, player, opponent)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # prune
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(board):
            new_board = copy.deepcopy(board)
            new_board[move] = opponent
            eval = minimax_alpha_beta(new_board, depth + 1, alpha, beta, True, player, opponent)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def minimax_player(board, player='X', opponent='O'):
    """Wrapper: chooses best move using alpha-beta"""
    global nodes_minimax
    nodes_minimax = 0

    best_score = -float('inf')
    best_move = None

    for move in get_available_moves(board):
        new_board = copy.deepcopy(board)
        new_board[move] = player
        score = minimax_alpha_beta(new_board, 0, -float('inf'), float('inf'), False, player, opponent)
        if score > best_score:
            best_score = score
            best_move = move

    return best_move