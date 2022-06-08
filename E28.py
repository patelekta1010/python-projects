import turtle
t = turtle.Pen()
def square(side):
    for i in range(0,5):
        t.forward(side)
        t.left(90)
square(50)
square(60)
square(70)