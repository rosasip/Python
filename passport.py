
import turtle
import math



#This is Montserra's stamp
def montserrat_saldias_stamp(startX, startY):
    
    turtle.pencolor("#FF50FA")
    turtle.speed(0)
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.setheading(0)

#Start of outline.
    turtle.pensize(1.5)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.penup()

#Lines that go inside giving it a "GameCube" design as it is one of the first consoles I had growing up. Adding the teal color as a contrast.
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(20)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor("#20E4FA")
    turtle.right(90)
    turtle.forward(105)
    turtle.left(90)
    turtle.forward(130)
    turtle.left(90)
    turtle.penup()
    turtle.forward(105)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(130)

#I will begin making a swirl of circles signifying multiple game discs over the years I obtained.
    turtle.penup()
    turtle.left(90)
    turtle.forward(52)
    turtle.left(90)
    turtle.forward(60)
    turtle.pendown()

    turtle.speed(15)
    turtle.pencolor("#FF50FA")
    for count in range (9):
        turtle.fillcolor("#a246e0")
        turtle.begin_fill()
        turtle.circle(15)
        turtle.left(40)
        turtle.end_fill()

    turtle.pencolor("#FFFFFF")
    turtle.dot(10)
 
    turtle.penup()
    turtle.right(90)
    turtle.forward(52)
    turtle.right(90)
    turtle.forward(70)
    turtle.pendown()
#This is the little power button for the gamecube.
    turtle.pencolor("#778899")
    turtle.fillcolor("#FF50FA")
    turtle.begin_fill()
    turtle.circle(6)
    turtle.end_fill()
    

   

#This is Claraliz's stamp
def claraliz_ramirez_stamp(x,y):
    turtle.speed(40)
    # Creating square
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.color("lime")
    turtle.penup()
    turtle.right(180)
    turtle.forward,(80)
    turtle.left(90)
    turtle.forward(40)
    turtle.pendown()
    turtle.left(90) 
    turtle.forward(70)
    for count in range(3):
        turtle.left(90)
        turtle.forward(140)
    turtle.left(90)
    turtle.forward(80)
    # Center
    turtle.penup()
    turtle.backward(10)
    turtle.left(90)
    turtle.forward(40)
    # First flower petal
    turtle.color("pink")
    turtle.pendown()
    for count in range(50):
            turtle.circle(18)
            turtle.left(10)
    turtle.penup()
    turtle.setheading(0)
    turtle.left(90)
    turtle.forward(60)
    turtle.pendown()
    # Second flower petal
    for count in range(50):
        turtle.circle(18)
        turtle.left(10)
    turtle.penup()
    turtle.setheading(0)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.pendown()
    # Third flower petal
    for count in range(50):
        turtle.circle(18)
        turtle.left(10)
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(60) 
    turtle.right(90)
    turtle.pendown()
    # Fourth flower petal
    for count in range(50):
        turtle.circle(18)
        turtle.left(10)
    # Center of flower
    turtle.penup()
    turtle.setheading(0)
    turtle.backward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.setheading(0)
    turtle.color("yellow")
    turtle.left(90)
    turtle.forward(30)
    turtle.pendown()
    for count in range(50):
        turtle.color("yellow")
        turtle.circle(10)
        turtle.left(20)


# This is my Stamp.
def rosa_siprien_stamp(startX, startY):
    turtle.tracer()
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.setheading(0)
    turtle.setup(500, 500)
    turtle.speed(0)
    turtle.pendown()
# Draw the square
    for i in range(4):
        turtle.width(4)
        turtle.pencolor("red")
        turtle.begin_fill()
        turtle.forward(120)
        turtle.left(90)
        turtle.end_fill()
    turtle.penup()
    turtle.forward(60)
    turtle.pendown()

    # Draw the green diamond inside the square
    turtle.pensize(3)
    turtle.pencolor("blue")
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.left(59)
    turtle.forward(117)
    turtle.left(63)
    turtle.forward(22)
    turtle.left(58)
    turtle.forward(95)
    turtle.left(59)
    turtle.forward(22)
    turtle.left(63)
    turtle.forward(117)
    turtle.left(45)
    turtle.end_fill()

    turtle.penup()
    turtle.left(45)

def main():
    rosa_siprien_stamp(100,100)
    rosa_siprien_stamp(100,-100)

#Claraliz- friend from TuTh 12pm
    claraliz_ramirez_stamp(-300,-300)
    claraliz_ramirez_stamp(-300,300)

# Monchi- friend from TuTh 12pm
    montserrat_saldias_stamp(-150,-200)
    montserrat_saldias_stamp(-150,200)
main()










