# Function is self-contained and returns the result
# The programmer can then elect to do what they need
# With the result

def reverse_upper(a_string): # Formal parameter (placeholder)
    # Reverse the string
    reverse_string = a_string[::-1]
    upper_string = reverse_string.upper()
    return upper_string


## Examples of a function
# Function taking a string, reversing it, turning it uppercase

quotes = []
quotes.append("To be or not to be, that is the question.")
quotes.append("As Gregor Samsa awoke one morning from uneasy dreams he found himself transformed in his bed into an enormous insect")
quotes.append("Hamburgers! The cornerstone of any nutritious breakfast.")

f = open('quotes.txt','w')

for q in quotes:
    r = reverse_upper(q)
    # Additionally to printing we want to save the quotes in a file
    print(r)
    f.write(r+'\n')

f.close()
