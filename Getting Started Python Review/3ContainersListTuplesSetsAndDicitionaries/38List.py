#Review of list and how they may vary from tuples


def main():
    fruits = ["apple", "orange", "banana"]
    
    #Can use th len function as it is a universal function built it
    print(len(fruits))
    #Can slice the list like it tuple
    print(fruits[1])
    #Can get a selection of items in the list like a tuple too
    print(fruits[0:2])

    #Can create a empty tuple and list similarly
    test1 = tuple()
    test2 = list()
    
    #Can convert tuple to list
    animals = ("fox", "rabbit")
    print(animals)
    #Here is where we convert it to a list and you can see in the terminal that the brackets are different indicating what structure it is
    animals = list(animals)
    print(animals)


    for animal in animals:
        print(animal)




main()