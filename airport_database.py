# Rosa Siprien
# COP 2500C
# Assignment 8: Airport Database
# 04-07-23


print("Welcome to OIA!\n")
def menu():# Prints menu options 
    print("1. Add airport\n")
    print("2. Remove airport\n")
    print("3. Access\n")
    print("4. List Airports\n")
    print("5. Exit\n")
    action= input("What would you like to do?\n")
    return action
     
def main():

    addedInfo = {} # Creates an empty dictionary to store info
    choice = 0 
    while (choice != 5): # loops until user exits
        choice = int(menu()) # calls menu function and get user's choice.
# Adding to dictionary
        if (choice == 1): # x(airport code),y(airport name),z(distance)
            x = input("What is the airport's code?\n")
            y = input("What is the airport's name?\n")
            z = input("What is the distance from Orlando?\n")
            addedInfo[x] = [y, z]
            print("Added")
# Removing from dictionay

        elif (choice == 2):
            undo = str(input("What airport would you like to remove?\n"))
            if undo in addedInfo.keys():
                addedInfo.pop(undo)  
                print("Removed")
            else:
                print("Airport does not exist.")
# Accessing an airport's info in the dictionary
        elif (choice == 3):
            access = str(input("What is the airport code you would like to access?\n"))
            if access in addedInfo.keys(): 
                print(addedInfo[access][0], "-",addedInfo[access][1])
            else:
                print("Airport does not exist.")
# Listing airports in the dictionary
        elif (choice == 4):
            if addedInfo:
                for key in addedInfo.keys():
                    print(key,"-",addedInfo[key][0])
            else:
                print("No Airports")
# Exiting the program
        elif choice == 5:
                print("Goodbye!!!")

main()
