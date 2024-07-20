#The Fridge

"""
    Get the user to enter temp in celsius 
    
    if temp <0 print fridge too cold
    
    if temp 0-4 degree print fridge ok
    
    if temp 4-6 degrees print fridge too warm
    
    if temp >6 print Fridge broken
"""
    
    
# temp = input("How hot is it in celsius degrees: ")

# print("You said it was " + temp + " Degrees Celsius")

# C = float(temp)
# if float(C) < 0:
#     print("Fridge too cold!")
# elif float(C) >= 0 and float(C) <=4:
#     print("Fridge is ok")
# elif float(C) >4 and float(C) <=6:
#     print("Fridge too warm")
# else:
#     print("Fridge Broken") 
    
    
#Improved the fridge solution with one print statement in one place. Could utilize constants since we know these statuses will not change

temp = input("How hot is it in celsius degrees: ")

print("You said it was " + temp + " Degrees Celsius")

STATUS_BROKEN = "Fridge is broken"
STATUS_COLD = "Fridge is too cold"
STATUS_WARM = "Fridge is too warm"
STATUS_OK =  "Fridge is ok"

status = STATUS_BROKEN

C = float(temp)
if float(C) < 0:
    status = STATUS_COLD
elif float(C) >= 0 and float(C) <=4:
    status = STATUS_OK
elif float(C) >4 and float(C) <=6:
    status = STATUS_WARM
    
print(status)