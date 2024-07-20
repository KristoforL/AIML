# Reviewing variable arguments


#This is an example of assigning arguments default values
def descritb_person(name, *attributes):
    print(name)
    for attribute in attributes:
        print(attribute)
    print(type(attributes))

def main():
    descritb_person("Todd", "hungry","tall", "clean", "well traveled")
    print()
    descritb_person("Effie", "short","funny", "doesnt like hevin hart", "well traveled")
    print()


    
main()