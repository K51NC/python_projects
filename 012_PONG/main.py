from turtle import Screen
from paddle import Paddle
from ball import Ball
from gameboard import Boundary, Scoreboard, Countdown
from random import choice
from time import sleep

screen_width = 1200
screen_height = 900
r_paddle_x = (screen_width / 2) - 50
l_paddle_x = ((screen_width / 2) - 50) * -1
players = ["left", "right"]
countdown = Countdown(3)

screen = Screen()
screen.listen()
screen.title("Pong")
screen.tracer(0)
screen.bgcolor("black")
screen.setup(screen_width, screen_height)


r_paddle = Paddle(x=r_paddle_x, y=0)
l_paddle = Paddle(x=l_paddle_x, y=0)
ball = Ball()
boundary = Boundary(screen_width, screen_height)
l_scoreboard = Scoreboard(screen_width, screen_height, "left")
r_scoreboard = Scoreboard(screen_width, screen_height, "right") 
# screen.update()

screen.onkeypress(key="Up", fun=r_paddle.go_up)
screen.onkeypress(key="Down", fun=r_paddle.go_down)
screen.onkeypress(key="w", fun=l_paddle.go_up)
screen.onkeypress(key="s", fun=l_paddle.go_down)



current_start_player = choice(players)
game_running = True
round_running = True
while game_running:
    countdown.countdown(screen)
    ball.start_ball(current_start_player)
    while round_running:
        sleep(.03)
        screen.update()
        ball.move_ball()
        ball.check_screen_collision(screen_height)


        if ball.xcor() > r_paddle_x - 30 and ball.distance(r_paddle) < 50:
            ball.x_mov *= -1
        elif ball.xcor() < l_paddle_x + 30 and ball.distance(l_paddle) < 50:
            ball.x_mov *= -1

        if ball.xcor() == screen_width / 2:
            round_running = l_scoreboard.increase_score()
            if round_running == True:
                ball.reset()
                ball = Ball()
                ball.start_ball("right")
                countdown.countdown(screen)
        elif ball.xcor() == screen_width / 2 * -1:
            round_running = r_scoreboard.increase_score()
            if round_running == True:
                ball.reset()
                ball = Ball()
                ball.start_ball("left")
                countdown.countdown(screen)

    ball.reset()
    l_paddle.reset()
    r_paddle.reset()
    if l_scoreboard.score > r_scoreboard.score:
        boundary.left_win()
    else:
        boundary.right_win()
        
    game_running = False


















screen.mainloop()