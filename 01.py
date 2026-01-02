"""
WORKFLOW OF PROJECT:
Input from user(rock,paper,scissors)
computer choice (computer will choose randomly not conditionally)
result print
Rock - Paper = Paper wins
Paper - Paper = Tie
Scissors - Paper = Scissors win
Scissors - Rock = Rock win
"""
import random

item_list = ["Rock", "Paper", "Scissors"]
user_choice = input("Enter your move Rock, Paper, Scissors: ")
comp_choice = random.choice(item_list)
print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("both chooses same := Match tie")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("paper covers rock = computer win")
    elif comp_choice == "Scissors":
        print("rock smashes scissors = You win")
elif user_choice == "Paper":
    if comp_choice == "Scissors":
        print("Scissors cuts paper = computer win")
    elif comp_choice == "Rock":
        print("paper covers rock = you win")
elif user_choice == "Scissors": 
    if comp_choice == "Paper":
        print("Scissors cuts paper = You win")
    elif comp_choice == "Rock":
        print("Rock smashes scissors = Computer win")





