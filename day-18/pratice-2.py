import random
from turtle import Turtle, Screen

# Setup screen and turtle
screen = Screen()
turtle = Turtle()
turtle.width(7)


# Define the function
def hello(num_sides):
    angle = 360 / num_sides  # Fix: Use division to calculate the angle
    random_color = ["red","blue","Green","Cyan","Magenta","Blue"]
    rand_colo = random.choice(random_color)
    for _ in range(num_sides):

        turtle.pencolor(rand_colo)

        turtle.forward(100)
        turtle.right(angle)

# Draw shapes
for v in range(3, 11):  # Polygons from triangle (3 sides) to decagon (10 sides)
    hello(v)

# Exit on click
screen.exitonclick()
