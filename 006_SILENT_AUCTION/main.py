import os
import art

running = True
bids = {"Nobody": 0}
currentWinner = "Nobody"

def getName():
    nameUsed = True
    name = ""

    while nameUsed:
        name = input("Name of bidder: ")
        if name.isalpha() == False:
            print("Invalid input. Please type in a name using only letters.")
            continue
        for key in bids:
            if key.lower() == name.lower():
                print("Sorry, name is already in use. Please use a different name.")
                nameUsed = True
                break
            else:
                nameUsed = False
    if nameUsed == False:
        return name

def getBid():
    while True:
        try:
            return int(input(f"Bid of {biddingUser}: "))
        except:
            print("Invalid input. Please type in a number.")

def inputBid(user, bid):
    global currentWinner
    global bids
    bids[user] = bid

    if bid > bids[currentWinner]:
        currentWinner = user

def endRunning():
    validInput = False

    while not validInput:
        selection = input("Is there another bidder? (y) or (n) ").lower()
        if selection == "y" or selection == "yes":
            validInput = True
            return True
        elif selection == "n" or selection == "no":
            validInput = True
            return False
        else:
            print("Invalid input. Please type in 'y' or 'n'.")

def showWinner():
    print(f"The winner is {currentWinner} with a bid of ${bids[currentWinner]}!") 

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



print(art.title)
print("Welcome to the silent auction!\nLet's begin bidding!")

while running:

    biddingUser = getName()
    bid = getBid()
    inputBid(user = biddingUser, bid = bid)
    running = endRunning()
    clear()

    if running == False:
        showWinner()