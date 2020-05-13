# Operators

def total(meal_cost,tip_percent,tax_percent):
    tip_cost = meal_cost * (tip_percent/100)
    tax_cost = meal_cost * (tax_percent/100)
    total_cost = meal_cost + tip_cost + tax_cost
    return total_cost
meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())
total_cost = total(meal_cost,tip_percent,tax_percent)
print(round(total_cost))
