from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.x_pos = 0
        self.x_mov = 0
        self.y_pos = 0
        self.y_mov = 0
        self.initialize()

    def initialize(self):
        self.speed(1)
        self.teleport(self.x_pos, self.y_pos)
        self.shape("circle")
        self.color("white")
        self.penup()

    def start_ball(self, player):
        if player == "right":
            self.x_mov = 10
            self.y_mov = 10
        elif player == "left":
            self.x_mov = -10
            self.y_mov = 10
        else:
            print("ERROR MESSAGE: Player on ball.start_ball was not properly assigned.")
    
    def move_ball(self):
        self.x_pos += self.x_mov
        self.y_pos += self.y_mov
        self.goto(self.x_pos, self.y_pos)

    def check_screen_collision(self, height):
        if self.ycor() == height / 2 - 20 or self.ycor() == height / 2 * -1 + 20:
            self.y_mov *= -1
            return True
