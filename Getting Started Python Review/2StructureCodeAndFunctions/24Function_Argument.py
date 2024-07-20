# Reviewing function arguments

#Functions can take in the input from a users input or calculation somewhere else in the code but the argument will need to be in argument section so the code knows what it is using
def greet(user):
    print("Hello " + user)
    
def main():
    name = input("What is your name? > ")
    greet(name)

#Dont forge to call your functions.
main()