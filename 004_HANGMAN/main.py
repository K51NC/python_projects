import os
import random
import art

wordList = ["alpha", "bravo", "charlie", "delta", "echo"]
livesRemaining = 6
gameRunning = True
userQuit = False
word = random.choice(wordList)
wordBoard = []
wordString = ""
used = []
usedLetters = ""

def guess(letter):
    if letter in used:
        print("You have already used that letter.")
        return
    addLetter(charGuess)
    contains = False
    global livesRemaining
    for char in range(0, len(word)):
        if word[char] == letter:
            wordBoard[char] = letter
            contains = True
    if contains == False:
        livesRemaining -= 1
    return contains

def isComplete():
    complete = True
    for char in wordBoard:
        if char == "_":
            complete = False
    return complete

def printBoard():
    print(wordString.join(wordBoard))
    print(art.board[livesRemaining])
    print(f"Lives remaining: {livesRemaining}")

def addLetter(letter):
    if letter not in used:
        used.append(letter)

def getGuess():
    char = input("Guess a letter or type 'quit' to quit the game: ").lower()
    return char

for x in range(0, len(word)):
    wordBoard += "_"

        
print(f"Welcome to Hangman!\n\nYour word has been selected. Time to begin!\n")

while gameRunning == True and livesRemaining > 0:

    printBoard()
    print(f"Letters you have already used: {usedLetters.join(sorted(used))}")
    charGuess = getGuess()
    os.system('cls')

    if len(charGuess) > 1 and charGuess == "quit":
        gameRunning = False
        userQuit = True
    elif len(charGuess) == 1:
        guess(charGuess)
    elif len(charGuess) == 0:
        print("You did not input a letter.")
    else:
        print("Only 1 letter at a time please.")
    
    if isComplete() == True:
        gameRunning = False
    


if userQuit == True:
    os.system('cls')
    print("Thank you for playing. Goodbye!")
elif livesRemaining == 0:
    os.system('cls')
    print(art.board[livesRemaining])
    print("You ran out of lives! Sorry.")
    print(f"The word was {word.upper()}...")
else:
    os.system('cls')
    print(f"The word was {word.upper()}!")
    print(f"CONGRATS! You guessed it right with {livesRemaining} lives remaining.")