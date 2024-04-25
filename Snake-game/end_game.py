from turtle import Turtle

class End(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.write("GAME END", align="center", font=('Arial', 20, 'normal'))
        self.hideturtle()
