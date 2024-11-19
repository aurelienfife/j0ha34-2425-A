'''
Count how many times a value appears in a collection
e.g. a list etc

1. Initialise counter to 0
2. For every element in a list/array etc
    2.1 if element matches search term
        2.2 increase counter by one
2.3 End loop

'''

import random

# Generate a list of 50 numbers between 1 and 10
def generate_random():
    nums = []
    for index in range(50):
        nums.append(random.randint(1,10))
    return nums

number_list = generate_random()
print(number_list)

val = int(input("What number are you looking for?"))
# Validate
while(val < 1 or val > 10):
    val = int(input("Out of bounds, what number are you looking for?"))

# Counting occurrences
counter = 0
for number in number_list:
    if number == val:
        counter += 1

print(val, "appears", counter, "time(s)")

