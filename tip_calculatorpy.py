print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
person = float(input("How many people to split the bill? "))
payment = bill * ((tip/100)+1) / person
print(f"Each person should pay: ${payment:.2f}")



