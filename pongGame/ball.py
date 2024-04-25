from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.xmove = 10
        self.ymove = 10



    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)



    def ybounceup(self):
        self.ymove  = -10



    def xbouncerigh(self):
        self.xmove = -10


    def ybouncedown(self):
        self.ymove  = 10


    def xbounceleft(self):
        self.xmove = 10