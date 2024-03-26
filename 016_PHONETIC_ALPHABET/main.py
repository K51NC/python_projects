ALPHABET_FILE = "./016_PHONETIC_ALPHABET/input/nato_phonetic_alphabet.csv"

import pandas

alphabet_data = pandas.read_csv(ALPHABET_FILE)
alpha_dict = {row.letter:row.code for index, row in alphabet_data.iterrows()}

while True:
        user_input = input("Enter a word:\n").upper()
        if user_input.isalpha():
            break
        else:
            print("Please enter one word using letters from A-z.")

result = [alpha_dict[letter] for letter in user_input]

print(result)