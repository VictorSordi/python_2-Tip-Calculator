print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? " + "$ "))
tip = int(input("How much tip would you like to give?, 10, 12 or 15" + "?"))
bill_with_tip = tip/100 * bill + bill
people = int(input("How many people to split the bill? "))
bill_split = bill_with_tip / people
print(f"Each person should pay: ${round(bill_split, 2)}")
