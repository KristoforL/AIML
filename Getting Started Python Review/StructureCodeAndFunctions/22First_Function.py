# Making first function

"""
Procedural: C
OOPS: Java
Functional: Haskell

Python fits in all these categories
"""

# response = input("How are you? ")

# if response == "OK" or response == "ok":
#     print("Excellent")
# else:
#     print("oh no")
    

def ask_user_status():
    response = input("How are you? ")

    if response == "OK" or response == "ok":
        print("Excellent")
    else:
        print("oh no")
        
        
ask_user_status()