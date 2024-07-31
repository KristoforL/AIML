#Review of Sets and removing items from them

#You can even create sets with list comprehension
numbers = {x for x in range(15)}
print(numbers)

#There are a few ways to remove items from sets
numbers.remove(6)
print(numbers)

#If you try to remove an item from the set that is not there you will get an error
#numbers.remove(20)

#The other way to remove items is to use discard
numbers.discard(20)
print(numbers)

#Even though you print a set like this you cannot rely or the order of numbers, so avoid using method like this to print the sets out
for x in numbers:
    print(x) 
    


    
    
    