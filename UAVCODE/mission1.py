from turtlepoint import *
from mathexclusive import *

def startmission(p1, p2, radius = 60, detail = 1):
    setturtle()

    latit = 111320
    cords = []
    lat1 = p1[0]
    lon1 = p1[1]
    lat2 = p2[0]
    lon2 = p2[1]
    disx = lat1 - lat2
    disy = lon1 - lon2
    disty = haversine(lat1, lon1, lat2, lon1)
    distx = haversine(lat1, lon1, lat1, lon2)
    x1 = 0
    y1 = 0
    x2 = distx * -disx / abs(disx) * 1000
    y2 = disty * -disy / abs(disy) * 1000
    alpha = (atan(y2 / x2) * d - 90) % 360
    minvalue = 360
    bmax = 0

    point(x1, y1)
    point(x2, y2)

    for i in range(360 // detail):
        corx = x1 + cos(alpha * r) * radius
        cory = y1 + sin(alpha * r) * radius

        ncorx = x1 + cos(((alpha + detail) * r) % 360) * radius
        ncory = y1 + sin(((alpha + detail) * r) % 360) * radius

        dcorx = ncorx - corx
        dcory = ncory - cory

        if (dcorx != 0):
            nalpha = atan(dcory / dcorx) * d

            if (dcorx / abs(dcorx) == -1):
                nalpha += 180
            else:
                if (dcory != 0):
                    if (dcory / abs(dcory) == -1):
                        nalpha += 360
                else:
                    if (dcorx / abs(dcorx) == -1):
                        nalpha = 180
                    else:
                        nalpha = 0
        else:
            if (dcory / abs(dcory) == -1):
                nalpha = 90
            else:
                nalpha = 270

        ocorx = x2 - cos((alpha * r) % 360) * radius
        ocory = y2 - sin((alpha * r) % 360) * radius

        docorx = corx - ocorx 
        docory = cory - ocory
        
        oalpha = atan(docory / docorx) * d

        if (docorx / abs(docorx) == -1):
            if (docory / abs(docory) == 1):
                oalpha += 360
        else:
            oalpha += 180

        if (minvalue > min((oalpha - nalpha) % 360, abs(oalpha - nalpha))):
            bmax = i
            minvalue = min((oalpha - nalpha) % 360, abs(oalpha - nalpha))

        alpha = (alpha + detail) % 360

    for i in range(bmax):
        corx = x1 + cos(alpha * r) * radius
        cory = y1 + sin(alpha * r) * radius
        point(corx, cory)

        cords.append((p1[0] + corx / (latit * cos(cory / latit * r)), p1[1] + cory / latit))
        alpha = (alpha + detail) % 360

    alpha = 0

    for i in range(360 // detail - 2 * bmax):
        corx = x2 - cos((360 - alpha) * r) * radius
        cory = y2 - sin((360 - alpha) * r) * radius
        point(corx, cory)

        cords.append((p2[0] + corx / (latit * cos(cory / latit * r)), p2[1] + cory / latit))
        alpha = (alpha + detail) % 360

    alpha = (atan(y2 / x2) * d - 90) % 360

    for i in range(360 // detail - 3 * bmax):
        corx = x1 + cos((alpha + bmax * detail + 90) * r) * radius
        cory = y1 + sin((alpha + bmax * detail + 90) * r) * radius
        point(corx, cory)

        cords.append((p1[0] + corx / (latit * cos(cory / latit * r)), p1[1] + cory / latit))
        alpha = (alpha + detail) % 360

    for i in cords:
        print(i)
    turtle.exitonclick()

def new_startmission(p1, p2, radius = 60, distance = 1, angle = 1):
    setturtle()
    latit = 111320
    cords = []
    lat1 = p1[0]
    lon1 = p1[1]
    lat2 = p2[0]
    lon2 = p2[1]
    disx = lat1 - lat2
    disy = lon1 - lon2
    disty = haversine(lat1, lon1, lat2, lon1)
    distx = haversine(lat1, lon1, lat1, lon2)
    x1 = 0
    y1 = 0
    x2 = distx * -disx / abs(disx) * 1000
    y2 = disty * -disy / abs(disy) * 1000
    alpha = (atan(y2 / x2) * d) % 360
    x3 = x1 + cos((alpha - 90) % 360 * r) * radius
    y3 = y1 + sin((alpha - 90) % 360 * r) * radius
    x4 = x2 / 2
    y4 = y2 / 2
    x5 = x2 + cos((alpha + 90) % 360 * r) * radius
    y5 = y2 + sin((alpha + 90) % 360 * r) * radius
    x6 = x2 + cos(alpha * r) * radius
    y6 = y2 + sin(alpha * r) * radius 
    x7 = x2 + cos((alpha - 90) % 360 * r) * radius
    y7 = y2 + sin((alpha - 90) % 360 * r) * radius
    x8 = x1 + cos((alpha + 90) % 360 * r) * radius
    y8 = y1 + sin((alpha + 90) % 360 * r) * radius
    x9 = x1 + cos((alpha + 180) % 360 * r) * radius
    y9 = y1 + sin((alpha + 180) % 360 * r) * radius
    
    point(x1, y1, (1, 0, 0))
    point(x2, y2, (1, 0, 0))
    point(x3, y3, (1, 0, 0))
    point(x4, y4, (1, 0, 0))
    point(x5, y5, (1, 0, 0))
    point(x6, y6, (1, 0, 0))
    point(x7, y7, (1, 0, 0))
    point(x8, y8, (1, 0, 0))
    point(x9, y9, (1, 0, 0))

    alpha = arr_nextwaypoint((x3, y3), (x4, y4), alpha, angle, distance)
    alpha = arr_nextwaypoint((x4, y4), (x5, y5), alpha, angle, distance)
    alpha = arr_nextwaypoint((x5, y5), (x6, y6), alpha, angle, distance)
    alpha = arr_nextwaypoint((x6, y6), (x7, y7), alpha, angle, distance)
    alpha = arr_nextwaypoint((x7, y7), (x4, y4), alpha, angle, distance)
    alpha = arr_nextwaypoint((x4, y4), (x8, y8), alpha, angle, distance)
    alpha = arr_nextwaypoint((x8, y8), (x9, y9), alpha, angle, distance)
    alpha = arr_nextwaypoint((x9, y9), (x3, y3), alpha, angle, distance)
    
    for i in cords:
        print(i)
    turtle.exitonclick()


def arr_nextwaypoint(start, end, delta, angle, distance):
    cords = []
    alpha = delta
    startx = start[0]
    starty = start[1]

    while True:
        odistx = startx - end[0]
        odisty = starty - end[1]
        oalpha = atan(odisty / odistx) * d

        if (odistx > 0):
            oalpha += 180
        else:
            if (odisty > 0):
                oalpha += 360

        if (abs(alpha - oalpha) % 360 < angle + 1):
            cords.append((end[0], end[1]))
            point(end[0], end[1])
            break

        alpha1 = (oalpha - alpha) % 360
        alpha2 = 360 - alpha1

        if (alpha1 < alpha2):
            alpha = (alpha + angle) % 360
        else:
            alpha = (alpha - angle) % 360

        print(cos(alpha * r) * distance, sin(alpha * r) * distance)
        startx = startx + cos(alpha * r) * distance
        starty = starty + sin(alpha * r) * distance
        
        cords.append((startx, starty))
        point(startx, starty)

    return oalpha