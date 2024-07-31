#Review of sets and difference updates

def main():
    numbers1 = {1,2,3,4,5,6,7}
    numbers2 = {8,0,3,10,3,6,1}

    #This will remove items from the first set that is in the referenced set
    numbers1.difference_update(numbers1)
    print(numbers1)

    #This will check to see if all the items in referenced set are in the first set
    print(numbers1.issuperset(numbers2))

    #This will return true as the items in the referenced set are in the first set
    print({1,2,3}.issuperset({1,2,3}))


main()