

# This is a program to help professors at 'UCF' calculate attendance percentage.

def present(attendenceList): # 1st Function calculates % of days of attendance.
    daysTotal=len(attendenceList)
    daysPresent=sum(attendenceList)
    percentagePresent=(daysPresent/daysTotal)*100 # calculate precentage of days 
    return round(percentagePresent,2) # return percentage


def report(name,attendenceList): # 2nd Function: print attendance report.
    print("Attendence for",name)
    print("Days Total:",len(attendenceList)) 
    print("Days Present:",sum(attendenceList))
    print("Attendance Percentage :",present(attendenceList),"%") # prints attendance percentage

# List
studentDaysPresent=[]

x = int(input("How many Students?\n"))
y = int(input("How many Days? \n"))
# Gather data for student.
for i in range(x):  # Loop
    name = input("Name of Student?\n"+ str(i+1) + ": ") # Get the name.
    z=[]
    for j in range(y):
        attendance= input("Was " + name + " in attendance on day" + str(j+1) + "? (yes/no) ")# ask for daily attendance.
        if attendance.upper()=="YES": # Check to see 'if' student was present
            z.append(1)
        else:
            z.append(0)

    studentDaysPresent.append([name,z]) # Add attendance data to list
# Generate and print report for student
for i in studentDaysPresent:
    report(i[0], i[1])
    
    
    

