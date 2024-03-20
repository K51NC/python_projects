from turtle import Screen
from player import Player
from gameboard import Gameboard, GetReady
from car import Car
from time import sleep


screen_width = 1200
screen_height = 400


screen = Screen()
screen.tracer(0)
screen.setup(width=screen_width, height=screen_height)
screen.colormode(255)


while True:
    difficulty_input = screen.textinput("Select Difficulty", "(E)asy, (M)edium or (H)ard?").lower()
    if difficulty_input == "easy" or difficulty_input == "e":
        difficulty_actual = "easy"
        break
    elif difficulty_input == "medium" or difficulty_input == "m":
        difficulty_actual = "medium"
        break
    elif difficulty_input == "hard" or difficulty_input == "h":
        difficulty_actual = "hard"
        break
    else:
        print("ERROR: Invalid difficulty was selected.")



gameboard = Gameboard(width=screen_width, height=screen_height)
player = Player(width=screen_width, height=screen_height, shape="turtle")
cars = []
get_ready = GetReady()



rate_of_spawn = 10
default_car_speed = .1
spawn_qty = 3
spawn_timer = rate_of_spawn
car_speed = default_car_speed


if difficulty_actual == "hard":
    default_car_speed = 0.02
elif difficulty_actual == "medium":
    default_car_speed = 0.05
else:
    default_car_speed = .1

screen.listen()
screen.onkeypress(key="w", fun=player.move_fd)
screen.onkeypress(key="s", fun=player.move_backward)

game_is_running = True
round_is_running = True
player.frozen = True
get_ready.get_ready()

while game_is_running:

    while round_is_running:

        if spawn_timer == 0:
            for _ in range(0, spawn_qty):
                cars.append(Car(width=screen_width, height=screen_height))
            spawn_timer = rate_of_spawn
            if cars[0].xcor() > screen_width / 2 * -1:
                car_speed = 0.01
                player.frozen = True
            else:
                car_speed = default_car_speed
                player.frozen = False
                get_ready.clear()

        for car in cars:
            car.forward(10)
            car_collision = player.check_collision(car)
            if car.xcor() < screen_width / 2 * -1 - 100:
                cars.remove(car)

        if player.car_collision:
            round_is_running = False

        if player.ycor() > gameboard.finishline_y:
            finish_collision = True
            round_is_running = False
        
        screen.update()
        sleep(car_speed)
        spawn_timer -= 1
    
    if player.car_collision:
        player.lives.reduce_lives()
        player.restart()
        round_is_running = True
        player.car_collision = False
        screen.update()
    elif finish_collision:
        gameboard.clear()
        player.hideturtle()
        for car in cars:
            car.hideturtle()
        cars = []
        gameboard.print_win()
        game_is_running = False
        screen.update()
    
    if player.lives.lives == 0:
        gameboard.clear()
        player.hideturtle()
        for car in cars:
            car.hideturtle()
        cars = []
        gameboard.print_lose()
        game_is_running = False
        screen.update()


screen.mainloop()