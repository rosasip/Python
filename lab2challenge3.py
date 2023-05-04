#Rosa Siprien
# COP 2500
# Lab 2: Challenge 3
# Feb3,2023


direction=(input("Where would you like to go?\n"))
if direction=="Theme Park":
    daysNum=int(input("How many days are you going for?\n"))
    for i in range(1, daysNum+1):
        print("Day"+str(i)+",Park"+str(i))
elif (direction=="Science Center"):
    leave=input("Are you ready to go?\n")
    while(leave!="Ready"):
        leave=input("Are you ready to go?\n")
    
    
