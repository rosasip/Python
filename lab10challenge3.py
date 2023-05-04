# Rosa Siprien
# COP 2500C
# Lab 10: Challenge 3
# 04-14-23


# Open the file
inFile = open("Lab10.csv", "r")
# Read the lines
lines = inFile.readlines()

finalList = []

for line in lines:
    info = line.split(",")
    temp = {}

    temp["course_code"] = info[0]
    temp["course_name"] = info[1]
    temp["course_hours"] = info[2]
    temp["teacher"] = info[3]
    temp["grade"] = info[4].strip("\n")

    finalList.append(temp)

for dictionary in finalList:
    print(dictionary)

                                
    

