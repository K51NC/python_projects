import os
from random import choice
from assets import fullDeck
import copy
from time import sleep

dealer = {
    "name": "Dealer",
    "cards": ['', ''],
    "blackJack": False,
    "bust": False
}
players = {
    0: dealer
}
currentDeck = {}
currentDeck = copy.deepcopy(fullDeck)
allBust = True
running = True
dealSpeed = 2


def setPlayerNames():
    while True:
        try:
            playerCount = (int(input("How many players? (Max 4 players)\n")))
            if playerCount < 1 or playerCount > 4:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please type the number of players. (1-4)")
    for each in range(1, playerCount + 1):
        while True:
            try:
                playerName = input(f"Name of player {each}? ").capitalize()
                if playerName.isalpha():
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input for a name. Only letters are permitted for names.")
        players[each] = createPlayer(playerName)
    return playerCount

def clearScreen():
    if os == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def createPlayer(playerName):
    player = {
        "name": playerName,
        "balance": 0,
        "bet": 0,
        "handValue": 0,
        "cards": ["", ""],
        "blackJack": False,
        "bust": False
    }
    return player

def getCard():
    global currentDeck
    availableCards = []
    for each in currentDeck:
        if currentDeck[each]["qty"] != 0:
            availableCards += [each]
    card = choice(availableCards)
    currentDeck[card]["qty"] -= 1
    return card

def deal():
    for each in players:
        players[each]["cards"][0] = getCard()
    for each in players:
        players[each]["cards"][1] = getCard()
        players[each]["handValue"] = handValue(each)
        if players[each]["handValue"] == 21:
            players[each]["blackJack"] = True
    # # dealer is dealt blackjack here for debugging
    # players[0]["cards"] = ["A", "K"]
    # players[0]["handValue"] == handValue(0)
    # players[0]["blackJack"] = True
    # # first player is dealt a blackjack here for debugging
    # players[1]["cards"] = ["J", "A"]
    # players[1]["handValue"] == handValue(0)
    # players[1]["blackJack"] = True

def handValue(playerID):
    value = 0
    aceCount = 0
    for each in range(0, len(players[playerID]["cards"])):
        if players[playerID]["cards"][each] == "A":
            aceCount += 1
        value += fullDeck[players[playerID]["cards"][each]]["value"]
    while value > 21 and aceCount > 0:
        value -= 10
        aceCount -= 1
    return value

def blackjack(playerID):
    if players[playerID]["handValue"] == 21:
        return True
    else:
        return False

def resetDeck():
    global currentDeck
    currentDeck = copy.deepcopy(fullDeck)

def resetPlayers():
    global allBust
    allBust = True
    for each in players:
        players[each]["handValue"] = 0
        players[each]["cards"] = ["", ""]
        players[each]["blackJack"] = False
        players[each]["bust"] = False

def playerTurn(playerID):
    global allBust
    invalid = False
    while True:
        clearScreen()
        if invalid:
            print("Invalid input. Please type 'h' or 's'.\n")
        invalid = False
        print(f"{players[playerID]["name"]}:")
        print(f"Dealer hand: * {players[0]["cards"][1]}")
        print(f"Your hand: {" ".join(players[playerID]["cards"])} ({players[playerID]["handValue"]})")
        hitStand = input("Would you like to hit or stand? Type 'h' or 's'.\n").lower()
        if hitStand == 'h' or hitStand == 'hit':
            players[playerID]["cards"].append(getCard())
        elif hitStand == 's' or hitStand == 'stand':
            allBust = False
            break
        else:
            invalid = True
        players[playerID]["handValue"] = handValue(playerID)
        if players[playerID]["handValue"] > 21:
            clearScreen()
            print(f"{players[playerID]["name"]}:")
            print(f"Your hand: {" ".join(players[playerID]["cards"])} ({players[playerID]["handValue"]})")
            print("BUST!")
            print(f"You lost your bet of {players[playerID]["bet"]}.")
            print(f"Your new balance is ${players[playerID]["balance"]}.")
            input("Press 'enter' to continue.")
            players[playerID]["bust"] = True
            players[playerID]["bet"] = 0
            break

def dealerTurn():
    clearScreen()
    for each in range(1, len(players)):
        print(f"{players[each]["name"]}: {" ".join(players[each]["cards"])} ({players[each]["handValue"]})")
    if allBust == True:
        print("All players bust. Dealer wins!")
    else:
        while True:
            players[0]["handValue"] = handValue(0)
            print(f"Dealer's hand is: {" ".join(players[0]["cards"])} ({players[0]["handValue"]})")
            if players[0]["handValue"] < 17:
                sleep(dealSpeed)
                print("DEALER HIT")
                players[0]["cards"].append(getCard())
            elif players[0]["handValue"] > 21:
                print("DEALER BUST")
                players[0]["bust"] = True
                break
            else:
                print("DEALER STAND")
                break

def payout():
    for each in range(1, len(players)):
        if players[each]["blackJack"] == False:
            if players[each]["bust"] == False:
                if players[0]["bust"]:
                    print(f"{players[each]["name"]} won against the dealer. Payout is ${players[each]["bet"] * 2}.")
                    players[each]["balance"] += players[each]["bet"] * 2
                    players[each]["bet"] = 0
                elif (players[each]["handValue"] > players[0]["handValue"]):
                    print(f"{players[each]["name"]} won against the dealer. Payout is ${players[each]["bet"] * 2}.")
                    players[each]["balance"] += players[each]["bet"] * 2
                    players[each]["bet"] = 0
                elif players[each]["handValue"] == players[0]["handValue"]:
                    print(f"{players[each]["name"]} tied the dealer. Bet of ${players[each]["bet"]} has been returned.")
                    players[each]["balance"] += players[each]["bet"]
                    players[each]["bet"] = 0
                elif players[each]["handValue"] < players[0]["handValue"]:
                    print(f"{players[each]["name"]} lost against the dealer. Bet of ${players[each]["bet"]} has been lost.")
                    players[each]["bet"] = 0
                else:
                    print("ERROR OCCURED AT POSITION 1")   

def chipAmount(playerID):
    while True:
        try:
            chips = round(float(input(f"How many chips would you like to purchase? $")), 2)
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    return chips

def anotherRound():
    while True:
        playAgain = input("Play another round? Type 'y' or 'n':\n").lower()
        if playAgain == 'y' or playAgain =='yes':
            return True
        elif playAgain == 'n' or playAgain == 'no':
            print("Thank you for playing! Final balances:")
            for each in range(1, len(players)):
                print(f"{players[each]["name"]}: ${players[each]["balance"]}")
            return False
        else:
            print("Invalid option.")