# This will take a number and find the factorial of the number and return it to the console.

"""
Write a function that calculates the factorial of a number
The factorial of a number is defined like this

n! - n * (n-1)(n-2)(n-3)*...*3*2*1
eg:
3! = 3*2*1

The factorial of zero is defined as !

"""

#This was my way of doing this project
def greetings():
    print("Welcome to the factorial machine.")

def get_number():
    return int(input("What number do you want to solve the factorial of: "))

def factorial(number):
    
    if number == 0:
        return "Factorial of 0 = 1"
    else:
        x = number
        count = 1
        total = number
        while (number - count) != 0:
            y = total * (number-count)
            count = count + 1
            total = y
        return total

def main():
    number = get_number()
    print(factorial(number))

main()

#This is how the course recommended doing it
