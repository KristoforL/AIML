# Making multiple functions

PASSWORD ="hello"

#Can create multiple functions to carry out multiple task easily
def greeting():
    print("Welcome! No unauthorised users")

def check_password():
    password = input("Enter your password > ")

    if password == PASSWORD:
        print("Access Granted")
    else:
        print("Access Denied")
        
#Can create a function to run other functions so that you can group functions that are supposed to work with each other
def main():
    greeting()
    check_password()
    
#Functions will not run when they are not called
main()