#Review of Joining list 

def main():
    fruits1 = ["apple", "orange", "banana"]
    fruits2 = ["melon", "lemon", "grape"]
    animals1 = ("dog", "cat", "mouse")
    animals2 = ("tiger", "lion", "panther")

    value = 5
    # Could do value = value + 3 to add but you can also use +=
    value +=3
    print(value)

    #That same function works for list as well
    animals1 += animals2
    print(animals1)
    fruits1 +=  fruits2
    print(fruits1)

    #The id stays the same because it is the same list with new elements
    print(id(fruits1))
    fruits1 += fruits2
    print(id(fruits1))
    print(fruits1)
    #Because tuples are not mutable the id changes because when adding tuples you essentially create a new one
    print(id(animals1))
    animals1 += animals2
    print(id(animals1))
    print(animals1)




main()
