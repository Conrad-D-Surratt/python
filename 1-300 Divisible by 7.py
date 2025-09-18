"""Write a Python program to find and print all numbers divisible by 7 between 1 and 300.
 Use a for loop and the modulus operator (%)."""

print("\n Here's a list of every number 1-300 that is divisible by 7:\n") #Just to make it more visually pleasing.
for i in range(1, 300):
    if i % 7 == 0:
        print(i) #Divides the number range by 7 and then prints the outcomes.
    elif i / 7 == 42:
        break #Once it is equals 42, it breaks the process.
print("\nThat's all 42 of the numbers between 1-300 that are divisible by 7!\n") #More visually pleasing lines for the end user.