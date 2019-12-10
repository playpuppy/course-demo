from puppy2d import *

setGravity(0, -1)

Rectangle(0, -500, 1100, 50, isStatic=True)

for j in range(10):
    for i in range(-500, 501, 100):
        Rectangle(i, 400, 100, 100)
