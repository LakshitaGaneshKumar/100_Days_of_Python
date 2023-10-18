from art import logo
import random
import os

#deck of possible cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

def deal_cards():
    """Deals a card at random"""
    return random.choice(cards)


def compute_scores(card_list):
    """Takes in a card list and computes the sum of all the cards in that list"""
    
    #compute score
    score = 0
    for card in card_list:
        score += card

    #checks for blackjack
    if score == 21 and len(card_list) == 2:
        return 0
    
    #checks for an Ace 11 that goes over 21 and replaces it with an Ace 1
    if 11 in card_list and score > 21:
        card_list.remove(11)
        card_list.append(1)
        score -= 10

    return score


def compare_scores(user_score, computer_score):
    """Takes in the user's score and the computer's score and compares those two values to determine the winner"""
    if user_score == computer_score:
        return "    It's a Draw!"
    elif computer_score == 0:
        return "    Opponent has a Blackjack. You lose!"
    elif user_score == 0:
        return "    You win with a Blackjack!"
    elif user_score > 21:
        return "    You went over 21. You lose!"
    elif computer_score > 21:
        return "    Opponent went over 21. You win!"
    elif user_score > computer_score:
        return "    You win!"
    else:
        return "    Opponent wins!"


def start_game():
    """Prompts user to start a new Blackjack Game"""
    game_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if game_play == "y":
        play_game()
    else:
        print("Thanks for trying out Blackjack.")


def play_game():
    """Starts the Blackjack Game"""
    os.system('clear')
        
    #print logo
    print(logo)

    #track if game is over
    game_over = False

    #deal two cards at random for user and computer
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    #add cards to user's hand
    while not game_over:

        #compute current scores
        user_score = compute_scores(user_cards)
        computer_score = compute_scores(computer_cards)
            
        #print initial results
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        #check if game over
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            #prompt user for another card
            next_card = input("    Type 'y' to get another card, type 'n' to pass: ")

            if next_card == "y":
                user_cards.append(deal_cards())
            else:
                game_over = True
        
    #add cards to computer's hand
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = compute_scores(computer_cards)

    #compare final scores and print result
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_scores(user_score, computer_score))
    start_game()


start_game()
