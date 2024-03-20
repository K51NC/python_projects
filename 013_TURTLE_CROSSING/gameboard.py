from turtle import Turtle

class Gameboard(Turtle):

    def __init__(self, width, height):
        super().__init__()
        self.startline_y = height / 2 * -1 + 50
        self.finishline_y = height / 2 - 50
        self.screen_width = width
        self.font = ("Arial", 40, "normal")
        self.initialize()

    def initialize(self):
        self.hideturtle()
        self.speed(0)
        self.width(3)
        self.teleport(self.screen_width / 2 * -1, self.startline_y)
        self.goto(self.screen_width / 2, self.startline_y)
        self.teleport(self.screen_width / 2 * -1, self.finishline_y)
        self.goto(self.screen_width / 2, self.finishline_y)

    def print_lose(self):
        self.teleport(0, 50)
        self.write(f"GAME OVER", align="center", font=self.font)
        self.teleport(0, -50)
        self.write(f"You ran out of lives!", align="center", font=self.font)

    def print_win(self):
        self.teleport(0, 0)
        self.write(f"YOU WIN!", align="center", font=self.font)


class GetReady(Turtle):

    def __init__(self):
        super().__init__()
        self.font = ("Arial", 40, "normal")
        self.initialize()

    def initialize(self):
        self.hideturtle()

    def get_ready(self):
        self.teleport(0, 0)
        self.write("Get Ready!", align="center", font=self.font)
