from turtle import Turtle


class scoreboard:

    def __init__(self, location_y):
        self.score = Turtle()
        self.score.speed(0)
        self.score.pencolor("white")
        self.score.hideturtle()
        self.score.penup()
        self.score_location_y = location_y / 2 + 10
        self.init_position = (0, self.score_location_y)
        self.current_score = 0
        self.score.setposition(self.init_position)
        self.update_score()

    def update_score(self):
        self.score.clear()
        self.score.pendown()
        self.score.write(f"Score: {self.current_score}", align="center", font=("Arial", 16, "normal"))
        self.score.penup()
    
    def increase_score(self):
        self.current_score += 1
        self.update_score()

    def game_over(self):
        self.score.setposition(0, self.score_location_y / 2)
        self.score.write(f"GAME OVER | GAME OVER | GAME OVER", align="center", font=("Arial", 16, "normal"))
        self.score.setposition(0, 0)
        self.score.write(f"GAME OVER | GAME OVER | GAME OVER", align="center", font=("Arial", 16, "normal"))
        self.score.setposition(0, (self.score_location_y / 2) * -1)
        self.score.write(f"GAME OVER | GAME OVER | GAME OVER", align="center", font=("Arial", 16, "normal"))
