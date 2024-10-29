import math

''' In this activity, you will assign a number to the x variable, increment the number, and perform additional operations. By completing this activity, you will learn how to perform multiple mathematical operations using Python. This activity can be performed in the Jupyter Notebook, interactive mode, or a script.

The steps are as follows:

First, set 14 to the x variable.
Now, add 1 to x.
Finally, divide x by 5 and square it.
'''

x = 14
x += 1
x = (x / 5) ** 2

print(x)

'''Create two variables l and w - length and width of a room, assign integer values of your choice. Calculate the surface area (l * w). Try varying the values and see the new results.'''

l = int(input('Enter the length'))
w = int(input('Enter the width'))

s = l * w

print(s)

'''
Other activities:

Create two variables l and w - length and width of a room, assign integer values of your choice. Calculate the surface area (l * w). Try varying the values and see the new results.
Create two variables a, b, lengths of two sides of a square rectangle. Create a variable h for hypothenuse. Using the Pythagorean theorem, calculate the length of the hypothenuse.'''

a = 4
b = 7

c = math.sqrt(a**2+b**2)

print(c)