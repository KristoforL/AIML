# Exercise to create and utilize arguments

"""
Exercise: define a single function that accepts: 
    one or more positional arguments
    zero or more variable arguments
    zero or more variable keyword arguments

    make the function print out all arguments it receives
"""


def practice(name, *atts ,**kwarg):
    print(name)

    for i in atts:
        print(i)

    for ats in kwarg:
        print(ats,":",kwarg[ats])

def main():
    practice("John", 15, "pizza", status= "single", belly= "hungry")
    print()
    practice("Tin", 27, "pineapple", "single", movement = "cruising")
    print()
    practice("JKL", age=31, food="ramen", status="taken", travel="soloer")

main()