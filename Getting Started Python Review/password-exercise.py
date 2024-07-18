"""
Write a program that asks the user to enter a password ands compares it to a hard coded password

If the password is correct, the program prints "Greetings Professor Falcoin" and exits

If the password is incorrect, the program prints "Access denied" and then asks for the password again

The program will ask for the password three tims if necessary

After that, it exits
"""

PASSWORD = "aswd"

for i in range(3):
    
    verify = input("Enter Password:\n")
    
    if verify == PASSWORD:
        print("Welcome Professor Falcon")
        break
    elif i ==2:
        print("Access Denied. Authorities on the way!!!")
    else:
        p=i+1
        print("Access Denied... This is attempt " + str(p))

        
