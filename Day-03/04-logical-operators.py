height = float(input("Enter your height in cm: "))
total_bill = 0

if height > 120:
    print("You can ride the roller coster!")

    age = int(input("Enter your age: "))
    if age < 12:
        total_bill += 5
    elif age <= 18:
        total_bill += 7
    elif age >= 45 and age <= 55:
        print("You tickets are free!")
    else:
        total_bill += 12

    want_photos = input("Do you want photos? (y/n) ")
    if want_photos == "y":
        total_bill += 3
        print(f"Please pay ${total_bill}")
    else:
        print(f"Please pay ${total_bill}")

else:
    print("You cannot ride the roller coster!")

""" 
NOTE:
- and (both must be true)
- or (any one must be true)
- not (must be false to return true)
"""
