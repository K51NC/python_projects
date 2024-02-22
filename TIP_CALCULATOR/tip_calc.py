print("Welcome to the tip calculator.")
totalBill = float((input("What was the total bill? $")))
partySize = int(input("How many people to split the bill? "))
percentTip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
perPersonPay = round((totalBill / partySize) * (percentTip / 100 + 1), 2)

print("Each person should pay: $" + str(perPersonPay))