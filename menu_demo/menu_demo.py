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

def main():
    # Create a couple of username/password combinations
    user1 = user("aurelien", "password123")
    user2 = user("arthur", "123password")
    userlist.append(user1)
    userlist.append(user2)

    authenticate()

if __name__ == "__main__":
    main()