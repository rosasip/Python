# Rosa Siprien
# COP 2500C
# Assignment 7: Code Database
# 03-31-23



def airport_code_finder(airport, city, method):
# if statement for airport name
    if method == "name":
        airportName = airport.split()
        code=""
        if len (airportName)<3:
            for i in range (len(airportName)):
                code+=airportName[i][0]
        else:
            x1 = airportName[0]
            x2 = airportName[1]
            x3 = airportName[2]
            code = x1[0] + x2[0] + x3[0]
        return code
# takes first three letters and makes it capital
    elif method == "city":
        letter = city.upper()
        letter = letter[0:3] 
        return letter

# main function goes here
def main(): 
    file_in = open("us-airports.csv","r") #inputting
    file_out = open("output.csv","w")   #outputting
    lines = file_in.readlines()
    for i in range(len(lines)):
        blank=lines[i].strip()
        items = lines[i].split(",")
        if items[0]!="":
            #The num1 variable stores airport code based on the airport name 
            num1 = airport_code_finder(items[0], items[1], "name")
        if items[1]!="":
            #The num2 variable stores airport code based on the city name
            num2 = airport_code_finder(items[0], items[1], "city")
#writes the output to the output file
        file_out.write(str(items[0]) + "," + str(items[1]) + "," + str(num2) + "," + str(num1) + "\n")
# closes the input and output files
    file_in.close()
    file_out.close()

main()

