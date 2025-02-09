




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



