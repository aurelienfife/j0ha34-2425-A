# Conditional loop
# Keyword: while
# Principle: repeat a section of code for as long as 
# a boolean condition is 'true'


index = 1
while index <= 5:
    print(index)
    index += 1


# Guess number game
answer = 8
guess = int(input('Enter a number between 1 and 10: '))

while answer != guess:
    print('Wrong guess!')
    guess = int(input('Try again. '))

print('Congratulations, you guessed well!')

# Grade a piece of coursework
# Input validation: will 'gatekeep' the running the program
# to data matching the criteria of your choice

# Below, the grading will only apply to numbers between 0 and 100

marks = int(input('Enter the marks for the coursework in %'))

while marks < 0 or marks > 100:
    print('This value is invalid, it needs to be between 0 to 100')
    marks = int(input('Enter the marks for the coursework in %'))

if marks >= 70:
    print('A')
elif marks >= 60:
    print ('B')
else:
    print('Fail or something')