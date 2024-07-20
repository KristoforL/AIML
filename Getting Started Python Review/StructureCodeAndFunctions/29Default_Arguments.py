# Reviewing default arguments


#This is an example of assigning arguments default values
def patient(name="fred", age=20, kids=False):
    print("NEW PATIENT:\n-Name:", name, "\n-Age:", age, "\n-Kids:", kids)


def main():
    patient("JKL", 30, False)
    patient("Toni", 25, True)
    patient("Lorena", 50, True)

    
main()