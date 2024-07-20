# Reviewing variable length and keyword arguments with some dictionaries

def add_descriptions(**description):

    for prop in description:
        print(prop, ":", description[prop])

    print()

#The way these are formatted this is considered a dictionary with key value pairs
def main():
    add_descriptions(height=180,weight=90,eyes="blue")
    add_descriptions(trousers="black",beard="True")
    add_descriptions(sex="male",height=180)


    
main()