STANDARD_FONT = ("Arial", 8, "normal")
SCOREBOARD_FONT = ("Arial", 30, "normal")
WIN_FONT = ("Arial", 40, "normal")


from turtle import Turtle

class Gameboard(Turtle):

    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        self.hideturtle()

    def mark_state(self, state, x, y):
        self.teleport(x, y)
        self.write(arg=state.capitalize(), align="center", font=STANDARD_FONT)
    
    def calculate_time(self, total_time):
        temp_time = total_time
        hours = int(total_time / 3600)
        temp_time -= hours * 3600
        minutes = int(temp_time / 60)
        temp_time -= minutes * 60
        seconds = round(temp_time, 2)
        self.total_time = f"{hours} hours, {minutes} minutes, {seconds} seconds"
        return total_time


    def win_message(self):
        self.clear()
        self.teleport(0, 50)
        self.write(arg="You Win!", align="center", font=WIN_FONT)
        self.teleport(0, -50)
        self.write(arg=f"It took you {self.total_time}", align="center", font=("Arial", 20, "normal"))

class Scoreboard(Turtle):

    def __init__(self, height):
        super().__init__()
        self.y_loc = height / 2 - 50
        self.initialize()

    def initialize(self):
        self.hideturtle()
        self.teleport(0, self.y_loc)

    def update_score(self, qty):
        self.clear()
        self.write(f"You have guessed {qty}/50 states", align="center", font=SCOREBOARD_FONT)