




import random


rules = {
    (0, 2): "User wins!", 
    (2, 1): "User wins!", 
    (1, 0): "User wins!",  
    (2, 0): "Computer wins!",
    (1, 2): "Computer wins!", 
    (0, 1): "Computer wins!",  
}


choices = {0: "Rock", 1: "Paper", 2: "Scissors"}


user_choice = int(input("Enter your choice: 0 for Rock, 1 for Paper, 2 for Scissors: "))


if user_choice not in choices:
    print("Invalid choice! Please enter 0, 1, or 2.")
else:
    
    computer_choice = random.randint(0, 2)

    print(f"User's choice: {choices[user_choice]}")
    print(f"Computer's choice: {choices[computer_choice]}")


    if user_choice == computer_choice:
        print("It's a draw!")
    else:
        print(rules.get((user_choice, computer_choice), "Invalid result!"))


import random

user_choice = int(input("enter ur choice: 0 rock,1 sci 2 paper"))

if(user_choice>=3 or user_choice<0):
    print("u lose")
else:
    print(user_choice)
    computer_choice = random.randint(0,2)
    print("computer choice:",computer_choice)

    if(computer_choice == user_choice):
        print("draw")
    elif(computer_choice > user_choice):
        print("computer wins")
    elif(user_choice > computer_choice):
        print("user wins")
    elif(computer_choice == 0 and user_choice == 2):
        print("computer win")
    elif(user_choice == 0 and computer_choice == 2):
        print("user win")

