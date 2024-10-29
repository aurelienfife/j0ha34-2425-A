# Example - lists

shopping_list = ['apples', 'bananas', 'milk', 'bread']

print(shopping_list)

# First element is positioned at 'zero'
# If you have n elements in the list, the first one is 0, the
# last one is n-1

print(shopping_list[0])
print(shopping_list[3])

# print(shopping_list[6]) # error

print(len(shopping_list))
print(shopping_list[len(shopping_list) - 1])

# Shortcut to last element
print(shopping_list[-2])

# Show several elements
print(shopping_list[1:3])

print(shopping_list[:3])
print(shopping_list[1:])


# Pretty much all the above can apply to strings instead

text = "Hello World today something"


print(text[0])
print(text[3])

# print(text[6]) # error

print(len(text))
print(text[len(text) - 1])

# Shortcut to last element
print(text[-2])

# Show several elements
print(text[1:3])

print(text[:3])
print(text[1:])
