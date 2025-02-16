import math
import turtle
import os

def coordinates(pylon1, pylon2, node=1):
    cords = []
    r1 = pylon2[1]
    r2 = pylon2[0] - pylon1[0] - r1

    for i in range(90//node):
        cords.append((pylon2[0] + math.sin(math.radians(i * node)) * r1, pylon2[1] - math.sin(math.radians(90 - i * node)) * r1))

    for i in range(90//node):
        cords.append((pylon2[0] + math.sin(math.radians(90 - i * node)) * r1, pylon2[1] + math.sin(math.radians(i * node)) * r1))

    for i in range(90//node):
        cords.append((pylon2[0] - math.sin(math.radians(i * node)) * r1, pylon2[1] + math.sin(math.radians(90 - i * node)) * r1))

    for i in range(90//node):
        cords.append((pylon1[0] + math.sin(math.radians(90 - i * node)) * r2, pylon1[1] - math.sin(math.radians(i * node)) * r2))

    for i in range(90//node):
        cords.append((pylon1[0] - math.sin(math.radians(i * node)) * r2, pylon1[1] - math.sin(math.radians(90 - i * node)) * r2))

    for i in range(90//node):
        cords.append((pylon1[0] - math.sin(math.radians(90 - i * node)) * r2, pylon1[1] + math.sin(math.radians(i * node)) * r2))

    for i in range(90//node):
        cords.append((pylon1[0] + math.sin(math.radians(i * node)) * r2, pylon1[1] + math.sin(math.radians(90 - i * node)) * r2))

    for i in range(90//node):
        cords.append((pylon2[0] - math.sin(math.radians(90 - i * node)) * r1, pylon2[1] - math.sin(math.radians(i * node)) * r1))

    cords.append((pylon2[0], pylon2[1] - r1))

    return cords

cords = coordinates((,), (,), 18)
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(cords[0][0], cords[0][1])
turtle.pendown()
        
for i in cords:
    turtle.goto(i[0], i[1])

turtle.exitonclick()
os.system("cls")