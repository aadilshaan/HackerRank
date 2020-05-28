# Class vs. Instance

class Person:
    def __init__(self,initialAge):
        self.age = 0
        if initialAge < 0:
            print('Age is not valid, setting age to 0.')
        else:
            self.age = initialAge
    def amIOld(self):
        if age < 13:
            print('You are young.')
        elif age >= 13 and age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')
    def yearPasses(self):
        global age
        age += 1
for _ in range(int(input())):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0,3):
        p.yearPasses()
    p.amIOld()
    print('')
