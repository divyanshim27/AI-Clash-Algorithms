# AI Clash Algorithms

**Algorithm Clash — BFS vs Minimax with α-β Pruning**

An interactive educational demonstration of two fundamental AI search algorithms competing in real time.

---

## Project Overview

**AI Clash Algorithms** is an educational web application that visually demonstrates the fundamental differences between **Breadth-First Search (BFS)** and **Minimax with α-β Pruning** through a live Tic-Tac-Toe game.

The project is designed to help students, educators, and developers clearly understand how uninformed search and adversarial search algorithms operate, analyse their performance, and observe their strategic behaviour in a zero-sum game environment.

By playing BFS (X) against Minimax (O), users can directly compare:
- Search strategy
- Node exploration efficiency
- Decision-making quality
- Computational performance

This tool serves as an excellent visual aid for teaching and learning core concepts in Artificial Intelligence and Game Theory.

---

## Live Demo

You can play the game online here:  
**[🔗 Play Algorithm Clash](https://divyanshim27.github.io/Al-Clash-Algorithms/clash_of_algorithms.html)**

---

## Features

- Fully interactive 3x3 Tic-Tac-Toe board
- Real-time battle between BFS and Minimax α-β
- Live metrics: nodes explored, execution time, and pruning percentage
- Detailed engine log showing each algorithm’s decision process
- Auto-play mode and manual move support
- Score tracking across multiple games
- Responsive dark cyber-themed UI with smooth animations
- Single-file, self-contained web application

---

## Algorithms Explained

### 1. Breadth-First Search (BFS)
BFS is a classic **uninformed search algorithm** that explores all possible moves level by level. In this implementation, it simulates breadth-first traversal of the game tree up to a limited depth and selects the next move using a simple heuristic (center → corner → edge).

**Key Characteristics:**
- Explores widely rather than deeply
- Does not assume optimal play from the opponent
- Higher number of nodes explored
- Useful for understanding basic graph traversal

### 2. Minimax with α-β Pruning
Minimax is an **adversarial search algorithm** designed for two-player zero-sum games. It recursively evaluates the game tree assuming both players play optimally — maximising its own score while minimising the opponent’s.

**α-β Pruning** is an optimisation technique that eliminates branches of the search tree that cannot influence the final decision, significantly reducing computation time without affecting the result.

**Key Characteristics:**
- Optimal decision making
- Looks several moves ahead
- Dramatically fewer nodes explored due to pruning
- Represents intelligent, strategic AI behaviour

---

## Educational Purpose

This project was created to provide a clear, visual, and interactive way to:
- Understand the difference between uninformed and informed/adversarial search
- Observe the impact of α-β pruning on performance
- Analyse why certain algorithms are more efficient in competitive environments
- Serve as a teaching tool for AI, Algorithms, and Game Theory concepts

---

## Project Structure

| File                      | Description                                      |
|--------------------------|--------------------------------------------------|
| `clash_of_algorithms.html` | Main interactive web game (HTML + CSS + JS)     |
| `algorithms.py`           | Python implementations of BFS and Minimax        |
| `app.py`                  | Backend application file                         |
| `engine.py`               | Core game engine logic                           |
| `requirements.txt`        | Python dependencies                              |
| `README.md`               | Project documentation                            |

---

## Technologies Used

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: Custom CSS with modern animations and responsive design
- **Algorithms**: Implemented directly in JavaScript for real-time browser execution
- **Deployment**: GitHub Pages

No external frameworks or libraries were used — the entire application is self-contained in a single HTML file.

---

## How to Run Locally

1. Clone or download the repository.
2. Open `clash_of_algorithms.html` in any modern web browser.
3. Click **"Next AI Move"** to watch the algorithms play, or use **"Auto-play"** for continuous demonstration.

---

## Made for Educational Exploration

This project stands as a practical demonstration of core Artificial Intelligence concepts. It is ideal for:
- Classroom presentations
- Algorithm visualisation
- Self-learning in AI and search techniques
- Portfolio showcases

---

**Created by Divyanshi**

---