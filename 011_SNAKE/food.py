from turtle import Turtle
from random import randint

class Food:

    def __init__(self, x_pos, x_neg, y_pos, y_neg, size):
        self.food = Turtle()
        self.location = (0, 0)
        self.size = size
        self.border_pos_x = int(x_pos)
        self.border_neg_x = int(x_neg)
        self.border_pos_y = int(y_pos)
        self.border_neg_y = int(y_neg)
        self.init_turtle()


    def get_new_location(self, snake):
        restart = True
        while restart:
            restart = False
            for each in snake:
                x = (
                    randint(self.border_neg_x + self.size, self.border_pos_x - self.size)
                    // self.size) * self.size
                y = (
                    randint(self.border_neg_y + self.size, self.border_pos_y - self.size)
                    // self.size) * self.size
                if (x, y) == each.position():
                    print(f"new food was on object at {x, y}")
                    restart = True

        self.location = (x, y)
        self.place_food()
    
    def check_food_collision(self, piece_position):
        if (
            round(piece_position[0]) == self.location[0]
            and round(piece_position[1]) == self.location[1]
        ):
            return True
        else:
            return False

    def init_turtle(self):
        self.food.hideturtle()
        self.food.speed(0)
        self.food.color("white")
        self.food.shape("square")
        self.food.penup()
        
    def place_food(self):
        self.food.clear()
        self.food.setposition(self.location)
        self.food.dot(self.size)
