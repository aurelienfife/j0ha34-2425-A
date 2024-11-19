'''

Find min/max

You have a list of values (numbers, words etc)

Find max:
1. Set max to first value in list
2. For each value in list (from the second) do
   2.2 if current value is greater than max
   2.3 set max to current value
2.4 Next iteration

Find min:
1. Set min to first value in list
2. For each value in list (from the second) do
   2.2 if current value is lower than min
   2.3 set min to current value
2.4 Next iteration

'''

# Age range
ages = [18, 19, 19, 17, 25, 21, 37, 26, 15]

# Finding maximum
maximum = ages[0]
for index in range(1,len(ages)):
    if ages[index] > maximum:
        maximum = ages[index]

print("The greatest value is", maximum)