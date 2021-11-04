import numpy as np



print('Welcome to Quick Tip Calculator')
total_bill = float(input("What was the total price of your bill?: "))
percentage_tip = int(input('how much tip do you want to leave? 10,12,15,20: '))
number_of_people = int(input("How many people are splitting the bill?: "))
group_meal_with_tip = (round(float(((percentage_tip / 100 + 1) * total_bill) / number_of_people), 2))
tip_amount = "%.2f" % float(percentage_tip / 100 * total_bill)
print(f'Tip amount: ${tip_amount} ')
total_bill_float = float(total_bill)
tip_amount_float = float(tip_amount)
tip_and_total = (total_bill_float + tip_amount_float)
print(f'Total bill including your tip: ${tip_and_total}' )
print(f"Each person owes: ${group_meal_with_tip} ")























