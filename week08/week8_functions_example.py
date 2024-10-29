# Function -> write code in the aim to re-use it

# Function adding two variables (irrespective of type)
def add(a, b):
    c = a + b
    return c


def main():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))

    # call function to perform operation
    tot = add(num1, num2)

    print('The result is', tot)

# This checks if the file is loaded as "program"
# instead of "module" and runs main
if __name__ == '__main__':
    main()