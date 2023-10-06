from guess_the_number_art import logo
import random
import os

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty():
    """Set game difficulty"""
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ")

        #set number of attempts
        if difficulty == "easy":
            return EASY_LEVEL_ATTEMPTS
        elif difficulty == "hard":
            return HARD_LEVEL_ATTEMPTS
        

def play_game():
    """Starts the game"""

    #clear screen
    os.system('clear')
        
    #print logo
    print(logo)

    #choose random number
    number = random.randint(0, 100)

    #greet user
    print("Welcome to GUESS THE NUMBER.")
    print("I'm thinking of a number between 1 and 100.")

    attempts = set_difficulty()
    
    print(f"You have {attempts} attempts to guess the number.")

    #play game while user has enough attempts
    while attempts > 0:
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            break
        elif guess > number:
            print("Too high.\nGuess again.")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number.")
        else:
            print("Too low.\nGuess again.")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number.")

    if attempts == 0:
        print("You lose!")
        
    #prompt user to play again
    play_again = input("Want to play again? 'y' or 'n': ")
    
    if play_again == "y":
        play_game()
    else:
        os.system('clear')
        print("Thanks for playing!")


play_game()
    

