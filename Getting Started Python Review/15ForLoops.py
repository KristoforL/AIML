#Review of for loops that will go for as long as a condition is not met which might not ever happen or you could break out of it after so many attempts using other conditions

#Range includes 0 since computers start counting at 0. This leads to leaving off the number you want in that range so adjust accordingly
for i in range(5):
    print(i)


print("Range can have to parameters but if use two but still the ending range number is not included so account for that")
for i in range(1,6):
    print(i)