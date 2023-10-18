import pandas

# Create a dictionary of nato alphbet phonetics
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter : row.code for (index, row) in nato_alphabet.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs
print([nato_alphabet_dict[letter.upper()] for letter in input("Enter a Word: ")])
