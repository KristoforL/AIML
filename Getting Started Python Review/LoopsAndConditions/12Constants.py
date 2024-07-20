#Review of constants so that in coding there is no problem with contantly typing a number or string

#Constants as best practice should not be changed and should have a note around them so there is an explanation as to why

NAME = "JKL"
finished = "COMPELTED!!"

name = input("What is your name?: ")
name = name.upper()

if name == "JKL":
    print("Your name is " + name)


if name == "Kris":
    print("Your name is " + name)
else:
    print('You name isnt Kris')

print(finished)