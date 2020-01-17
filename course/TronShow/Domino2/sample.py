from puppy2d import *

setGravity(0, -1)

Rectangle(-100, 200, 700, 30, isStatic=True)

for i in [-300, -200, -100, 0]:
    Rectangle(i, 300, 20, 200)

Circle(200, 300, 150)

Rectangle(0, -200, 1000, 30, isStatic=True)

for i in [-400, -300, -200, -100, 0, 100, 200, 300]:
    Rectangle(i, -100, 20, 200)

Circle(-350, 500, 150)
