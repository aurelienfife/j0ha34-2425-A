# This is the base code for the Y/N input validation
# Your job will be to integrate this into a function
# and complete exercise 3 of the link
# "Python Exercises Using Functions" on iLearn
#

user_input = input('Do you wish to continue? (Y/N)')
continuing = False
# Validation stage, criteria are Y/y/N/n
while user_input != 'Y' or user_input != 'y' or user_input != 'N' or user_input != 'n':
    print('Invalid input.')
    user_input = input('Do you wish to continue? (Y/N)')

if user_input == 'Y' or user_input == 'y':
    continuing = True
else:
    continuing = False

# Should the function return something?
