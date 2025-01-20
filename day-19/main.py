from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(500,400)

user_bet=screen.textinput("hi which turtle willl win the race" ,"what that brother")
colors = ["red","orange","yellow","green","blue","purple"]
y_position = [-70,-40,-10,20,50,80]
race_On = False
new_Turtles =[]

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    new_Turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in new_Turtles:
        if turtle.xcor()>230:
           is_race_on=False
           winning_color = turtle.pencolor()
           if winning_color == user_bet:
               print("you won")
           else:
               print("sorry the option is wrong")


        dist = random.randint(0,10)
        turtle.forward(dist)

    



screen.exitonclick()
