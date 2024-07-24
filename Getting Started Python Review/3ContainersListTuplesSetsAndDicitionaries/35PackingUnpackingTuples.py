#Review of packing and unpacking tuples or assigning values 


#Tuples are data structures that cannot change

def main():
    elements = (True, 3.14, 7, "Goated")
    #This assigns values keys to the values in the tuple above and it is in the speific order for this case
    (is_raining, weight, volume, animal)= elements
    
    print(is_raining)
    print(weight)
    print(volume)
    print(animal)
    
    fruits = ("Apple","orange", "banana", "strawberry", "grape")
    #This assigns values to the tuple but it 
    (fruit1, *more_fruits, fruit2, fruit3) = fruits
    
    print()
    print(fruit1)
    print(fruit2)
    print(fruit3)
    print(more_fruits)   
    
    #When using one item for a tuple it will be a list
    one_item = ("goat")
    print(type(one_item))
    
    #When you use a comma after the tuple item it will then be read as a tuple
    one_item = ("goat",)
    print(type(one_item))
    
main()

