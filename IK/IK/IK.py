#Avem un brat 3R cu o baza ce se roteste dupa z si doua jointuri ce se rotesc dupa x
#Trebuie sa reducem problema la un brat 2D 2R, si vom face asta prin a roti baza in pozitie
#FOARTE IMPORTANT! Rotirea jointului bazei creaza doua noi solutii, cand se uita in spate
                                                                #si cand se uita in fata!!!
#Ulterior, aplicam algoritmul 2RIK (Two rotational Joints Inverse Kinematics)
import math
from math import sqrt
from math import atan
from math import acos
from math import pi
from math import sin
from math import cos
L1 = 98.875
L2 = 136.875
#constante
def transform3(q):
    for i in range(0, 3):
        q[i] = q[i] / (pi)
    return q

def RIK3(x, y, z): #x este forward, y este height, z este left
    if (x == 0):
        q3 = pi/2
    else:
        q3 = atan(z/x) #asta este tangenta
    #observatie, q3 poate lua valori DOAR intre -pi/2 si pi/2, sorry!!!!!!
    if (x < 0):
        if q3 >= 0:
            q3 = pi - q3
        else:
            q3 = -(pi - q3)
    #x-ul nu este chiar x, ci mai degraba:
    x = sqrt(x**2 + z**2)
    xd = sqrt(x**2 + y**2) #modulul vectorului
    if xd < 50: #treshold
        return ([-1024,-1024,-1024])
    c2 = (xd**2 - L1**2 - L2**2)/(2*L1*L2)
    if (-1 > c2) | (1 < c2):
        return ([-1024,-1024,-1024])
    if c2 == 1:
        if x == 0:
            q1 = pi/2
        else:
            q1 = atan(y/x)
        return([q1, 0, q3])
    if (c2 == -1) & (xd != 0):
        if x == 0:
            q1 = pi/2
        else:
            q1 = atan(y/x)
        return([q1, pi, q3])
    if (c2 == -1) & (xd == 0): #nu ar trebui sa intre in acest caz anyways ca xd va fi mai mare
        return([-1024, pi, q3])
    if x == 0:
        theta = pi/2
    else:
        theta = atan(y/x)
    theta = atan(y/x)
    q2 = -acos(c2)
    q1 = theta - atan(L2 * sin(q2) /( L1 + L2*cos(q2)))
    if (q1 <= 0): #recalculam dupa constraintul dorit, in cazul nostru vrem ca articulatia sa fie in sus
        q2 = acos(c2)
        q1 = theta - atan(L2 * sin(q2)/(L1 + L2*cos(q2)))
    #q2 ia solutii intre -pi si pi pentru ca q2 poate lua 2 valori, una in 0 pi si cealalta in -pi 0
    #q1 e dependent de q2 si poate lua valori intre -pi si pi
    #daca TOATE imi returneaza in -pi si pi, atunci stiu unghiurile
    return ([q1, q2, q3])

