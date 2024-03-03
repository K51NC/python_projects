from art import title
from assets import *
import copy
import os
from random import choice

running = True
playerCount = 0
currentDeck = copy.deepcopy(fullDeck)
dealer = {
    "name": "Dealer",
    "cards": ['', ''],
    "blackJack": False,
    "bust": False
}
players = {
    0: dealer
}
allBust = True


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

def handValue(playerID):
    value = 0
    for each in range(0, len(players[playerID]["cards"])):
        value += fullDeck[players[playerID]["cards"][each]]["value"]
    # players[playerID]["handValue"] = value
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
    clearScreen()
    global allBust
    print(f"{players[playerID]["name"]}'s turn:")
    print(f"Dealer hand: * {players[0]["cards"][1]}")
    while True:
        print(f"Your hand: {" ".join(players[playerID]["cards"])} ({players[playerID]["handValue"]})")
        hitStand = input("Would you like to (h)it or (s)tand?\n").lower()
        if hitStand == 'h' or hitStand == 'hit':
            players[playerID]["cards"].append(getCard())
        elif hitStand == 's' or hitStand == 'stand':
            allBust = False
            break
        players[playerID]["handValue"] = handValue(playerID)
        if players[playerID]["handValue"] > 21:
            print(f"Your hand: {" ".join(players[playerID]["cards"])} ({players[playerID]["handValue"]})")
            print("BUST!")
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
        print("VERIFY BET HAS BEEN TAKEN FROM 'BALANCE' AND 'BET'")
    else:
        while True:
            players[0]["handValue"] = handValue(0)
            print(f"Dealer's hand is: {" ".join(players[0]["cards"])} ({players[0]["handValue"]})")
            if players[0]["handValue"] < 17:
                players[0]["cards"].append(getCard())
                print("DEALER HIT")
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
                    print(f"{players[each]["name"]} won against the dealer. Payout is {players[each]["bet"] * 2}.")
                    players[each]["balance"] += players[each]["bet"] * 2
                    players[each]["bet"] = 0
                elif (players[each]["handValue"] > players[0]["handValue"]):
                    print(f"{players[each]["name"]} won against the dealer. Payout is {players[each]["bet"] * 2}.")
                    players[each]["balance"] += players[each]["bet"] * 2
                    players[each]["bet"] = 0
                elif players[each]["handValue"] == players[0]["handValue"]:
                    print(f"{players[each]["name"]} tied the dealer. Bet has been returned.")
                    players[each]["balance"] += players[each]["bet"]
                    players[each]["bet"] = 0
                elif players[each]["handValue"] < players[0]["handValue"]:
                    print(f"{players[each]["name"]} lost against the dealer. Bet of {players[each]["bet"]} has been lost.")
                    players[each]["bet"] = 0
                else:
                    print("ERROR OCCURED AT POSITION 1")           
            

print(title)

playerCount = (int(input("How many players? ")))
for each in range(1, playerCount + 1):
    playerName = input(f"Name of player {each}? ").capitalize()
    players[each] = createPlayer(playerName)

while running:

    for each in range(1, playerCount + 1):
        addChips = int(input(f"{players[each]["name"]}: How many chips would you like to purchase? $"))
        players[each]["balance"] += addChips
        print(f"{players[each]["name"]}: New balance is ${players[each]["balance"]}.")
        bet = int(input(f"{players[each]["name"]}'s bet? $"))
        players[each]["balance"] -= bet
        players[each]["bet"] = bet
        print(f"Bet: ${players[each]["bet"]} - New Balance: ${players[each]["balance"]}")


    clearScreen()

    deal()
    if players[0]["blackJack"] == True:
        print("Dealer Blackjack!")
        for each in range(1, len(players)):
            if players[each]["blackJack"]:
                players[each]["balance"] += players[each]["bet"]
                players[each]["bet"] = 0
            else:
                players[each]["bet"] = 0
        running = False
        break
    
    for each in range(1, len(players)):
        if players[each]["blackJack"]:
            print(f"{players[each]["name"]}: Blackjack! Payout is {players[each]["bet"] * 2.5}!")
            players[each]["balance"] += players[each]["bet"] * 2.5
            players[each]["bet"] = 0
            input("Press 'enter' to continue.")
        else:
            playerTurn(each)

    dealerTurn()
    payout()
    resetDeck()
    resetPlayers()

    while True:
        playAgain = input("Play another round? (y)es or (n)o:\n").lower()
        if playAgain == 'y' or playAgain =='yes':
            running = True
            break
        elif playAgain == 'n' or playAgain == 'no':
            running = False
            print("Thank you for playing! Final balances:")
            for each in range(1, len(players)):
                print(f"{players[each]["name"]}: ${players[each]["balance"]}")
            break
