#Review of tuples


#Tuples are data structures that cannot change

def main():
    animals = ("dog", "cat", "fish", "wolf")
    number_animals = len(animals)
    
    print(number_animals)
    print(animals[0])
    print(animals[3])

    for animal in animals:
        print(animal)
    

main()

