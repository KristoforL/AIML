
##Utilizing the input function to accomplish taking input in from the user

greeting = "Hello World\n"
status = "What is your name?"
print(greeting + status)

response  = input()

print("\nHello " + response + "." + "\nNice to meet you!")

## Can easily substitute the print function all together with the input so you can make a variable of it for easy storage
##
pie = input("Do you like pie "+ response+"? Y/N: ")
PL = pie.lower()


## Ahead of the curve here but if else loops to handle reason and responses
if pie.lower() == "y":
    print("I like pie too")
    
elif pie.lower() == "n":
    print("That is a shame")
    
else:
   print("Improper ")