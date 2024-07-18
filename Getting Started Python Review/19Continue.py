#Review of Continue keyword in loops


for i in range(5):
    print("Starting loop number " + str(i))
    
    stop = input("Stop the loop(y/n)? ")
    if stop.lower() =="y":
        break
    else:
        continue
    
    print("Ending loop numer " + str(i))
    
print("Program Finished")