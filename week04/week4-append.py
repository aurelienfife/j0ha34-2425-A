# Create empty list

students = []

for index in range(5):
    s = input('Enter the name of a student')
    students.append(s)

print(students)


students[2] = 'boris'

print(students)