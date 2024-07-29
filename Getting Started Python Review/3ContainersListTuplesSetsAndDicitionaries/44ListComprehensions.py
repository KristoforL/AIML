#Review of quick easy ways to create list with list comprehensions

animals = ["dogs", "goats", "sloth", "tiger"]

#This does not make a copy of the same list and instead it will reference the same list
animals2 = animals
del animals[1]
print(animals)
print(animals2)

#Using the copy method will actually create a list for animals3 being its own variable
animals3 = animals.copy()
del animals3[1]
print(animals)
print(animals3)

#This a list comprehension and how they are structured. We userd the upper method to make the list distinct
animals4 = [animal.upper() for animal in animals]
print(animals4)

#This will print the length of the items in the list and not the length of the list itself
lengths = [len(text) for text in animals]
print(lengths)

#You can even do math with the items before they get put it in another list
numbers = [3,6,3,8,5]
numbers2 = [x*x for x in numbers]
print(numbers2)