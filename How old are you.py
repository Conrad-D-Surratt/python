"""Write a Python program that uses if-else statements and:

Asks the user for their age and converts the input to an integer.
Check to see if the user is old enough to drive.
Check to see if the user can vote.
Check to see if the user can legally buy alcohol.
Check to see if the user is eligible for a senior discount.
Prints all the results on the screen, ensuring the output is straightforward and user-friendly.
"""
print()
users_age = float(input("How old are you? ")) #The user can enter the number as a float.
print() #Lines 1 and 3 are blank for visual clarity.
int_age = int(users_age) #This line converts the float number into an integer
if int_age >= 15:
    print("You are old enough to drive")
else:
    print("You are not old enough to drive")
if int_age >= 18:
    print("You are able to vote")
else:
    print("You are not old enough to vote")
if int_age >= 21:
    print("You are able to buy alcohol")
else:
    print("You cannot legally buy alcohol")
if int_age >= 65:
    print("You are eligible for a senior discount\n")
else:
    print("You are not eligible for a senior discount\n") #Lines 18 and 20 also add some blank lines for visual clarity.
print("(Note that some some organizations or businesses may offer senior discounts or benefits at different ages, such as 55 or 60.)\n") #Found out this info on Google.
#Simple if and else statements for this. Didn't see the need to use elif, although I could have.