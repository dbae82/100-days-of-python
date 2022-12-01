print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100 + 1
people_split = int(input("How many people to split the bill? "))
payment = round(total_bill * tip_percentage / people_split, 2)
message = f"Each person should pay: ${payment}"

print(message)