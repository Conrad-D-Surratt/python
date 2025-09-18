"""In this exercise, you will practice using logical operators (and, or, not) in Python. Your task is to create a program that
  prompts the user for two integer inputs and then demonstrate the use of these operators.

User Input: Start by asking the user to input two distinct integers. 
Logical Operators: Implement six different logical comparisons using the input integers. Include two examples for each of the following operators:
and
or
not
Display Results: Print the logical statement and its result for each comparison.
Guidelines for Logical Comparisons:
Ensure that your comparisons are meaningful and not too obvious (e.g., avoid comparisons like num1 == num1).
Try to use comparisons that could yield different results based on user input."""

user_input = float(input("\nEnter an integer: "))
user_input_two = float(input("Enter another integer: ")) #I'm not trusting the user to enter an integer.
print()
int_one = int(user_input)
int_two = int(user_input_two) #Converts the floats into integers.
if int_one > 0 and int_two > 0:
    print("Both numbers are greater than 0")
if int_one > 100 and int_two > 100:
    print("Both numbers are greater than 100") #Two and statements.
if int_one % 2 == 0 or int_two % 2 == 0:
    print("At least one number is even")
if int_one < 100 or int_two < 100:
    print("At least one of the numbers is less than 100") #Two or statements.
if not int_one == int_two:
    print("The numbers are not equal")
if not int_one == 0:
    print("The first number is not zero") #Two not statements.
print()
#A couple of blank lines for visual clarity. This was a fun one to figure out!