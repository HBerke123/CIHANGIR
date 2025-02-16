import math
import turtle
import os

def cords(pylon1, pylon2, r=0):
    distancex = abs(pylon1[0] - pylon2[0])
    distancey = abs(pylon1[1] - pylon2[1])
    distance = math.sqrt(pow(distancex, 2) + pow(distancey, 2))
    angle = math.asin(distancey / distance)
    print(angle)

print(cords((0, 0), (100, 0)))
turtle.exitonclick()
os.system("cls")