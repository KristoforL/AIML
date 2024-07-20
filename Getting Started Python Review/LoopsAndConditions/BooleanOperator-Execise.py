
"""
Write a program that asks the user three questions

Ask the user:
Are you a student?
Do you have pets?
Do you smoke?

The program automatically decides whether a property you've applied to rent is available to you

It should print an appropriate response, like "Property available" or "Property Unavailable"

The program applies these criteria

If you are a student, you can only rent the property if you don't have pets and don't smoke
If you are not a student you can only rent the property if you smoke or have pets not if you both smoke and have pets

"""



STUDENT =True
PETS = True
SMOKER = True

student = input("Are you a student (y/n)? ")
pets = input("Do you Pets (y/n)? ")
smoker = input("Are you a smoker (y/n)? ")
print("Thank you for your patience. Evaluating...")

if student.lower() == "n":
    STUDENT = False
if pets.lower() == "n":
    PETS = False
if smoker.lower() == "n":
    SMOKER = False
    
if STUDENT == True:
    if  SMOKER == True or PETS == True:
        print("Property Unavailable")
    else:
        print("Property Available")
elif STUDENT == False:
    if  SMOKER == True and PETS == True:
        print("Property Unavailable")
    else:
        print("Property Available")
