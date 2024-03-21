from turtle import Turtle
from random import choice

class Snake:

    def __init__(self, width):
        self.snake_width = width
        self.previous_position = (-200, 0)
        self.whole_snake = []
        self.color = ("white")
        for _ in range(3):
            self.add_snake_piece()

    def add_snake_piece(self):
        piece = Turtle()
        piece.speed(3)
        piece.penup()
        piece.color(self.color)
        piece.shape("square")
        if self.whole_snake == []:
            piece.setposition(self.previous_position)
            self.whole_snake.append(piece)
        else:
            piece.setposition(
                self.whole_snake[len(self.whole_snake) - 1].position()
                )
            self.whole_snake.append(piece)
            self.move()

    def move(self):
        piece_index = len(self.whole_snake) - 1
        for _ in range(1, len(self.whole_snake)):
            new_position = self.whole_snake[piece_index - 1].position()
            self.whole_snake[piece_index].setposition(new_position)
            piece_index -= 1
        self.whole_snake[0].forward(self.snake_width)

    def go_up(self):
        if self.whole_snake[0].heading() != 90 and self.whole_snake[0].heading() != 270:
            self.whole_snake[0].setheading(90)

    def go_down(self):
        if self.whole_snake[0].heading() != 90 and self.whole_snake[0].heading() != 270:
            self.whole_snake[0].setheading(270)

    def go_left(self):
        if self.whole_snake[0].heading() != 0 and self.whole_snake[0].heading() != 180:
            self.whole_snake[0].setheading(180)

    def go_right(self):
        if self.whole_snake[0].heading() != 0 and self.whole_snake[0].heading() != 180:
            self.whole_snake[0].setheading(0)

    def check_snake_collision(self):
        for each in range(1, len(self.whole_snake)):
            if (
                round(self.whole_snake[0].position()[0])
                == round(self.whole_snake[each].position()[0])
                and round(self.whole_snake[0].position()[1])
                == round(self.whole_snake[each].position()[1])
            ):
                return True
        return False
    
    def color_change(self):
        current_color = self.color
        colors = ["white", "blue", "green", "red", "purple"]
        new_color = choice(colors)
        while new_color == current_color:
            new_color = choice(colors)
            print("DEBUG: HAD TO CHANGE COLOR")
        self.color = new_color
        for piece in self.whole_snake:
            piece.color(self.color)