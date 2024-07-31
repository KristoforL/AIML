#Review of Sets

#Sets use curly brackets and fun thing about sets every entry needs to be unique
numbers = {1, 2, 3, 1}
print(numbers)

#Because of that fun fact when you print a set it will only show the uniwue items even though there may be more items in
numbers_list = [ 2,3, 3, 2, 5, 6]
print(set(numbers_list))

#You cannot print one item in a list but you can loop through the items in a set
#print(numbers[1])

for number in numbers:
    print(number)
 
#Will let you know if an item is in a list and if it is then it will be returning a boolean
print(3 in numbers)  
print("3" in numbers)  
    
    
"""
List: Ordered, "in" is slow, mutable
tuple: ordered, "in" is slow, immutable
set: not ordered, "in" is fast, mutable
"""