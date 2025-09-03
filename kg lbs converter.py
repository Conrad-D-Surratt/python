"""
Create a Python program that converts kilograms to pounds. Use at least four different samples to convert. A sample of the math is provided below;
do not use the same example in your program.

Kilograms to Pounds Conversion:
To convert kilograms (kg) to pounds (lb), use the formula:

Pounds (lb) = Kilograms (kg) * 2.20462

Example: 5 kg * 2.20462 = 11.0231 lb
"""

print()
weight = float(input("Enter the amount in kilograms that you'd like to convert to pounds: "))
pounds = weight * 2.20462
print()
print(f"{weight} kg is equal to {pounds:.2f} lbs." , "\n")
new_weight = float(input("Enter the amount in pounds that you'd like to convert to kilograms: "))
kilograms = new_weight / 2.20462
print()
print(f"{new_weight} lbs is equal to {kilograms:.2f} kg" , "\n")
#Empty print() lines added for visual clarity.
#Perhaps second_weight would be a better name that new_weight?