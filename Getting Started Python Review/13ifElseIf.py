#Review of if else-if loop that will be reviewing multiple conditions in a loop


NAME = "JKL"
finished = "COMPELTED!!"

name = input("What is your name?: ")
name = name.upper()

if name == "JKL":
    print("Your name is " + name)

#There is no limit to how many else if sections there can be.
if name.title() == "Kris":
    print("Your name is " + name)
elif name == NAME:
    print('You name is '+ NAME)
else:
    print("Your name is not JKL or Kris")

print(finished)