ALPHABET_FILE = "./016_PHONETIC_ALPHABET/input/nato_phonetic_alphabet.csv"

import pandas

alphabet_data = pandas.read_csv(ALPHABET_FILE)
alpha_dict = {row.letter:row.code for index, row in alphabet_data.iterrows()}

def get_input():
    user_input = input("Enter a word:\n").upper()
    try:
        result = [alpha_dict[letter] for letter in user_input]
    except KeyError:
        print("Please enter one word using letters from A-z.")
        get_input()
    else:
        print(result)

get_input()