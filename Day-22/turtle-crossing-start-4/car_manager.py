COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random

from turtle import Turtle


class CarManager:
    def __init__(self):

        self.all_car=[]
        self.distance = STARTING_MOVE_DISTANCE



    def creating_car(self):
        random_choice = random.randint(1,6)
        if random_choice ==1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_x = 300
            new_y =random.randint(-250,250)
            new_car.penup()
            new_car.speed(self.distance)
            new_car.goto(new_x,new_y)
            self.all_car.append(new_car)


    def car_backward(self):
        for x in self.all_car:
            x.backward(STARTING_MOVE_DISTANCE)


    def speed_increment(self):
        self.distance+= MOVE_INCREMENT
