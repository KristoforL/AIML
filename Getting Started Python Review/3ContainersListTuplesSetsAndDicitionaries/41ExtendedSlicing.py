#Review of extended slicing

numbers = ["zero","one","two","three","four","five","six","seven"]

#You can show the slice you want to see and then increment by the third argument like slicing or like range method
print(numbers[3:7:2])

numbers[3:7:2] = ["hello", "hi"]
print(numbers)
#This will also print the entire list
print(numbers[::])

#Strings are seen as list in python and can be evaluated the same way
greetings = "hello there"
print(greetings[2])
#Also spaces also are counted in strings so watch out for that when incrementing
print(greetings[::2])
#You can apply slice inside print statements
print("What are you?" [3::3])