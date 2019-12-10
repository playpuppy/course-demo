from puppy2d import *
import math


def archimedes_spiral(max_len):
    a = 20
    degrees = [0]
    for d in degrees:
        degrees.append(d + 18)
        rad = d / 180 * math.pi
        x = a * rad * math.cos(rad)
        y = a * rad * math.sin(rad)
        Circle(x, y, 10, fillStyle='black', isStatic=True)
        if len(degrees) > max_len:
            break


def paradolic_spiral(max_len):
    a = 60
    degrees = [0]
    for d in degrees:
        degrees.append(d + 18)
        rad = d / 180 * math.pi
        x = a * math.sqrt(rad) * math.cos(rad)
        y = a * math.sqrt(rad) * math.sin(rad)
        Circle(x, y, 10, fillStyle='black', isStatic=True)
        if len(degrees) > max_len:
            break


archimedes_spiral(70)
# paradolic_spiral(80)
