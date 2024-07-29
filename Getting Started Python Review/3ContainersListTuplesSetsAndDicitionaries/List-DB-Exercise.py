"""
    CRUD
    
    Create a progeam that siplays the following menu

    1.Display database
    2.Add an item
    3.Delete an item
    4.Change an item
    5.Quit
    
    The program contains a list of items; for example fruits
    
    If you select 1m, the program displays the items in the list, numbering each item. For exmaple:
    
    0: orange
    1: banana
    2: blackberry

    If you select 2 the program asks you to enter a new item. It adds what you've typed to the list.
    
    If you select 3, the program asks you to enter the list number of an item to delete. It deletes the specified item from the list
    
    If you select 4, the program asks you to enter the list number of an item to change then ask you to enter text. It changes the specified item to the specified text.
    
    If you select 5, the program quits.
    
    Until you quit with option, the program displays the menu again after every action.
    
"""

MY_LIST = ["Ramen", "Ice Cream", "Smoothies", ""]

def greet():
    welcome = input("Please make a selection \n1.Display database \n2.Add an item \n3.Delete an item \n4.Change an item \n5.Quit\n")
    
def addItem():
    pass


greet()