from turtle import Turtle, Screen


class Gameboard:

    def __init__(self):
        self.board_size_x = 800
        self.board_size_y = 800
        self.screen = Screen()
        self.screen.listen()
        self.screen.tracer(0)
        self.turtle = Turtle()
        self.turtle.speed(0)
        self.setup_board()
        self.border_pos_x = self.board_size_x / 2
        self.border_neg_x = (self.board_size_x / 2) * -1
        self.border_pos_y = self.board_size_y / 2
        self.border_neg_y = (self.board_size_y / 2) * -1

    def exit(self):
        self.screen.exitonclick()
    
    def setup_board(self):
        self.screen.bgcolor("black")
        self.screen.setup(width=1000, height=1000)
        self.setup_boundary()

    def setup_boundary(self):
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.color("white")
        self.turtle.setposition(-(self.board_size_x / 2), -(self.board_size_y / 2))
        self.turtle.pendown()
        for _ in range(4):
            self.turtle.forward(800)
            self.turtle.left(90)
        self.turtle.penup()

    def check_border_collision(self, piece):
        if piece[0] >= self.border_pos_x - 10 or piece[0] <= self.border_neg_x + 10:
            return True
        elif piece[1] >= self.border_pos_y - 10 or piece[1] <= self.border_neg_y + 10:
            return True
        else:
            return False

