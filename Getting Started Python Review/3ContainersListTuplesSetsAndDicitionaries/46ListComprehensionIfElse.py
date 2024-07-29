#Review of List comprehensions with if else 

def main():
    
    #This adds the condition to the end to check if the number is greater than 0 and is even
    numbers = [x for x in range(0,20) if x > 0 and x %2 != 0]
    print(numbers)
    
    #This does the full if else statement at the front
    more_numbers = [x if x >10 else 0 for x in numbers]
    print(more_numbers)
    
    
main()