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
    pass

def check_passwords():
    pass

def compare_password(clear_password, hash):
    pass

def main():    
    # Load the main credentials
    load_credentials()

if __name__ == "__main__":
    main()