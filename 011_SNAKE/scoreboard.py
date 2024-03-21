from turtle import Turtle


class scoreboard:

    def __init__(self, location_y, high_score):
        self.score = Turtle()
        self.score.speed(0)
        self.score.pencolor("white")
        self.score.hideturtle()
        self.score.penup()
        self.score_location_y = location_y / 2 + 10
        self.init_position = (0, self.score_location_y)
        self.current_score = 0
        self.high_score = high_score
        self.score.setposition(self.init_position)
        self.update_score()

    def update_score(self):
        self.score.clear()
        self.score.teleport(-200, self.score_location_y)
        self.score.write(f"Score: {self.current_score}", align="center", font=("Arial", 16, "normal"))
        self.score.teleport(200, self.score_location_y)
        self.score.write(f"High Score: {self.high_score}", align="center", font=("Arial", 16, "normal"))

    
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

    def check_high_score(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        self.update_score()