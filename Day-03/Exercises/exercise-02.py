# pizza order exercise

"""
small pizza =  $15, pepperoni = $2, cheese = $1
medium pizza =  $20, pepperoni = $3, cheese = $1
large pizza =  $25, pepperoni = $3, cheese = $1
"""

# ------------------------------------------------------------------

print("Welcome to the Python Pizza Deliveries!")

size = input("What size pizza do you want? (s, m or l): ")
pepperoni = input("Do you want pepperoni on your pizza? (y/n): ")
extra_cheese = input("Do you want extra cheese? (y/n): ")
bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
else:
    bill += 25

if size == "s":
    if pepperoni == "y":
        bill += 2
else:
    bill += 3

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is ${bill}")


# ------------------------------------------------------------------
