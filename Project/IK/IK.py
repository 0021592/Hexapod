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

def RIK3(x, y, z): #y este height, x este forward, z este left
    q3 = atan(z/y)
    #x-ul nu este chiar x, ci mai degraba:
    x = sqrt(x**2 + z**2)
    xd = sqrt(x**2 + y**2) #modulul vectorului
    if xd < 50: #treshold
        return ([-1,-1,-1])
    c2 = (xd**2 - L1**2 - L2**2)/(2*L1*L2)
    if (-1 > c2) | (1 < c2):
        return ([-1,-1,-1])
    if c2 == 1:
        return([atan(y/x), 0, q3])
    if (c2 == -1) & (xd != 0):
        return([atan(y/x), pi, q3])
    if (c2 == -1) & (xd == 0): #nu ar trebui sa intre in acest caz anyways ca xd va fi mai mare
        return([-1, pi, q3])
    theta = atan(y/x)
    q2 = -acos(c2)
    q1 = theta - atan(L2 * sin(q2) /( L1 + L2*cos(q2)))
    if (q1 > 0):
        return ([q1, q2, q3])
    q2 = acos(c2)
    q1 = theta - atan(L2 * sin(q2)/(L1 + L2*cos(q2)))
    return ([q1, q2, q3])

