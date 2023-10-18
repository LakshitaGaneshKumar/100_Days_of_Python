# import random module
import random

# create ASCII art for all possible moves in the game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# create list of all possible moves in the game
possible_moves = [rock, paper, scissors]

# generate user input, convert into Integer data type, and validate input
user_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"
    ))
if user_choice > 2 or user_choice < 0:
    print("You printed an invalid number. You lose!")
else:
    # print image of user's move
    print(possible_moves[user_choice])

    # randomly generate computer's choice
    computer_choice = random.randint(0, len(possible_moves) - 1)

    # print image of computer's choice
    print(f"Computer choses: {computer_choice}")
    print(possible_moves[computer_choice])

    # calculate winner of game
    if user_choice == computer_choice:
        print("Draw!")
    elif user_choice == 0:
        if computer_choice == 1:
            print("You lose.")
        else:
            print("You win!")
    elif user_choice == 1:
        if computer_choice == 2:
            print("You lose.")
        else:
            print("You win!")
    else:
        if computer_choice == 0:
            print("You lose.")
        else:
            print("You win!")
