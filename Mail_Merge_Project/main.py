PLACEHOLDER = "[name]"

# Create list of all names to write letters to
with open(file="./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()

# Replace placeholder with each name in invited names and save completed letter as a new file
with open(file="./Input/Letters/starting_letter.txt", mode="r") as letter_file:
        letter_contents = letter_file.read()
        for name in names:
            stripped_name = name.strip()
            new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
            with open(file=f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
                 completed_letter.write(new_letter)
