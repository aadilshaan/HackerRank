# Intro to Conditional Statements

num = int(input())
if num%2 == 1:
    print('Weird')
elif num <= 5:
    print('Not Weird')
elif num <= 20:
    print('Weird')
else:
    print('Not Weird')