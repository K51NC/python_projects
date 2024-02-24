from art import title


print(f"{title}\n")
print("Welcome to the tip calculator.")
bill = float((input("What was the total bill? $")))
partySize = int(input("How many people to split the bill? "))
percentTip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
totalBill = round(bill * (percentTip / 100 + 1), 2)
perPersonPay = round(totalBill / partySize, 2)

print(f"Total bill: ${"{:.2f}".format(totalBill)}")
print(f"Each person should pay: ${"{:.2f}".format(perPersonPay)}")