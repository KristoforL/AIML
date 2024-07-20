# Reviewing return values and how they can be utliized from function to function

#Returns do not print but rather return a value in like the form of a arugument or parameter

def greet(name):
    print("Hello " + name)

def create_greeting(name):
    return "Hi "+ name

def create_simple_greeting():
    return "Hi There"

def main():
    name = "John"
    greet(name)

    #The return of create greeting becomes the variable for greeting
    greeting =  create_greeting(name)
    #Remember that when something is a return you have to explicitly print it
    print(greeting)

    #Create_simple_greeting just returns a string and here the string becomes the variable for simple greeting
    simple_greeting = create_simple_greeting()
    #Remember that when something is a return you have to explicitly print it
    print(simple_greeting)
    
main()