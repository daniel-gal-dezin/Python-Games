from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,xpos,ypos):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.setpos(xpos, ypos)
        self.setheading(90)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1 , stretch_len=5)



    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)


