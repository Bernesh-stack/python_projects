from turtle import Turtle,Screen
from paddle import Paddle
from Ball import Ball
import time
from Scoreboard import Score
screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)
score = Score()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()



# def go_up():
#     new_y = turtle_pad.ycor()+20
#     turtle_pad.goto(turtle_pad.xcor(),new_y)
#
#
# def go_down():
#     new_y = turtle_pad.ycor()-20
#     turtle_pad.goto(turtle_pad.xcor(),new_y)
#
#
screen.listen()
screen.onkey(r_paddle.go_up,"Up",)
screen.onkey(r_paddle.go_down,"Down",)

screen.onkey(l_paddle.go_up,"w",)
screen.onkey(l_paddle.go_down,"d",)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(r_paddle) <50 and ball.xcor() >320 or ball.distance(l_paddle) <50 and ball.xcor() <-320:
       ball.bounce_x()


    if ball.xcor() >380:
        ball.restart()

        score.l_point()
    if ball.xcor() <-380:
        ball.restart()
        score.R_point()







screen.exitonclick()



