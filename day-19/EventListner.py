import turtle
from turtle import Turtle,Screen

trim = Turtle()
Screen = Screen()


def move_forward():
    trim.forward(13)

def move_backward():
    trim.backward(13)

def move_left():
    trim.left(30)
def mov_right():
    trim.right(30)



Screen.listen()
Screen.onkey(key="w",fun=move_forward)
Screen.onkey(key="s",fun=move_backward)
Screen.onkey(key="a",fun=move_left)
Screen.onkey(key="d",fun=mov_right)



Screen.exitonclick()