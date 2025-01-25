from turtle import Turtle,Screen
import time
from Snake import snake
from food import Food
from Scoreboard import Scoreboard
Screen = Screen()
Screen.setup(600,600)
Screen.bgcolor("black")
Screen.title("Snake")
Screen.tracer(0)

snake = snake()
food = Food()
Score = Scoreboard()
Screen.listen()
Screen.onkey(snake.Up ,"Up")
Screen.onkey(snake.Down,"Down")
Screen.onkey(snake.Left,"Left")
Screen.onkey(snake.Right,"Right")

game_is_on = True
while game_is_on:
    Screen.update()
    time.sleep(0.1)
    snake.Moves()

    if snake.head.distance(food) <15:
            food.refresh()
            Score.increase()
            snake.extend()

    if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor() <-280 or snake.head.ycor() >280:
        Score.reset()
    for segment in snake.segments:
        if segment ==snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            Score.reset()
            snake.reset()


Screen.exitonclick()