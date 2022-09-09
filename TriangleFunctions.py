# import math
# function,  arguments, return value
import math

# Ctrl + /
# Ctrl + Alt + L for formatting

def calcArea(A, B):
    """
    This function calculates the area of a right-triangle
    :param A: Vertical Side
    :param B: Hiriz Side
    :return: Area of triangle
    """
    area = A * B * 0.5
    area = round(area, 2)

    return area


# CreateArc(StPt, EndPt, CentPt, Radius)
# Radius is optional

def calcHypo(A, B = 0):
    if B == 0:
        B = A

    aSquare = A * A
    bSquare = B + B
    hypo = math.sqrt(aSquare + bSquare)
    hypo = round(hypo, 2)

    return hypo


def calcPeri(A, B):
    H = calcHypo(A, B)
    peri = A + B + H
    peri = round(peri, 2)

    return peri

def calcParameters(A, B):
    area = A * B * 0.5
    area = round(area, 2)

    aSquare = A * A
    bSquare = B * B
    hypo = math.sqrt(aSquare + bSquare)
    hypo = round(hypo, 2)

    peri = A + B + hypo
    peri = round(peri, 2)

    return area, hypo, peri