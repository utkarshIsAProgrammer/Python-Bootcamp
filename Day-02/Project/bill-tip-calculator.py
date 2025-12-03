print("Welcome to the bill tip calculator!")

bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? (10%, 12% or 15%) $"))
people = int(input("How much people to split the bill? $"))

tip_as_percent = tip / 100
tip_amount = (bill * tip) / 100
total_bill = bill + tip_amount
split_amount = total_bill / people

print(f"Each person should pay ${round(split_amount,2)}")
