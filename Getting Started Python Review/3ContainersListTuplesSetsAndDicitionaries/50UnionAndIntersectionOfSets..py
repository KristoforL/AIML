#Review of set union and intersection


def main():
    
    numbers1 = {1,2,3,4,5,6,7}
    numbers2 = {8,0,3,10,3,6,1}
    
    #This is how you use union to join sets. Remember that the sets will only show unique items in order
    print(numbers1.union(numbers2))
    
    #This will show the items shared in each set
    print(numbers1.intersection(numbers2))

    #This will show the numbers tha ter different from each set and order matters
    print(numbers1.difference(numbers2))    
    print(numbers2.difference(numbers1))  
    
    #This will show the numbers that unique in bothe sets. The numbers that will only show are the ones that dont show in both 
    print(numbers1.symmetric_difference(numbers2))
    
    #You can subutract sets from each other and remove one set from the other sets based on the similar numbers
    print(numbers1-numbers2)
    print(numbers2-numbers1)

    #But oddly enough you cannot add sets together
    #print(numbers1+numbers2)
     
     
main()