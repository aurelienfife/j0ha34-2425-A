'''
    This script opens:
    - a credentials username / password hash CSV file
    - a most common passwords text file

    Then loops through the (clear) passwords, hash them.

    If there's a match with an existing hash, display as found.
    29/04/2025 - AA

    Caveats:
    - We know that the hash in use is SHA256
    - There's no salt in the password hashes
'''
import hashlib

# Global variable: credentials
cred = {} # empty dict

def load_credentials():
    # Open file
    f = open("leakedcredentials.csv")

    # Split every line and store in dictionary
    for line in f:
        item = line.split(',')
        pass_hash = item[1].strip() # Remove new line

        cred[item[0]] = pass_hash  # key: username, value: password hash

    f.close()

def check_passwords():
    # Outer loop -> go through every leaked hash
    for username in sorted(cred.keys()):
        current_hash = cred[username]

        print("Solving password for:", username)
        print("-"*20)
        # Open the passwords file and go through them

        p = open("10k-most-common.txt")

        # Go through every password
        for password in p:
            if compare_password(password, current_hash):
                pass


def compare_password(clear_password, leaked_hash):
    pass

def main():    
    # Load the main credentials
    load_credentials()

    # Check individual hash vs password list
    check_passwords()

if __name__ == "__main__":
    main()