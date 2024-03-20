from turtle import Turtle
from time import sleep

class Boundary(Turtle):

    def __init__(self, width, height):
        super().__init__()
        self.x = width / 2 - 10
        self.y = height / 2 - 10
        self.initialize()

    def initialize(self):
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.teleport(self.x * -1, self.y * -1)
        self.pensize(5)
        self.pendown()
        self.goto(self.x, self.y * -1)
        self.color("blue")
        self.goto(self.x, self.y)
        self.color("white")
        self.goto(self.x * -1, self.y)
        self.color("blue")
        self.goto(self.x * -1, self.y * -1)
        self.teleport(0, self.y * -1)
        self.seth(90)
        self.color("white")
        self.pensize(1)
        while self.pos()[1] != self.y:
            self.pendown()
            self.fd(10)
            self.penup()
            self.fd(10)

    def left_win(self):
        self.clear()
        self.teleport(0, 0)
        self.write("LEFT WINS!", align="center", font=("Arial", 40, "normal"))

    def right_win(self):
        self.clear()
        self.teleport(0, 0)
        self.write("RIGHT WINS!", align="center", font=("Arial", 40, "normal"))


class Scoreboard(Turtle):

    def __init__(self, width, height, player):
        super().__init__()
        self.x = width / 2
        self.y = height / 2 - 75
        self.player = player
        self.score = 0
        self.initialize()
        self.update_score()

    def initialize(self):
        self.hideturtle()
        self.speed(0)
        self.color("white")
        if self.player == "right":
            self.teleport(self.x / 2, self.y)
        elif self.player == "left":
            self.teleport(self.x / 2 * -1, self.y)
    
    def update_score(self):
        self.clear()
        self.write(self.score, align="center", font=("Arial", 40, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.update_score()
        if self.score >= 3:
            return False
        else:
            return True


class Countdown(Turtle):

    def __init__(self, countdown_time):
        super().__init__()
        self.countdown_time = countdown_time
        self.initialize()

    def initialize(self):
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.teleport(0, 0)
        self.pensize(5)

    def countdown(self, screen):
        timer = self.countdown_time
        while timer != 0:
            self.write(timer, align="center", font=("Arial", 40, "normal"))
            timer -= 1
            screen.update()
            sleep(1)
            self.clear()

        