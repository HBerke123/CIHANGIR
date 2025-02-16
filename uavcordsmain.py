import math

def route1(pylon1, pylon2, r, angle, detail):
    c = False
    cords = []
    distancex = pylon2[0] - pylon1[0]
    distancey = pylon2[1] - pylon1[1]
    a = angle
    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        sx = pylon2[0] + math.sin(math.radians(a + detail)) * r
        sy = pylon2[1] - math.cos(math.radians(a + detail)) * r
        ox = pylon1[0] - math.sin(math.radians(a)) * r
        oy = pylon1[1] + math.cos(math.radians(a)) * r
        ol = (ox, oy)
        dfo = math.sqrt(pow(fx - ox, 2) + pow(fy - oy, 2))
        fso = math.sqrt(pow(fx - sx, 2) + pow(fy - sy, 2))
        dfa = math.degrees(math.acos((fy - oy) / dfo))
        fsa = math.degrees(math.acos((fy - sy) / fso))

        if ((2 * r > distancex) & (2 * r > distancey)):
            if (c & (dfa < fsa)):
                cords.append(ol)
                b = 270 - i * detail
                break
            if (dfa > fsa):
                c = True
        else:
            if (dfa > fsa):
                cords.append(ol)
                b = 270 - i * detail
                break

        cords.append(fl)
        a = a + detail

    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        ox = pylon1[0] - math.sin(math.radians(a)) * r
        oy = pylon1[1] + math.cos(math.radians(a)) * r
        ol = (ox, oy)

        if ((360 - b * 2) // detail < i):
            cords.append(fl)
            break

        cords.append(ol)
        a = a - detail

    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        
        if (a > angle):
            break

        cords.append(fl)
        a = a + detail

    return cords

def route2(pylon1, pylon2, r, angle, detail):
    c = False
    cords = []
    a = angle
    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        sx = pylon2[0] + math.sin(math.radians(a + detail)) * r
        sy = pylon2[1] - math.cos(math.radians(a + detail)) * r
        ox = pylon1[0] - math.sin(math.radians(a)) * r
        oy = pylon1[1] + math.cos(math.radians(a)) * r
        ol = (ox, oy)
        dfo = math.sqrt(pow(fx - ox, 2) + pow(fy - oy, 2))
        fso = math.sqrt(pow(fx - sx, 2) + pow(fy - sy, 2))
        dfa = math.degrees(math.acos((fy - oy) / dfo))
        fsa = math.degrees(math.acos((fy - sy) / fso))

        if (c & (dfa < fsa)):
                cords.append(ol)
                b = 270 - i * detail
                break
        if (dfa > fsa):
            c = True

        cords.append(fl)
        a = a + detail

    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        ox = pylon1[0] - math.sin(math.radians(a)) * r
        oy = pylon1[1] + math.cos(math.radians(a)) * r
        ol = (ox, oy)

        if ((360 - b * 2) // detail < i):
            cords.append(fl)
            break

        cords.append(ol)
        a = a - detail

    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        
        if (a > angle):
            break

        cords.append(fl)
        a = a + detail

    return cords

def route3(pylon1, pylon2, r, angle, detail):
    c = False
    cords = []
    a = angle
    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        sx = pylon2[0] + math.sin(math.radians(a + detail)) * r
        sy = pylon2[1] - math.cos(math.radians(a + detail)) * r
        ox = pylon1[0] - math.sin(math.radians(a)) * r
        oy = pylon1[1] + math.cos(math.radians(a)) * r
        ol = (ox, oy)
        dfo = math.sqrt(pow(fx - ox, 2) + pow(fy - oy, 2))
        fso = math.sqrt(pow(fx - sx, 2) + pow(fy - sy, 2))
        dfa = math.degrees(math.acos((fy - oy) / dfo))
        fsa = math.degrees(math.acos((fy - sy) / fso))
        
        if (c & (dfa > fsa)):
                cords.append(ol)
                b = 270 - i * detail
                break
        if (dfa < fsa):
            c = True

        cords.append(fl)
        a = a + detail

    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        ox = pylon1[0] - math.sin(math.radians(a)) * r
        oy = pylon1[1] + math.cos(math.radians(a)) * r
        ol = (ox, oy)

        if ((360 - b * 2) // detail < i):
            cords.append(fl)
            break

        cords.append(ol)
        a = a - detail

    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        
        if (a > angle):
            break

        cords.append(fl)
        a = a + detail

    return cords

def route4(pylon1, pylon2, r, angle, detail):
    cords = []
    a = angle
    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        sx = pylon2[0] + math.sin(math.radians(a + detail)) * r
        sy = pylon2[1] - math.cos(math.radians(a + detail)) * r
        ox = pylon1[0] - math.sin(math.radians(a)) * r
        oy = pylon1[1] + math.cos(math.radians(a)) * r
        ol = (ox, oy)
        dfo = math.sqrt(pow(fx - ox, 2) + pow(fy - oy, 2))
        fso = math.sqrt(pow(fx - sx, 2) + pow(fy - sy, 2))
        dfa = math.degrees(math.acos((fy - oy) / dfo))
        fsa = math.degrees(math.acos((fy - sy) / fso))
        
        if (fsa > dfa):
            b = 270 - i * detail
            cords.append(ol)
            break

        cords.append(fl)
        a = a + detail

    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        ox = pylon1[0] - math.sin(math.radians(a)) * r
        oy = pylon1[1] + math.cos(math.radians(a)) * r
        ol = (ox, oy)

        if ((360 - b * 2) // detail < i):
            cords.append(fl)
            break

        cords.append(ol)
        a = a - detail

    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        
        if (a > angle):
            break

        cords.append(fl)
        a = a + detail

    return cords

def route5(pylon1, pylon2, r, angle, detail):
    cords = []
    a = angle
    c = False
    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        sx = pylon2[0] + math.sin(math.radians(a + detail)) * r
        sy = pylon2[1] - math.cos(math.radians(a + detail)) * r
        ox = pylon1[0] - math.sin(math.radians(a)) * r
        oy = pylon1[1] + math.cos(math.radians(a)) * r
        ol = (ox, oy)
        dfo = math.sqrt(pow(fx - ox, 2) + pow(fy - oy, 2))
        fso = math.sqrt(pow(fx - sx, 2) + pow(fy - sy, 2))
        dfa = math.degrees(math.acos((fy - oy) / dfo))
        fsa = math.degrees(math.acos((fy - sy) / fso))

        if (dfa > fsa):
            c = True
        if (c & (dfa < fsa)):
            cords.append(ol)
            b = 270 - i * detail
            break

        cords.append(fl)
        a = a + detail

    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        ox = pylon1[0] - math.sin(math.radians(a)) * r
        oy = pylon1[1] + math.cos(math.radians(a)) * r
        ol = (ox, oy)

        if ((360 - b * 2) // detail < i):
            cords.append(fl)
            break

        cords.append(ol)
        a = a - detail

    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        
        if (a > angle):
            break

        cords.append(fl)
        a = a + detail

    return cords

def route6(pylon1, pylon2, r, angle, detail):
    cords = []
    a = angle
    c = False
    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        sx = pylon2[0] + math.sin(math.radians(a + detail)) * r
        sy = pylon2[1] - math.cos(math.radians(a + detail)) * r
        ox = pylon1[0] - math.sin(math.radians(a)) * r
        oy = pylon1[1] + math.cos(math.radians(a)) * r
        ol = (ox, oy)
        dfo = math.sqrt(pow(fx - ox, 2) + pow(fy - oy, 2))
        fso = math.sqrt(pow(fx - sx, 2) + pow(fy - sy, 2))
        dfa = math.degrees(math.acos((fy - oy) / dfo))
        fsa = math.degrees(math.acos((fy - sy) / fso))
        
        if (fsa > dfa):
            c = True
        if (c & (fsa < dfa)):
            b = 270 - i * detail
            cords.append(ol)
            break

        cords.append(fl)
        a = a + detail

    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        ox = pylon1[0] - math.sin(math.radians(a)) * r
        oy = pylon1[1] + math.cos(math.radians(a)) * r
        ol = (ox, oy)

        if ((360 - b * 2) // detail < i):
            cords.append(fl)
            break

        cords.append(ol)
        a = a - detail

    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        
        if (a > angle):
            break

        cords.append(fl)
        a = a + detail

    return cords

def route7(pylon1, pylon2, r, angle, detail):
    cords = []
    a = angle
    c = False
    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        sx = pylon2[0] + math.sin(math.radians(a + detail)) * r
        sy = pylon2[1] - math.cos(math.radians(a + detail)) * r
        ox = pylon1[0] - math.sin(math.radians(a)) * r
        oy = pylon1[1] + math.cos(math.radians(a)) * r
        ol = (ox, oy)
        dfo = math.sqrt(pow(fx - ox, 2) + pow(fy - oy, 2))
        fso = math.sqrt(pow(fx - sx, 2) + pow(fy - sy, 2))
        dfa = math.degrees(math.acos((fy - oy) / dfo))
        fsa = math.degrees(math.acos((fy - sy) / fso))

        if (fsa > dfa):
            c = True
        if (c & (fsa < dfa)):
            cords.append(ol)
            b = 270 - i * detail
            break

        cords.append(fl)
        a = a + detail

    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        ox = pylon1[0] - math.sin(math.radians(a)) * r
        oy = pylon1[1] + math.cos(math.radians(a)) * r
        ol = (ox, oy)

        if ((360 - b * 2) // detail < i):
            cords.append(fl)
            break

        cords.append(ol)
        a = a - detail

    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        
        if (a > angle):
            break

        cords.append(fl)
        a = a + detail

    return cords

def route8(pylon1, pylon2, r, angle, detail):
    cords = []
    a = angle
    c = False
    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        sx = pylon2[0] + math.sin(math.radians(a + detail)) * r
        sy = pylon2[1] - math.cos(math.radians(a + detail)) * r
        ox = pylon1[0] - math.sin(math.radians(a)) * r
        oy = pylon1[1] + math.cos(math.radians(a)) * r
        ol = (ox, oy)
        dfo = math.sqrt(pow(fx - ox, 2) + pow(fy - oy, 2))
        fso = math.sqrt(pow(fx - sx, 2) + pow(fy - sy, 2))
        dfa = math.degrees(math.acos((fy - oy) / dfo))
        fsa = math.degrees(math.acos((fy - sy) / fso))
        
        if (fsa < dfa):
            c = True
        if (c & (fsa > dfa)):
            cords.append(ol)
            b = 270 - i * detail
            break

        cords.append(fl)
        a = a + detail

    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        ox = pylon1[0] - math.sin(math.radians(a)) * r
        oy = pylon1[1] + math.cos(math.radians(a)) * r
        ol = (ox, oy)

        if ((360 - b * 2) // detail < i):
            cords.append(fl)
            break

        cords.append(ol)
        a = a - detail

    for i in range(360 // detail):
        fx = pylon2[0] + math.sin(math.radians(a)) * r
        fy = pylon2[1] - math.cos(math.radians(a)) * r
        fl = (fx, fy)
        
        if (a > angle):
            break

        cords.append(fl)
        a = a + detail

    return cords

def cords(pylon1, pylon2, r, detail = 1):
    distancex = pylon2[0] - pylon1[0]
    distancey = pylon2[1] - pylon1[1]

    if (distancex == 0):
        if (abs(distancey) / distancey == 1):
            angle = 90
            return route5(pylon1, pylon2, r, angle, detail)
        else:
            angle = 270
            return route6(pylon1, pylon2, r, angle, detail)
    elif (distancey == 0):
        if (abs(distancex) / distancex == 1):
            angle = 0
            return route7(pylon1, pylon2, r, angle, detail)
        else:
            angle = 180
            return route8(pylon1, pylon2, r, angle, detail)
    else:
        distance = math.sqrt(pow(distancex, 2) + pow(distancey, 2))

    angle = math.degrees(math.asin(abs(distancey) / distance))

    if (distancex > 0):
        if (distancey > 0):
            return route1(pylon1, pylon2, r, angle, detail)
        else:
            angle = angle + 270
            return route3(pylon1, pylon2, r, angle, detail)
    else:
        if (distancey > 0):
            angle = angle + 90
            return route2(pylon1, pylon2, r, angle, detail)
        else:
            angle = angle + 180
            return route4(pylon1, pylon2, r, angle, detail)
    
p1 = (14, 40)
p2 = (153, 96)
cor = cords(p1, p2, 60)

f = open("UAV\\cords.txt", "w")
for i in cor:
    t = str(i)
    f.write(t+"\n")
f.close()