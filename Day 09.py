# Recursion 3

def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)
number = int(input())
number_factorial = factorial(abs(number))
print(number_factorial)