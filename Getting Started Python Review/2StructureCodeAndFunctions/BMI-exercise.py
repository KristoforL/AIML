# Exercise to create a BMI calculator


def get_user_info():
    w = input("Enter weight in kilos> ")
    h = input("Enter height in meters> ")
    #When you return mulitple items you can call them nearly the same in the another function
    return w, h

def BMI(weight, height):
    return float(weight)/(float(height)**2)
    

def main():
    #Here is the way to call multiple returns to another function
    w, h = get_user_info()
    print(BMI(w,h))
    

main()