# Finding the percentage

number_of_students = int(input())
students_marks = dict()
for lines in range(number_of_students):
    line = input().split()
    scores = list(map(float,line[1:]))
    students_marks[line[0]] = scores
student_name = input()
print('{:.2f}'.format(sum(students_marks[student_name])/len(students_marks[student_name])))
