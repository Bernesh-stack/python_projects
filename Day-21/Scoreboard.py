from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_Score = 0
        self.r_Score = 0
        self.Update_score_boarad()

    def Update_score_boarad(self):
        self.goto(-100, 200)
        self.write(self.l_Score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_Score, align="center", font=("Courier", 80, "normal"))
    def l_point(self):
        self.l_Score+=1
        self.clear()
        self.Update_score_boarad()

    def R_point(self):
        self.r_Score+=1
        self.clear()
        self.Update_score_boarad()


