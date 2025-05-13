'''
    Example of:
    - Menu based program with several options + input validation
    - Authentication using a username/password object
'''

# Objects
# Objects are new data types that can contain
# - Several properties (variables)
# - functions
# e.g. a string string.split()   <- it's an object
# another example: student.name  student.id etc.   <- student is an object

# new Class: user (just a single user)
class user_details:
    username = 'aurelien'
    password = 'password123'



# new class template for several objects
class user:     # Constructor function called __init__
    def __init__(self, username, password):
        self.username = username
        self.password = password

userlist = [] # Global list of users

def authenticate():
    # For login set-up an attempt counter
    attempts = 0

    # Run a while loop for under the 3 attempts
    while attempts < 3:
        # update to say a new attempt is taking place
        attempts+=1
        authenticated = False

        uname = input("What is your username?")
        upass = input("What is your password?")

        # If single user you can test on a single line, e.g.
        # if user_detail.username == uname and user_detail.password==upass
        
        # Check through list
        for checked_user in userlist:
            # check if username matches
            if checked_user.username == uname:
                # check if password matches
                if checked_user.password == upass:
                    print("Welcome, ", uname)
                    authenticated = True
        
        if authenticated:
            break # if authentication successful, break out of loop
        else: # if not authenticated
            print("username or password invalid")
            if attempts == 3:
                print("Program will exit")
                exit(0)

def menu():

    choice = 0

    print('''Here are the options:
1 - Coffee
2 - Tea
3 - Hot Chocolate
4 - Quit''')

    # Repeat loop unless quit was chosen
    while choice != 4:

        # Because of unsafe int conversion we'll use a try statement
        try:
            choice = int(input("Please make a selection"))
        # If the user enters a value not convertible to int, it may crash
        # The code below handles that case and sets value to an integer
        # that will just re-run the loop
        except ValueError:
            choice = 0

        # match/case statement
        # new since Python 3.10 - equivalent of switch/case in C/C++/JS etc
        match choice:
            case 1:
                print("You picked coffee")
            case 2:
                print("You picked tea")
            case 3:
                print("You picked hot chocolate")
            case 4:
                print("Bye.")
            case _:    # default case
                print("Option not recognised, please try again.")
                
def main():
    # Create a couple of username/password combinations
    user1 = user("aurelien", "password123")
    user2 = user("arthur", "123password")
    userlist.append(user1)
    userlist.append(user2)

    authenticate()
    menu()


if __name__ == "__main__":
    main()