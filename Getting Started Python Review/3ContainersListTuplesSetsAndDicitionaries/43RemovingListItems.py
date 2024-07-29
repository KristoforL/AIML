#Review of removing items from list

def main():
    
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    
    #You can be over simple and remove items with slicing
    days[0:3]= [] 
    print(days)

    #You can remove items in a list by name if you know them and the list are small
    days.remove("Sat")
    print(days)
    
    #You can remove them using the pop method which is a way you can remove the last item or you can remove an item at a specific index
    days.pop()
    print(days)
    days.pop(1)   
    print(days)
    
    #You can delete items at index with del keyword or delete the variable all together
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    del days[0]
    print(days)
    #The clear method will empy out an entire list as well
    days.clear()
    print(days)
    
    del days
    print(days)    
    
    
main()
