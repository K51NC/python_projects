import os
import random
import art
import words

word = random.choice(words.list)
wordBoard = []
used = []
livesRemaining = 6
gameRunning = True
userQuit = False

for x in range(0, len(word)):
    wordBoard += "_"

print(f"{art.title}\n")
input(f"Welcome to Hangman!\n\nYour word has been selected. Press the 'enter' key to begin!\n")

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    
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

def isComplete():
    complete = True
    for char in wordBoard:
        if char == "_":
            complete = False
    return complete

def printBoard():
    print(" ".join(wordBoard))
    print(art.board[livesRemaining])
    print(f"Lives remaining: {livesRemaining}")

def addLetter(letter):
    if letter not in used:
        used.append(letter)

def getGuess():
    char = input("Guess a letter or type 'quit' to quit the game: ").lower()
    return char
        

while gameRunning == True and livesRemaining > 0:

    printBoard()
    print(f"Letters you have already used: {" ".join(sorted(used))}\n")
    charGuess = getGuess()
    clear()

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
    clear()
    print("Thank you for playing. Goodbye!")
elif livesRemaining == 0:
    clear()
    print(art.board[livesRemaining])
    print("You ran out of lives! Sorry.")
    print(f"The word was {word.upper()}...")
else:
    clear()
    print(f"The word was {word.upper()}!")
    print(f"CONGRATS! You guessed it right with {livesRemaining} lives remaining.")