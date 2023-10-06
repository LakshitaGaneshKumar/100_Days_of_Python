from higher_lower_art import logo, vs
from higher_lower_game_data import data
import random
import os

def clear_screen():
    """Clears the terminal screen"""
    os.system('clear')
    print(logo)


def check_to_play_game():
    """Prompts user to play the Higher-Lower game"""
    play = input("Do you want to play Higher-Lower? 'y' or 'n': ")
    if play == "y":
        clear_screen()
        play_game()
    else:
        clear_screen()
        print("Thanks for trying out Higher-Lower!")


def more_followers(a, b):
    """Takes in two Instagram accounts and returns the account with the most followers"""
    if a['follower_count'] > b['follower_count']:
        return "A"
    else:
        return "B"
    

def check_grammar(description):
    """Takes in a sentence and returns the proper a/an operator"""
    if description[0].lower() == "a":
        return "an"
    else:
        return "a"
    

def format_data(account):
    """Takes in an account's data and returns a formated String of the account's information"""
    name = account['name']
    description = account['description']
    country = account['country']

    return f"{name}, {check_grammar(description)} {description}, from {country}."


def play_game():
    """Starts the Higher-Lower Game"""
    game_over = False
    score = 0
    account_b = random.choice(data)

    while not game_over:
        #choose two random accounts to compare
        account_a = account_b
        account_b = account_a
        #ensures that accounts A and B are different
        while account_b == account_a:
            account_b = random.choice(data)

        #print initial comparisons
        print(f"Compare A: {format_data(account_a)}") 
        print(vs)
        print(f"Against B: {format_data(account_b)}") 

        #check who has more followers
        answer = more_followers(account_a, account_b).lower()

        #user input
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        #check if user's guess is correct
        if guess == answer:
            clear_screen()
            score += 1
            print(f"You're right! Current Score: {score}")
        else:
            clear_screen()
            game_over = True
            print(f"Sorry that's wrong. Final Score: {score}")
            check_to_play_game()
    

clear_screen()
check_to_play_game()
