#Review of List comprehensions with conditions

def main():
    numbers1 = [x for x in range(0,10)]
    print(*numbers1)
    
    #Creating a new list with the condition at the end
    numbers2 = [x for x in numbers1 if x >5]
    print(numbers2)
    
    #This will use the mmodular operator to see what is an even number
    numbers2 = [x for x in numbers1 if x>0 and x %2 == 0 ]
    print(numbers2)
        


main()