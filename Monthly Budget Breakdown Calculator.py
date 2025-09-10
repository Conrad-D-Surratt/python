"""Create a Python application that allows users to input their total budget and the amount spent in various categories.
The program will then calculate and display the percentage of the total budget each category represents.
Requirements:
Design a Python program that prompts users to enter their total budget (ask them for their net monthly income) and amounts for spending categories:
Housing (rent or mortgage)
Utilities
Groceries
Transportation
Health Care
Personal Care
Clothing
Debt
Calculate the percentage of the total budget spent in each category.
Tell the user how much the spent total, and how much money they have left. 
Display the results in a user-friendly format using f-strings.
Ensure your code is well-commented to explain the functionality of different sections."""

#Nice little greeting, maybe too enthusiastic.
print("Hello and welcome to my monthly budget breakdown calculator! \nPlease enter in your financial information to get started. \n")
monthly_income = float(input("Net monthly income: $"))
housing = float(input("Housing (mortgage or rent): $"))
utilities = float(input("Utilities: $"))
groceries = float(input("Groceries: $"))
transportation = float(input("Transportation: $"))
health_care = float(input("Health Care: $"))
personal_care = float(input("Personal Care: $"))
clothing = float(input("Clothing: $"))
debt = float(input("Debt: $"))
#Used float for each one although users likely won't enter decimal spaces.
total_spent = housing + utilities + groceries + transportation + health_care + personal_care + clothing + debt
remaining = monthly_income - total_spent
#Storing these additions in a new variable to add at the end.
housing_percent = (housing / monthly_income) * 100
utilities_percent = (utilities / monthly_income) * 100
groceries_percent = (groceries / monthly_income) * 100
transportation_percent = (transportation / monthly_income) * 100
health_care_percent = (health_care / monthly_income) * 100
personal_care_percent = (personal_care / monthly_income) * 100
clothing_percent = (clothing / monthly_income) * 100
debt_percent = (debt / monthly_income) * 100
#Dividing and then multiplying by 100 to get the percentages right
print("\nMonthly Budget Summary: \n")
print(f"Total Spent: ${total_spent:.2f}")
print(f"Remaining: ${remaining:.2f}\n")
print("Spending Percentages: \n")
print(f"Housing:        {housing_percent:.2f}%")
print(f"Utilities:      {utilities_percent:.2f}%")
print(f"Groceries:      {groceries_percent:.2f}%")
print(f"Transportation: {transportation_percent:.2f}%")
print(f"Health Care:    {health_care_percent:.2f}%")
print(f"Personal Care:  {personal_care_percent:.2f}%")
print(f"Clothing:       {clothing_percent:.2f}%")
print(f"Debt:           {debt_percent:.2f}%")
#Added some blank lines for visual clarity and rounded the percentages to two decimal places for the same reason.