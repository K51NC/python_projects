from art import title
import random
import art

print(f"{title}\n")
print("Welcome to RPS!")

userPick = input("Select (r)ock, (p)aper, or (s)cissors: ").lower()
userHand = "User hand did not get assigned."
random_integer = random.randint(0, 2)
compPick = -1

if random_integer == 0:
    compPick = "r"
elif random_integer == 1:
    compPick = "p"
elif random_integer == 2:
    compPick = "s"
else:
    print("There was an error with the computer picking.")

if userPick == "r":
    userHand = art.rock
elif userPick == "p":
    userHand = art.paper
elif userPick == "s":
    userHand = art.scissors
else:
    print("Something went wrong when assigning art to the user's hand.")

if compPick == "r":
    compHand = art.rock
elif compPick == "p":
    compHand = art.paper
elif compPick == "s":
    compHand = art.scissors
else:
    print("Something went wrong when assigning art to the computer's hand.")

print(f"You picked:\n{userHand}")
print(f"The computer picked: {compHand}.")

if userPick == "r":
    if compPick == "r":
        print("Draw!")
    elif compPick == "p":
        print("The computer wins!")
    elif compPick == "s":
        print("You win!")
    else:
        print("Something went wrong after you picked 'r'.")
elif userPick == "p":
    if compPick == "r":
        print("You win!")
    elif compPick == "p":
        print("Draw!")
    elif compPick == "s":
        print("The computer wins!")
    else:
        print("Something went wrong after you picked 'p'.")
elif userPick == "s":
    if compPick == "r":
        print("The computer wins!")
    elif compPick == "p":
        print("You win!")
    elif compPick == "s":
        print("Draw!")
    else:
        print("Something went wrong after you picked 's'.")
else:
    print("There was an error when you picked. Did you select r, p, or s?")