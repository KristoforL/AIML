#Review of tuple functions and operators

number1 = 1,2,3,4,5,6,7

#Built in functions that work well in other areas as well but these are good for finding length of tuples, minimums and maxes
print(len(number1))
print(min(number1))
print(max(number1))

#Thisn is a way to count the number of a specific entry in the tuple
print(number1.count(3))
#This will print out the first occurance og the arugments location in the tuple
print(number1.index(3))

#You can even add tuples together and multiply them
print(number1 + (10, 20))
print((1,2,3) * 3)

#Remember that for a tuple to be typed as a tuple it only needs an object followed by a comma and that is as of python version 3.12.4 which may change later on