import os
import turtle
from math import * 
from math import radians as rad
from math import degrees as deg
from turtlepoints import *

def findangle(p1, p2):
    distancex = p2[0] - p1[0]
    distancey = p2[1] - p1[1]
    distance = sqrt(pow(distancex, 2) + pow(distancey, 2))
    angle = degrees(acos(abs(distancex) / distance))

    if (distancey < 0):
        if (distancex < 0):
            angle = angle + 180
        else:
            angle = 360 - angle
    else:
        if (distancex < 0):
            angle = 180 - angle

    return angle

def findedge(p1, p2, r):
    distancex = p2[0] - p1[0]
    distancey = p2[1] - p1[1]
    distance = sqrt(pow(distancex, 2) + pow(distancey, 2))
    sinof = (distancey / distance)
    cosof = (distancex / distance)
    return (p1[0] - cosof * r, p1[1] - sinof * r)

def findturned(p, r, angle):
    sinof = sin(radians(angle))
    cosof = cos(radians(angle))
    return (p[0] + cosof * r, p[1] + sinof * r)

def arrivepoint(start, end, a, ad = 1, dd = 1):
    cords = []
    ll = start
    la = a
    ab = findangle(ll, end)
    da = abs(ab - la)
    db = 360 - da
    increase = False
    decrease = False
    while not ((da < ad) or (db < ad)):
        if ((la / 360) > 1):
            la = la % 360
            increase  = True
        
        if (la < 0):
            la = 360 + la
            decrease = True

        ab = findangle(ll, end)
        da = abs(ab - la)
        db = 360 - da

        if (increase or decrease):
            if (increase):
                la = la + ad
            else:
                la = la - ad
        else:
            if (da > db):
                if ((360 - la) > 180):
                    la = la - ad
                else:
                    la = la + ad
            else:
                if (ab > la):
                    la = la + ad
                else:
                    la = la - ad

        ll = (ll[0] + cos(rad(la)) * dd, ll[1] + sin(rad(la)) * dd)
        cords.append(ll)
    cords.append(end)
    return (cords, la)
    
red = (1, 0, 0)
blue = (0, 0, 1)
p1 = (0, 0)
p2 = (200, 200)
a = findangle(p1, p2)
r = 60
a1 = (125, 200)
a2 = (25, 100)
v1 = findedge(p1, p2, r)
v2 = findedge(p2, p1, r)
v3 = findturned(p2, r, a + 270)
turtle.speed(0)
turtle.pensize(4)
turtle.hideturtle()
turtle.penup()
turtle.pendown()
drawpoint(p1)
drawpoint(p2)
drawpoint(a1, red)
drawpoint(a2, red)
drawpoint(v1, red)
drawpoint(v2, red)
drawpoint(v3, red)
path1 = arrivepoint(v3, v2, a)
path2 = arrivepoint(v2, a1, path1[1])
path3 = arrivepoint(a1, a2, path2[1])
path4 = arrivepoint(a2, v1, path3[1])
path5 = arrivepoint(v1, v3, path4[1])

cords1 = path1[0]
cords2 = path2[0]
cords3 = path3[0]
cords4 = path4[0]
cords5 = path5[0]
cords = cords1 + cords2 + cords3 + cords4 + cords5

turtle.penup()
turtle.goto(cords[0][0], cords[0][1])
turtle.pendown()

for i in cords:
    turtle.goto(i[0], i[1])

turtle.exitonclick()
os.system("cls")