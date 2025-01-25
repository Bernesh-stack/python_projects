with open("data.txt" ) as file:
    file_value = file.read()
from turtle import Turtle
import random
ALIGNMENT ="center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score=0
        with open("data.txt") as data:
                self.high_score= int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)

        self.hideturtle()
    def Updatescoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} high score={self.high_score}", align=ALIGNMENT, font=FONT)

    # FONTdef gameover(self):
    #     self.goto(x=0,y=0)
    #     self.write(f"Bush", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w")as writere:
                writere.write(f"{self.high_score}")
        self.score=0
        self.Updatescoreboard()



    def increase(self):
        self.score+=1

        self.Updatescoreboard()
