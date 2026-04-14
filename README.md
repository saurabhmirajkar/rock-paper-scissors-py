# 🪨📄✂️ Rock, Paper, Scissors (Python CLI)

A lightweight, terminal-based implementation of the classic Rock, Paper, Scissors game. 

This project was built to explore core Python concepts, specifically focusing on moving away from exhaustive `if/else` branching and utilizing mathematical patterns (Modulo logic) for game state resolution.

## ✨ Features
* **Mathematical Win Logic:** Uses a modulo-based engine (`(user - computer) % 3`) to calculate win/loss states efficiently.
* **Input Validation:** Safely handles unexpected user inputs using dictionary `.get()` fallbacks.
* **Randomized AI:** Utilizes Python's `random` module for unpredictable computer choices.

## 🚀 How to Run

1. Ensure you have Python 3.x installed.
2. Clone this repository:
   ```bash
   git clone https://github.com/saurabhmirajkar/rock-paper-scissors-py.git