from art import title
from my_functions import *

print(title)
playerCount = 0

playerCount = setPlayerNames()

while running:

    for each in range(1, playerCount + 1):
        clearScreen()
        print(f"{players[each]["name"]}:")
        print(f"Your current chip balance is ${players[each]["balance"]}.")
        addChips = chipAmount(each)
        players[each]["balance"] += addChips
        while True:
            if players[each]["balance"] > 0:
                break
            else:
                print("Balance must be greater than $0.")
                addChips = chipAmount(each)
                players[each]["balance"] += addChips
        print(f"New balance is ${players[each]["balance"]}.")
        while True:
            try:
                bet = round(float(input(f"Bet? $")), 2)
                if bet > players[each]["balance"]:
                    raise ValueError
                elif bet <= 0:
                    print("Bet cannot be '$0'.")
                else:
                    break
            except ValueError:
                print(f"Invalid bet. Please enter a number within your available balance of {players[each]["balance"]}.")
        players[each]["balance"] -= bet
        players[each]["bet"] = bet
        print(f"Bet: ${players[each]["bet"]} - New Balance: ${players[each]["balance"]}")


    clearScreen()
    deal()


    if players[0]["blackJack"] == True:
        print("Dealer Blackjack!")
        for each in range(1, len(players)):
            if players[each]["blackJack"]:
                print(f"{players[each]["name"]}: Your bet of {players[each]["bet"]} has been returned!")
                players[each]["balance"] += players[each]["bet"]
                players[each]["bet"] = 0
            else:
                print(f"{players[each]["name"]}: Your bet of {players[each]["bet"]} has been lost!")
                players[each]["bet"] = 0
    else:
        for each in range(1, len(players)):
            if players[each]["blackJack"]:
                print(f"{players[each]["name"]}:")
                print(f"Hand: {" ".join(players[each]["cards"])}")
                print(f"Blackjack! Payout is your bet of {players[each]["bet"]} plus {players[each]["bet"] * 1.5}!")
                players[each]["balance"] += players[each]["bet"] * 2.5
                players[each]["bet"] = 0
                print(f"New balance: ${players[each]["balance"]}.")
                input("Press 'enter' to continue.")
            else:
                playerTurn(each)

        dealerTurn()
        payout()
    resetDeck()
    resetPlayers()
    running = anotherRound()
