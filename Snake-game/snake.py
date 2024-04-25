from turtle import Turtle
from end_game import End

## Capital latters as constant
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]

    def createsnake(self):
        for i in STARTING_POSITION:
            new_segmant = Turtle("square")
            new_segmant.color("white")
            new_segmant.penup()
            new_segmant.goto(i)
            self.segments.append(new_segmant)


    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.createsnake()
        self.head = self.segments[0]


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
            self.segments[seg].setheading(self.segments[seg].heading())
 


        self.segments[0].forward(20)

    def right(self):
        self.segments[0].setheading(0)

    def left(self):
        self.segments[0].setheading(180)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)


    def add_body(self):
        new_segmant = Turtle("square")
        new_segmant.speed("fastest")
        new_segmant.color("white")
        new_segmant.penup()
        heading = self.segments[len(self.segments)-1].heading()
        position = self.segments[len(self.segments)-1].position()
        x = position[0]
        y = position[0]
        if position == 0:
            new_segmant.goto(position[0]-20, position[1])

        elif position == 90:
            new_segmant.goto(position[0] , position[1]-20)

        elif position == 180:
            new_segmant.goto(position[0]+20 , position[1])

        else:
            new_segmant.goto(position[0], position[1] + 20)

        self.segments.append(new_segmant)






    def vanishsnake(self):
        for seg in self.segments:
            seg.hideturtle()




