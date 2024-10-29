# For loops - Fixed loops

# nums = [1,2,3,4,5]

# for n in nums:
#     print('5 x',n,'=',n*5)

# For large number ranges, it's not convenient, there's
# a type called 'range' doing this

# Display the 100 first numbers

for n in range(100):
    print(n)

# range(start,end,step_direction)

print()
print()

# The 100 first numbers -> effectively
for n in range(1,101):
    print(n)

print()
print()

for n in range(1,101,5):
    print(n)

# Countdown
for n in range (10,0,-1):
    print(n)



# Practical applications - go through lists
students = ['Kadie', 'Erik', 'Andrew', 'Luka','Valentin','Kristian']

for i in range(len(students)):
    print('Position:',i,students[i])

# You can avoid using an index if you do not need it
# Note: no keeping track of index
for name in students:
    print(name)


# Just like with lists/strings, loops can be used on strings
phrase = 'To be or not to be? That is the question.'

for c in phrase:
    print(c)