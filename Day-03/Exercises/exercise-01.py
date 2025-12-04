# Write a program to print the bmi and give related interpretations.

# ---------------------------------------------------

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meter: "))

bmi = weight / (height**2)

if bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("underweight")
# ---------------------------------------------------
