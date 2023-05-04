
#Rosa Siprien
# Cop 2500c
# 01/27/23
# Lab 2: Challenge 3



place = input("Where would you like to go?\n ")
if place == "Beach":
    balls = int(input("How many beach balls do you have?\n "))
    if balls >= 5:
        print("You are well prepared!")
    else:
        print("Are you sure you have enough?\n")
elif place == "Theme park":
    people = int(input("How many people are there?\n "))
    if people >= 1000:
        print("This is too crowded")
    elif people >= 500:
        print("It's going to be busy.")
    elif people >= 100:
        print("It's a light day")
    else:
        print("Nobody is here.")
