MOVE_DISTANCE = 20
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
from turtle import Turtle
UP =90
DOWN=270
RIGHT=0
LEFT=180
class snake:
    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]

    def createsnake(self):
        for position in STARTING_POSITION:
           self.add_segments(position)


    def add_segments(self,position):
        new_segment = Turtle("square")
        new_segment.goto(position)
        new_segment.color("white")
        new_segment.penup()
        self.segments.append(new_segment)

    def extend(self):
        self.add_segments(self.segments[-1].position())
    def Moves(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    def reset(self):
        for seg in self.segments:
           seg.goto(1000,1000)
        self.segments.clear()
        self.createsnake()
        self.head = self.segments[0]
    def Up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)



    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)