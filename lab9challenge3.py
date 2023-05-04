# Rosa Siprien
# COP 2500C
# Lab 9: Challenge 3
# 04-09-2023



semester = [[95, 92, 93, 96, 92],

            [100, 100],

            [70, 80, 90],

            [95, 85, 75, 70]]




def grade_up (semesterList):
    result = []
    #outer loop
    for row in range (len(semesterList)):
        increase = 0
    #inner loop
        for col in range (len(semesterList[row])-1):
            #compare two grades
            if semesterList[row][col] < semesterList[row][col+1]:
                increase+=1
        result.append(increase)
    return result
print(grade_up(semester))
