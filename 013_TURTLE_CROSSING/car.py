from turtle import Turtle
from random import randint


class Car(Turtle):

    def __init__(self, width, height):
        super().__init__()
        self.min_height = int(height / 2 * -1 + 75)
        self.max_height = int(height / 2 - 51)
        self.start_pos_x = width / 2 + 100
        self.pos_y = randint(self.min_height, self.max_height)
        self.start_pos_y = self.pos_y - self.pos_y % 25
        self.color_tuple = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.initialize()

    def initialize(self):
        self.penup()
        self.teleport(self.start_pos_x, self.start_pos_y)
        self.color(self.color_tuple)
        self.shape("square")
        self.shapesize(1, 3)
        self.setheading(180)

