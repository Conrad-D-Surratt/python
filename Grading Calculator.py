"""Accept a numeric grade from the user and display a letter grade. The  grading scale is  90 - 100: A, 80-89: B, 70-79:C, 60-69:D, Below 60: F

Check to see if the number given is between 0 and 100."""

grade = float(input("\nPlease enter your grade as a numeric number: ")) #A lot of people will likely enter decimals for their grade. A float is best here.
if grade > 100:
    print("\nIt seems your letter grade is an A++!\n") #Extra credit is possible, although I was just trying to be funny.
elif grade >= 90:
    print("\nYour letter grade is an A\n")
elif grade >= 80:
    print("\nYour letter grade is a B\n")
elif grade >= 70:
    print("\nYour letter grade is a C\n")
elif grade >= 60:
    print("\nYour letter grade is a D\n")
elif grade >= 0:
    print("\nYour letter grade is an F\n")
else:
    print("\nIt seems that your letter grade is an F-\n") #People would likely enter negatives eventually. Needed to cover for that as well. Also kinda funny haha.
#Using \n at the beginning and end of each print just for visual clarity. I feel that it makes the code look a little messier though compared to blank print lines.