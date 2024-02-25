import os
from art import title

print(title)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
running = True
print("Welcome to the Caesar Cipher!\n")

def encode(word, shift):
    encodedWord = ""
    for char in word:
        if char in alphabet:            
            alphabetIndex = alphabet.index(char)
            shiftedLetter = alphabet[(alphabetIndex + shift) % len(alphabet)]
            encodedWord += shiftedLetter
        else:
            encodedWord += char
    return encodedWord

    
def decode(word, shift):
    decodedWord = ""
    for char in word:
        if char in alphabet:
            alphabetIndex = alphabet.index(char)
            shiftedLetter = alphabet[(alphabetIndex - shift) % len(alphabet)]
            decodedWord += shiftedLetter
        else:
            decodedWord += char
    return decodedWord

def shift():
    while True:
        try:
            shift = int(input("Enter shift number: "))
            break
        except ValueError:
            print("Please enter an integer.")
    return shift



while running:

    userChoice = input("Would you like to '(e)ncode' or '(d)ecode'?\n").lower()

    if userChoice == 'e' or userChoice == 'encode':
        word = input("Enter the word you would like to encode:\n")
        shiftNumber = shift()
        print(f"Your encoded word is: '{encode(word, shiftNumber)}'.")

    elif userChoice == 'd' or userChoice == 'decode':
        word = input("Enter the word you would like to decode:\n")
        shiftNumber = shift()
        print(f"Your decoded word is: '{decode(word, shiftNumber)}'.")
    else:
        print("You have typed something I am not familiar with. Please type 'e' for encode or 'd' for decode.")
        continue


    while True:
        endRunning = input("Do you have another word? (y) or (n)\n").lower()
        if endRunning == "n" or endRunning == "no":
            running = False
            break
        elif endRunning == "y" or endRunning == "yes":
            break
        else:
            print("You have typed something I am not familiar with. Please type 'y' for yes or 'n' for no.")

os.system("cls")
print("Goodbye!")