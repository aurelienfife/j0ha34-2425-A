''' 
Input validation:
Mechanism ensuring the input is within established
parameters, e.g. a numerical range, a list of values etc

Example in pseudo-code:

1 Initialise age 
2 Get age from user, display "How old are you?"
3 While age is not within the range 18-59 years old do:
    3.1 Display "To use this, you need to be aged 18-59"
    3.2 Get age from user
3.4 Done
4 Display "Welcome"

'''

# Actual Python version
age = int(input("How old are you?"))
while age < 18 or age > 59:
    print("To use this, you need to be aged 18-59")
    age = int(input("How old are you?"))
print("Welcome")
