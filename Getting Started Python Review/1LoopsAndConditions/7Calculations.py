
##Utilizing the input function to accomplish taking input in from the user

greeting = "Hello World\n"

name = input("What is your name? ")
age = input("How old are you? ")
years = 100 - int(age)
years = str(years)

print("Hi " + name)
print("You have " + years + " years before you are 100 years old")

