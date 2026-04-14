'''

PROJECT 1: Rock, Paper, Scissor game

We all have played Rock, Paper, Scissor game in our childhood. If you haven't,
google the rules of this game and write a python program capable of playing
this game with the user.

'''
import random

game_rules = {"r": -1, "p": 0, "s": 1}
rule_names = {-1: "🗿 Rock", 0: "🧻 Paper", 1: "✂️ Scissors"}

user_input = input("enter your choice (r,p or s): ")

if game_rules.get(user_input) is None:
    print("Your choice is not valid! 🚫")

else:
    computer_choice = random.choice([-1, 0, 1])
    user_choice = game_rules.get(user_input)

    computer_selection = rule_names.get(computer_choice)
    user_selection = rule_names.get(user_choice)

    print(f"😎 [You] - {user_selection}\n🤖 [Computer] - {computer_selection}")

    if computer_choice == user_choice:
        print("🤝 It's a draw my friend!")
    else:
        if computer_choice == -1 and user_choice == 0:
            print("You Win! 🎉")

        elif computer_choice == -1 and user_choice == 1:
            print("You Lose! 🦧")

        elif computer_choice == 0 and user_choice == -1:
            print("You Lose! 🦧")

        elif computer_choice == 0 and user_choice == 1:
            print("You Win! 🎉")

        elif computer_choice == 1 and user_choice == -1:
            print("You Win! 🎉")

        elif computer_choice == 1 and user_choice == 0:
            print("You Lose! 🦧")

        else:
            print("Something went wrong! 😵‍💫")
