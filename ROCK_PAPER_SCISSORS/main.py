import random

print("Welcome to RPS!")

userPick = input("Select (r)ock, (p)aper, or (s)cissors: ")
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

print(f"You picked {userPick}.")
print(f"The computer picked {compPick}.")

if userPick == "r":
    if compPick == "r":
        print("Draw!")
    elif compPick == "p":
        print("You win!")
    elif compPick == "s":
        print("The computer wins!")
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