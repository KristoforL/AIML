#Review of boolean operators

# and, not, or

is_raining = True
is_windy = False

stay_inside = is_raining and is_windy

print("Stay inside: " + str(stay_inside))

take_coats = is_raining or is_windy

print("Take Coats: " + str(take_coats))

print("Not Windy: " + str(not is_windy))