from art import title
import random

print(f"{title}\n")
print("Welcome to the Password Generator!")

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = ["!", "#", "@", "$", "%", "^", "&", "*", "(", ")"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

userPassword = []
userString = ""


qtyLetters = int(input("How many letters would you like in your password? "))
qtySymbols = int(input("How many symbols would you like in your password? "))
qtyNumbers = int(input("How many numbers would you like in your password? "))

for each in range(0, qtyLetters):
    upperLower = random.randint(0, 1)
    if upperLower == 0:
        userPassword.append(letters[random.randint(0, len(letters) - 1)].lower())
    else:
        userPassword.append(letters[random.randint(0, len(letters)) - 1].upper())

for each in range(0, qtySymbols):
    userPassword.append(random.choice(symbols))

for each in range(0, qtyNumbers):
    userPassword.append(random.choice(numbers))

random.shuffle(userPassword)

print(userString.join(userPassword))
