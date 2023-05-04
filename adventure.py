
# Rosa Siprien
# COP 2500c
# Assignment 3: Travel Adventure
# Feb 1, 2023


print("You find yourself in a dark forest. You have three options:\n")
print("1. Search for a way out of the forest.")
print("2. Explore the forest to find treasure.")
print("3. Stay there and wait for rescue. \n")
choice = input("What would you like to do? (Enter 1,2 or 3)\n ")
if choice == "1":
  print("You have chosen to search for a way out of the forest.")
  print("After walking for a while, you come across a fork in the road.")
  print("Do you want to go left or right?")
  
  direction = input("Enter 'left' or 'right': ")
  if direction == "left":
    print("You have chosen to go left.")
    print("After walking for some time, you see a glimmer of light in the distance.")
    print("You have successfully escaped the forest!")
  elif direction == "right":
    print("You have chosen to go right.")
    print("You come across a deep ravine and fall to your death.")
    print("Game Over.")
elif choice == "2":
  print("You have chosen to explore the forest hoping to find a treasure.")
  print("You come across a large hill with an exposed rock.")
  print("Do you want to explore the large hill with the exposed rock?")
  
  exploreHill = input("Enter 'yes' or 'no':\n ")
  if exploreHill == "yes":
    print("You have chosen to explore the large hill with the exposed rock.")
    print("You found a treasure chest filled with gold and jewels underneath the rock!")
    print("Congratulations, you have found the treasure!")
  elif exploreHill == "no":
    print("You have chosen not to explore the large hill with the exposed rock.")
    print("you continued going straight and fell into a pit.")
    print("You died, of a broken neck.")
    print("Game Over.")
elif choice == "3":
  print("You were too scared to go anywhere.\nSo you stayed there and got unalived by a dangerous animal.")
  print("In life, you have to be more adventurous.")
else:
  print("Invalid input. Please try again.")



