# A function that doesn't return a value is also called
# a 'procedure' 

def reverse_upper(a_string): # Formal parameter (placeholder)
    # Reverse the string
    reverse_string = a_string[::-1]
    upper_string = reverse_string.upper()
    print(upper_string)


## Examples of a function
# Function taking a string, reversing it, turning it uppercase

some_string = "To be or not to be, that is the question."
another_string = "As Gregor Samsa awoke one morning from uneasy dreams he found himself transformed in his bed into an enormous insect"
pulp_fiction = "Hamburgers! The cornerstone of any nutritious breakfast."

reverse_upper(some_string)
reverse_upper(another_string)
reverse_upper(pulp_fiction)

