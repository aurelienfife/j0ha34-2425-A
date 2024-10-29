'''
Look at the following list of numbers

thesenumbers = [1,7,9,4,2,9,12,13,17]
Loop through the items in this list and add them up.
Output the total (hint declare total=0 at the start)

Get the length of the list and work out the average number
in the list by dividing the total by the length - output the average number.
'''

thesenumbers = [1, 7, 9, 4, 2, 9, 12, 13, 17]

total = 0

# 'Easy way' -> in this scenario it's easier to use that
for index in thesenumbers:
    total = total + index

# 'Hard way' -> if you need to access the array value via position
# for index in len(thesenumbers):
#    num = thesenumbers[index]
#    total = total + num

average = total / len(thesenumbers)
print('The sum of all the numbers:', total)
print('The average of all the numbers:', average)