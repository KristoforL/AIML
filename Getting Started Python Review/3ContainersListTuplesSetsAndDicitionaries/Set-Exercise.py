import math


"""

Print all the cubic numbers up to and including 729
Print all the square numbers up and including 729

Which cubic numbers are also square numbers?
Which cubic numbers are not square numbers?

"""

#I could not figure out how to do it my way

cube = []
square = []


def sqrt():
    for x in range(int(math.sqrt(784))):
        print(x)
        square.add(x)

def cube():
    pass


def main():
    sqrt()


#This is how the instructor did it

def main():
    
    #This will print all cubic numbers up to 729
    cubic = {x**3 for x in range(10)}
    print(cubic)
    
    #This will print all square numbers up to 729
    square = {x**2 for x in range(28)}
    print(cubic)
    
    #These are the cubic numbers that are square
    print(cubic.intersection(square))
    
    #This will show which cubic numbers are not square numbers
    print(cubic - square)
    

main()