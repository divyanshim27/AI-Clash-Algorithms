# app.py - Improved Clash of Algorithms Dashboard

import streamlit as st
import time
import copy
from engine import check_winner, get_available_moves
from algorithms import bfs_player, minimax_player, nodes_bfs, nodes_minimax

st.title("Clash of Algorithms: BFS vs Minimax Alpha-Beta")

# Initialize game state
if 'board' not in st.session_state:
    st.session_state.board = [' '] * 9
    st.session_state.turn = 'X'          # BFS starts as X
    st.session_state.game_over = False
    st.session_state.last_nodes = 0
    st.session_state.last_time = 0.0

board = st.session_state.board

# Display interactive 3x3 grid
st.subheader("Game Board")
cols = st.columns(3)
for row in range(3):
    for col in range(3):
        idx = row * 3 + col
        symbol = board[idx]
        label = " " if symbol == ' ' else symbol
        disabled = (symbol != ' ') or st.session_state.game_over
        if cols[col].button(label, key=f"cell_{idx}", disabled=disabled):
            # For future: allow human play — but for now AI vs AI only
            pass  # We handle AI moves below

# AI vs AI button
if st.button("Start / Next Move (AI vs AI)", type="primary") and not st.session_state.game_over:
    start_time = time.time()

    if st.session_state.turn == 'X':
        move = bfs_player(board, 'X')
        player_name = "BFS (X)"
        nodes = nodes_bfs
    else:
        move = minimax_player(board, 'O', 'X')
        player_name = "Minimax Alpha-Beta (O)"
        nodes = nodes_minimax

    if move is not None and move in get_available_moves(board):
        board[move] = st.session_state.turn
        st.session_state.turn = 'O' if st.session_state.turn == 'X' else 'X'
        st.session_state.last_nodes = nodes
        st.session_state.last_time = (time.time() - start_time) * 1000

        winner = check_winner(board)
        if winner:
            st.session_state.game_over = True
            if winner == 'Tie':
                st.info("It's a Tie!")
            else:
                st.success(f"{winner} wins! ({'BFS' if winner == 'X' else 'Minimax'})")

    else:
        st.warning("No valid move found — game might be over.")

# Live stats
col1, col2 = st.columns(2)
col1.metric("Nodes Explored (last move)", st.session_state.last_nodes)
col2.metric("Time taken (ms)", f"{st.session_state.last_time:.2f}")

# Show current board in readable text format
st.subheader("Current Board (text view):")
board_str = ""
for i in range(0, 9, 3):
    row = f" {board[i]} | {board[i+1]} | {board[i+2]} "
    board_str += row + "\n"
    if i < 6:
        board_str += "---+---+---\n"
st.code(board_str)

# Reset
if st.button("Reset Game"):
    st.session_state.board = [' '] * 9
    st.session_state.turn = 'X'
    st.session_state.game_over = False
    st.session_state.last_nodes = 0
    st.session_state.last_time = 0.0
    st.rerun()

# Instructions
st.markdown("---")
st.info("Click 'Start / Next Move' repeatedly to watch BFS (X) vs Minimax Alpha-Beta (O) play. BFS explores many more nodes — watch the difference!")