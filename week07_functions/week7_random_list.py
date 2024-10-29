'''

Write a program which creates a list of random numbers then outputs the list of random numbers. We have done something similar before! But this time:
•	The main code will welcome the user and tell them what will happen
•	We will write a function called create_list to create the list of random numbers
•	This function will take no parameters, and will return the list it has created
•	This function will be called by the Main code, and after it has completed, the Main code will have the new list and can print out the numbers in it

'''

import random

def create_list():
    # Empty list at start
    num_list = []
    for counter in range(10):
        num_list.append(random.randint(1,100))

    # List created - return it
    return num_list

# To avoid issues when reusing your code as a module
# You need to isolate your main program as a function itself

def main():
    print("Hi, I will pick 10 random numbers between 1 and 100")
    rand_list = create_list()
    print("Here is the list")
    print(rand_list)

# You call to main when running this as a program
# But guard it from running if loaded as an external module
if __name__ == "__main__":
    main()
