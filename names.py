
def main(): # Input goes here
    airport = input("Name of airport: \n")
    city = input("Name of city: \n")
    method = input("Coding Method: \n ")
    # print
    answer = 0
    answer = airport_code_finder(airport, city, method)
    print(airport, "-", city, "-", answer)


def airport_code_finder(airport, city, method):
# Splits name of airports. takes up to the third letter.
    if method == "name":
        airportName = airport.split()
        x1 = airportName[0]
        x2 = airportName[1]
        x3 = airportName[2]
# takes uppercase and others for lettering
        number = 0
        code = ""
        for i in range(len(x1)):
            if not x1[i].islower():
                number += 1
                code += x1[i]
            if number == 2:
                b = i + 1
                code += x1[b]
                b = code.upper()
                return b
# puts first letters together to get acronym
        word = x1[0] + x2[0] + x3[0]
        return word
# takes first three letters and makes it capital
    elif method == "city":
        letter = city.upper()
        letter = letter[0:3]
        return letter

main()
