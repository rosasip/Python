# Rosa Siprien
# COP 2500c
# Assignment 5A: Travel Stamps
# Feb 21, 2023

import turtle

turtle.setup(500,500)
turtle.speed()

#The square represents a box.
for i in range(4):
    turtle.pencolor("red")
    turtle.begin_fill()
    turtle.forward(120)
    turtle.left(90)
    turtle.end_fill()
turtle.penup()
turtle.forward(60)
turtle.pendown()

#The green Diamond inside it.
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



'''
The stamps that I designed feature a big green diamond inside a red box.
I selected the color green for the diamond as it symbolizes new beginnings and growth.
As someone who changed their major multiple times in the past, I have now settled on Information Technology.
I am now taking my first coding class. So that is how the the green diamond represents me.
I also chose the color blue to draw my diamond because the color blue represents so many things, inspiration included.

'''
