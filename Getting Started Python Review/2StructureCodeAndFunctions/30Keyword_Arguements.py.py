# Reviewing keyword arguments


#This is an example of assigning arguments default values
def new_fruit(color, weight, sweatness,location):
    print(color)
    print(weight)
    print(sweatness)
    print(location)

def main():
    new_fruit("orange",1, 60,"Colombia")
    print("\n")
    new_fruit(color="red",sweatness = 1, weight=60,location="Colombia")

    
main()