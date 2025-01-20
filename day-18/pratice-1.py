from turtle import Turtle,Screen
pampu = Turtle()

pampu.forward(20)
pampu.penup()

for _ in range(15):
    pampu.forward(10)
    pampu.penup()
    pampu.forward(10)
    pampu.pendown()

screen = Screen()
screen.exitonclick()
