# IMPORTS
import art

# FUNCTIONS
def multiply(first, second):
    """Multiply first number with second number."""
    return first * second

def divide(first, second):
    """Divide first number by second number."""
    return first / second

def add(first, second):
    """Add second number to first number."""
    return first + second

def subtract(first, second):
    """Subtract second number from first number."""
    return first - second

def getNum(number):
    """Asking user to input number."""
    while True:
        try:
            num = float(input(f"{number} number: "))
            break
        except:
            print("Invalid input. Please enter a number.")
    return num

def getOperation():
    """Asking user to input operation."""
    while True:
        operation = input(f"Enter the operation you wish to perform:\n'*'\n'/'\n'+'\n'-'\n")
        if operation == "*" or operation == "/" or operation == "+" or operation == "-":
            return operation
        else:
            print("Invalid operation. Please type in '*' '/' '+' or '-'.")

def more():
    """Asking a user if they would like to continue using the previous result in a new calculation."""
    tempNumber = result

    while True:
        yesNo = input("Would you like to continue working with this result? (y)es or (n)o: ").lower()
        if yesNo == "y" or yesNo == "yes":
            return False, tempNumber
        elif yesNo == "n" or yesNo == "no":
            tempNumber = 0
            return True, tempNumber
        else:
            print("Invalid input. Please answer (y)es or (n).")

def proceed():
    """Asking user if they would like to end the program."""
    while True:
        yesNo = input("Would you like to make another calculation? (y)es or (n): ").lower()
        if yesNo == "y" or yesNo == "yes":
            return True
        elif yesNo == "n" or yesNo == "no":
            return False
        else:
            print("Invalid input. Please type (y)es or (n).")

# INITS
running = True
firstNum = 0
secondNum = 0
result = 0
startOver = True
operations = {
    "*": multiply,
    "/": divide,
    "+": add,
    "-": subtract
    }

print(art.title)
print("Welcome to the Calculator!")

while running:

    if startOver == True:
        firstNum = getNum("First")

    action = getOperation()
    secondNum = getNum("Second")
    result = operations[action](first = firstNum, second = secondNum)
    print(f"{firstNum} {action} {secondNum} = {result}")

    startOver, result = more()
    firstNum = result

    if startOver == True:
        running = proceed()
