#Review of ranges. Although lesson 15 went over it slightly here we will explore more limitations around range method


print("Range can have to parameters but if use two but still the ending range number is not included so account for that")
for i in range(1,6):
    print(i)
    
    

print("Range can even have 3 paramters where the third one is what number to iterate by where it will include the first number because default is 1")
for i in range(1,6,2):
    print(i)
    

for i in range(0,16,5):
    print("Hello " + str(i))