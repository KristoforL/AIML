#How to return multiple things

def get_user_info():
    name = input("Enter your name> ")
    height = input("Enter your height> ")

    return name, height

def main():
    #This is how you might call multiple returns from to another function
    name, height =  get_user_info()
    print(name + " : "+ height)

main()