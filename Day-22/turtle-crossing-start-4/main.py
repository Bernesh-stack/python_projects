import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

Screen().listen()
pealyer = Player()
Screen().onkey(pealyer.Move_forward, "Up")
car = CarManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.creating_car()
    car.car_backward()
    for ar in car.all_car:
        if ar.distance(pealyer) <  20:
            game_is_on= False
    if pealyer.ycor() ==300:
        pealyer.goto(0,-300)
        car.speed_increment()