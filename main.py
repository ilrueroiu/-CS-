#!/usr/bin/python3

import math


def triangle_area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area


def hypo(p1, p2):
    side = math.hypot(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))
    return side


def check_crossroad(robot, point1, point2, point3, point4):
    ab = point2[0] - point1[0]
    bc = point3[1] - point2[1]
    cd = ab
    da = bc

    # print(ab, bc, cd, da)

    rect_area = ab * bc

    # r - robot's point
    ar = hypo(robot, point1)
    br = hypo(robot, point2)
    cr = hypo(robot, point3)
    dr = hypo(robot, point4)

    arb = triangle_area(ar, br, ab)
    brc = triangle_area(br, cr, bc)
    crd = triangle_area(cr, dr, cd)
    dra = triangle_area(dr, ar, da)

    tri_area = round(arb + brc + crd + dra)

    if tri_area == rect_area:
        return True
    else:
        return False


robot = (2 ** 10000 + 1, 2 ** 10000 + 10)
point1 = (2 ** 10000 + 1, 2 ** 10000 + 10)
point2 = (2 ** 10000 + 7, 2 ** 10000 + 10)
point3 = (2 ** 10000 + 7, 2 ** 10000 + 14)
point4 = (2 ** 10000 + 1, 2 ** 10000 + 14)

print(check_crossroad(robot, point1, point2, point3, point4))



