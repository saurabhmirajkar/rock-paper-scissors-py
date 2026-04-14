"""
Rock, Paper, Scissors (CLI Edition)

A terminal-based implementation of the classic game. 
This script utilizes a mathematical modulo approach to resolve 
win states efficiently, bypassing traditional exhaustive conditional branching.

Rules Mapping:
- Rock: -1
- Paper: 0
- Scissors: 1
"""
import random

game_rules = {"r": -1, "p": 0, "s": 1}
rule_names = {-1: "🗿 Rock", 0: "🧻 Paper", 1: "✂️ Scissors"}

user_input = input("Enter your choice (r, p or s): ")

# 1. Validation
user_choice = game_rules.get(user_input)

if user_choice is None:
    print("Your choice is not valid! 🚫")
else:
    # 2. Execution
    computer_choice = random.choice([-1, 0, 1])

    # 3. Presentation
    print(f"😎 [You] - {rule_names.get(user_choice)}")
    print(f"🤖 [Computer] - {rule_names.get(computer_choice)}")

    # 4. Win Logic (The Modulo Trick)
    if user_choice == computer_choice:
        print("🤝 It's a draw my friend!")
    elif (user_choice - computer_choice) % 3 == 1:
        print("You Win! 🎉")
    else:
        print("You Lose! 🦧")
