print("Welcome TO Fatima's Tip Calculator")

meal = float (input("Enter the cost of the food: "))
people = int (input(" Number of people splitting: "))
tip = int (input(" Enter your tip %: "))
tax = .10

# Time to calculate

tip_amount = meal * tip/100 
tax_amount = meal * tax
total = meal + tip_amount + tax_amount
amount_per_person = total / people

# Print statements

print(f"Your meal was ${meal} and your tip was ${tip_amount}")
print(f"Your total with tax was ${total}.")
print(f"Each diner should pay: {amount_per_person}")