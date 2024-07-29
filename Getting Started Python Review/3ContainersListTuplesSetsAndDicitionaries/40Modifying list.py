#Review of modifying list 

def main():
    
    fruits = ["Apple", "orange", "strawberry", "banana"]
    print(fruits)

    #You can add items to the end of the list using the append method
    fruits.append("melon")
    print(fruits)
    
    #You can also add change items in a list to something else
    fruits[2] = "grape"
    print(fruits)
    
    #You can also change via slices
    fruits[1:4] = ["madiren", "lime", "lemon"]
    print(fruits)
    print()
    #You can even replace multiple items with one item
    fruits[1:4] = ["lime"]
    print(fruits)
    fruits[2:] = ["grapefruit"]
    print(fruits)
    fruits[:2] = ["tomato", "raspberry", "melon"]
    print(fruits)
    
    
main()