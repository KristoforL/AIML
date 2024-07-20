# Reviewing ID Functions

#You ID the variables that you use in your functions to ensure the variables are different or the same

def greet(name):
    print(id(name))
    print("Hello " + name)


def main():
    name = "John"
    
    print(id(name))
    greet(name)


    
main()