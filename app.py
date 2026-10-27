from main import *
from login import login
import time

def main():
    #this is the main function that is going to run the program
    #it is going to ask for the user to login and then it is going to show the menu
    #if the user is not logged in, it is going to ask for the user to login again
    successfull = login()
    if(successfull):
        print("Welcome to the platform user! You are now logged in. We're redirecting you in...")
        time.sleep(3)
        show_cli()
    else:
        print("Wrong username or password. Please try again.")


if __name__ == "__main__":
    main()