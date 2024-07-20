# Reviewing passing multiple arguments


#This is an example od positional paramters where they are matched by the positional input
def calculate_box_volume(width, height, length):
    return width*length*height


def main():
    volume = calculate_box_volume(5, 5, 5)
    print("Volume of the box with width " + str(volume))

    #You can separate returns with commas and it will still place a space in the print for you by default
    print("Box volume is:", volume) 


    
main()