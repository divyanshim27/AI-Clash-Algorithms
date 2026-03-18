# app.py - Streamlit Dashboard for Clash of Algorithms

import streamlit as st
import time
from engine import print_board, check_winner, get_available_moves
from algorithms import bfs_player, minimax_player, nodes_bfs, nodes_minimax

st.title("Clash of Algorithms: BFS vs Minimax Alpha-Beta")

# Initialize session state
if 'board' not in st.session_state:
    st.session_state.board = [' '] * 9
    st.session_state.turn = 'X'  # BFS starts as X
    st.session_state.game_over = False

board = st.session_state.board

# Display board as 3x3 buttons
cols = st.columns(3)
for i in range(3):
    for j in range(3):
        idx = i*3 + j
        with cols[j]:
            if st.button(board[idx] or " ", key=f"btn_{idx}", disabled=board[idx] != ' ' or st.session_state.game_over):
                # Human move? For now auto AI vs AI
                pass  # We'll add AI moves below

# Auto-play AI vs AI when button pressed
if st.button("Start / Next Move (AI vs AI)") and not st.session_state.game_over:
    start_time = time.time()

    if st.session_state.turn == 'X':
        move = bfs_player(board, 'X')
        player_name = "BFS (X)"
        nodes = nodes_bfs
    else:
        move = minimax_player(board, 'O', 'X')
        player_name = "Minimax (O)"
        nodes = nodes_minimax

    if move is not None:
        board[move] = st.session_state.turn
        st.session_state.turn = 'O' if st.session_state.turn == 'X' else 'X'

    elapsed = (time.time() - start_time) * 1000  # ms

    winner = check_winner(board)
    if winner:
        st.session_state.game_over = True
        st.success(f"{winner} wins!" if winner != 'Tie' else "It's a Tie!")

# Live stats
col1, col2 = st.columns(2)
with col1:
    st.metric("Nodes Explored (last move)", nodes if 'nodes' in locals() else 0)
with col2:
    st.metric("Time taken (ms)", f"{elapsed:.2f}" if 'elapsed' in locals() else 0)

# Show board in text
st.text("Current Board:")
st.code("\n".join([" | ".join(board[i:i+3]) for i in range(0,9,3)]))

# Reset button
if st.button("Reset Game"):
    st.session_state.board = [' '] * 9
    st.session_state.turn = 'X'
    st.session_state.game_over = False
    st.rerun()