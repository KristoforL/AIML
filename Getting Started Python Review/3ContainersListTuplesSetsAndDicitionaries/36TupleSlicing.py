#Review of slicing tuples which is bascially cutting off a section of the tuple to return read print etc

def main():
    animals = ("goat", "sheep", "dog", "elephat")
    
    #This counts as a slice even though it is a single element
    print(animals[1])
    #This is more traditionally how a slice might be executed in code
    print(animals[1:3])
    #This is a way to include less text and still accomplish only showing certain elements up to a certain index or after a certain index
    print(animals[:3])
    print(animals[2:])
    #There is even a way to do negative elements so to speak
    print(animals[-1])
    print(animals[-3:-1])
    
    extract = animals[0:2]
    print(extract)
    
    #This works with strings as well
    quote = "It was the best of times"
    print()
    print(quote[3])
    print(quote[0:6])
    
main()

