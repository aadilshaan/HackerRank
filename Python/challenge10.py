# Nested Lists

num = int(input())
marksheet = [[input(),float(input())] for _ in range(num)]
second_lowest = sorted(list(set([mark for name,mark in marksheet])))[1]
second_name = [name for name,mark in marksheet if mark == second_lowest]
second_name = sorted(second_name)
for name in second_name: print(name)
