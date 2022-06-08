from turtle import Turtle, Screen

def draw_square(some_turtle):
    for _ in range(4):
        some_turtle.forward(200)
        some_turtle.right(90)

def draw_art():
    brad=Turtle(shape="turtle")
    brad.color("violet")
    brad.pensize(3)
    brad.speed(0)
    for _ in range(73):
        draw_square(brad)
        brad.right(5)

window= Screen()
window.bgcolor("black")

draw_art()

window.exitonclick()