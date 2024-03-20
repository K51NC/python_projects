from turtle import Turtle

class Player(Turtle):

    def __init__(self, width, height, shape):
        super().__init__()
        self.lives = Lives(width=width, height=height)
        self.board_width = width
        self.board_height = height
        self.startx = 0
        self.starty = height / 2 * -1 + 25
        self.char = shape
        self.car_collision = False
        self.frozen = True
        self.initialize()

    def initialize(self):
        self.speed(0)
        self.shapesize(1, 1)
        self.seth(90)
        self.shape(self.char)
        self.penup()
        self.teleport(self.startx, self.starty)
    
    def restart(self):
        self.initialize()
        
    def move_fd(self):
        if self.ycor() < self.board_height / 2 - 25 and self.frozen == False:
            self.fd(25)

    def move_backward(self):
        if self.ycor() > self.board_height / 2 * -1 + 25 and self.frozen == False:
            self.backward(25)

    def check_collision(self, car):
        if int(car.ycor()) == int(self.ycor()) and self.distance(car) < 30:
            self.car_collision = True


class Lives(Turtle):

    def __init__(self, width, height):
        super().__init__()
        self.lives = 3
        self.font = ("Arial", 20, "normal")
        self.position_1x = width / 2 * -1 + 20
        self.position_1y = height / 2 - 50
        self.position_2x = width / 2 - 20
        self.position_2y = height / 2 - 50
        self.initialize()
        self.update_score()

    def initialize(self):
        self.hideturtle()
        self.speed(0)

    def update_score(self):
        print(self.position_1x, self.position_1y)
        self.clear()
        self.teleport(self.position_1x, self.position_1y)
        self.write(f"Lives: {self.lives}", align="left", font=self.font)
        self.teleport(self.position_2x, self.position_2y)
        self.write(f"Lives: {self.lives}", align="right", font=self.font)

    def reduce_lives(self):
        self.lives -= 1
        self.update_score()
