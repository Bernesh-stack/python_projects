import random
from turtle import Turtle, Screen

# Setup screen and turtle
screen = Screen()
turtle = Turtle()
turtle.width(7)
screen.tracer(0)  # Disable automatic screen updates for smooth animation

# Function Definitions
def forward():
    turtle.forward(10)

def up():
    turtle.setheading(90)
    turtle.forward(10)

def down():
    turtle.setheading(-90)
    turtle.forward(10)

def left():
    turtle.left(90)
    turtle.forward(10)

def right():
    turtle.right(90)
    turtle.forward(10)

# Random movement function
def random_move():
    direction = random.choice(["up", "down", "left", "right"])
    if direction == "up":
        up()
    elif direction == "down":
        down()
    elif direction == "left":
        left()
    elif direction == "right":
        right()



while True:
    random_move()  # Make a random move


# Exit on click
screen.exitonclick()
