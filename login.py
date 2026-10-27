from auth import *

def login() -> bool:
    print("Welcome to the bookmarker app! The place where your favorite books are.")
    #asking for the credentials of the user
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    while username == "" or password == "":
        print("Username and password cannot be empty. Please try again.")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
    validate = validate_user(username, password)
    if validate:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False