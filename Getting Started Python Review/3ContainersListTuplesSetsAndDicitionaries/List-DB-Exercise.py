"""
    CRUD
    
    Done: Create a program that displays the following menu

    1.Display database
    2.Add an item
    3.Delete an item
    4.Change an item
    5.Quit
    
    The program contains a list of items; for example fruits
    
    Done: If you select 1, the program displays the items in the list, numbering each item. For exmaple:
    
    0: orange
    1: banana
    2: blackberry

    Done: If you select 2 the program asks you to enter a new item. It adds what you've typed to the list.
    
    Done: If you select 3, the program asks you to enter the list number of an item to delete. It deletes the specified item from the list
    
    If you select 4, the program asks you to enter the list number of an item to change then ask you to enter text. It changes the specified item to the specified text.
    
    If you select 5, the program quits.
    
    Until you quit with option, the program displays the menu again after every action.
    
"""

MY_LIST = ["Ramen", "Ice Cream", "Smoothies", "Gyoza", "Chicken Sandwich"]
OPTIONS = ("1. Display database", "2. Add an item", "3. Delete an item", "4. Change an item", "5. Quit\n")

def greet():
    for i in OPTIONS:
        print(i)
    select = int(input("Pick an option: "))
    
    return select
    
def display():
    x = 1
    for item in MY_LIST:
        print(str(x) + ". " + item)
        int(x)
        x+=1
    print("Items displayed")
    print()
        
def addItem():
    adding = input("What would you like to add to the list?: ")
    MY_LIST.append(adding)
    print("item Added")
    print()

def delete():
    adding = int(input("What number item would you like to remove to the list?: "))
    size = len(MY_LIST)
    if adding not in range(0, size):
        print("Sorry number not in range")
    else:
        MY_LIST.pop(adding-1)
        print("Item removed")
    
    print()

def change():
    adding = int(input("What number item would you like to change to the list?: "))
    size = len(MY_LIST)
    if adding not in range(1, size+1):
        print("Sorry number not in range")
    else:
        sub = input("What you like to change it to: ")
        MY_LIST[adding-1] = sub
        print("item changed")
    print()

def CRUD():  
    Go = True
    while Go:
        number = greet()
        if number in range(1,6):
            if number == 1:
                display()
            elif number == 2:
                addItem()
            elif number == 3:
                delete()
            elif number == 4:
                change()
            else:
                Go = False
                print("Thank you for participating")
        else:
            print("Not a valid entry.Try Again")

CRUD()