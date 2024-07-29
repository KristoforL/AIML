#Review of extending and inserting into list

def main():
    
    animals = ["dog", "donkey", "duck"]
    #You can use the insert which places your item after the index referenced
    animals.insert(1, "giraffe")
    print(animals)
    
    #You can add list together or onto the end like appending using the extends method like below
    more_animals = ["elephant" , "monkey"]
    animals.extend(more_animals)
    print(animals)


main()