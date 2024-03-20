from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.x_pos = x
        self.y_pos = y
        self.initialize()

    def initialize(self):
        self.speed(0)
        self.teleport(self.x_pos, self.y_pos)
        self.penup()
        self.shape("square")
        self.color("white")
        self.left(90)
        self.pensize(20)
        self.shapesize(1, 5)
    
    def go_up(self):
        self.fd(20)

    def go_down(self):
        self.back(20)

