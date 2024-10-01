# Check for perfect squares

print('Enter a number')
number = input()
# abs -> converts negative to positive
number = abs(int(number))

# Start from -1, which cannot be a square36
# One-by-one check every integer between
# 0 and sqrt of number
i = -1
# Assume num is not perfect
square = False

while i <= number**0.5:
    i += 1
    # If i is sqrt of number
    if i*i == number:
        square = True
        break

if square:
    print('The square root of', number, 'is', i, '.')
else:
    print('Not a perfect square')