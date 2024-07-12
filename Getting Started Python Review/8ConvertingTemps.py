

F = input("What is the temp in Fahrenheit?: ")
F = int(F)

C = (F-32) * (5/9)
C = str(C)
F = str(F)

print("You said it was " + F + " Degrees Fahrenheit\nThat means it is " + C + " degrees Celsius")