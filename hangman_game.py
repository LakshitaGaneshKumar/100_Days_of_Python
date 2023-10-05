import random
from hangman_art import stages, logo
from hangman_words import word_list

# initialize variables
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

# print hangman logo
print(logo)

# create and display blanks
display = []
for _ in range(word_length):
    display += "_"

# while loop for the user to play until end of game
while not end_of_game:

    # generate user input
    guess = input("Guess a letter: ").lower()

    # if the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    # check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")

    # display hangman's life stage
    print(stages[lives])
