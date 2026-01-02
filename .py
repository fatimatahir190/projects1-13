"""
WORKFLOW OF PROJECT:
choices = ("rock", "paper", "scissors")
computer_choice = (computer will choose randomly not conditionally)
result print 

"""
import random

choices = ("rock", "paper", "scissors")
user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
computer_choice = random.choice(choices)  # computer will choose randomly not conditionally

print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("it is tie")
elif user_choice == "rock" and computer_choice == "scissors":
    print("you win") 
elif user_choice == "rock" and computer_choice == "paper":
    print("you lose")
elif user_choice == "scissors" and computer_choice == "paper":    
    print("you win")
elif user_choice == "scissors" and computer_choice == "rock":  
    print("you lose")  
elif user_choice == "paper" and computer_choice == "rock":   
    print("you win")  
elif user_choice == "paper" and computer_choice == "scissors":
    print("you lose")
else:
    print("Invalid choice! Please enter rock, paper, or scissors.")
