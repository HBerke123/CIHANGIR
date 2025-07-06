import turtle 

def setturtle():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.pensize(4)

def point(x, y, color=(0, 0, 0)):
    if (color != (0, 0, 0)):
        turtle.color(color)
        
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x, y)
    
    if (color != (0, 0, 0)):
        turtle.color((0, 0, 0))