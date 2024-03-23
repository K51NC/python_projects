# update file locations to match your specific setup
IMAGE_LOCATION = "./015_STATES_QUIZ/input/blank_states_img.gif"
STATES_LOCATION = "./015_STATES_QUIZ/input/50_states.csv"
SAVE_LOCATION = "./015_STATES_QUIZ/output/save.csv"
TIME_LOCATION = "./015_STATES_QUIZ/output/time.txt"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

from turtle import Screen
import pandas
from gameboard import Gameboard, Scoreboard
from file_handler import FileHandler
import time

# game inits
qty_guessed = 0
previous_time = 0

# screen setup
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgpic(IMAGE_LOCATION)
screen.title("States Quiz")

# gameboard setup
gameboard = Gameboard()
scoreboard = Scoreboard(SCREEN_HEIGHT)
scoreboard.update_score(qty_guessed)

# file load/create
data = pandas.read_csv(STATES_LOCATION)
data = data.to_dict()
file_handler = FileHandler()
ask_player_load = False
load_save = False

# check for and load save data
while True:
    try:
        save_data = file_handler.load(SAVE_LOCATION)
        ask_player_load = True
        break
    except:
        save_data = file_handler.create_default()
        ask_player_load = False
        break

# ask player if they want to load previous game or start a new one
while ask_player_load:
    player_load = screen.textinput("New Game?", "(C)ontinue previous game or (N)ew Game?").lower()
    if player_load == "c" or player_load == "continue":
        load_save = True
        break
    elif player_load == "n" or player_load == "new":
        save_data= file_handler.create_default()
        previous_time = 0
        load_save = False
        ask_player_load = False
        break

if load_save:
    for index in save_data["state"]:
        if save_data["state"][index] == data["state"][index]:
            gameboard.mark_state(data["state"][index], data["x"][index], data["y"][index])
            del data["state"][index]
            del data["x"][index]
            del data["y"][index]
            qty_guessed += 1
            scoreboard.update_score(qty_guessed)
    while True:
        try:
            with open(TIME_LOCATION, "r") as file:
                previous_time = float(file.read())
            break
        except:
            print("ERROR: Did not load previous time.")
            break
    load_save = False


# start game
start_time = time.time()
game_is_running = True
while game_is_running:

    # player guess
    player_guess = screen.textinput(f"Guess all the states!", "Enter a state or 'exit':").lower()

    # exit procedure
    if player_guess == "exit":
        time_stopped = gameboard.calculate_time(time.time() - start_time + previous_time)
        file_handler.save(save_data, SAVE_LOCATION, time_stopped, TIME_LOCATION)
        break

    # primary game component. check answer and update data.
    for index in data["state"]:
        if player_guess == data["state"][index].lower():
            gameboard.mark_state(data["state"][index], data["x"][index], data["y"][index])
            save_data["state"][index] = data["state"][index]
            save_data["x"][index] = data["x"][index]
            save_data["y"][index] = data["y"][index]
            del data["state"][index]
            del data["x"][index]
            del data["y"][index]
            qty_guessed += 1
            scoreboard.update_score(qty_guessed)
            break
    
    # win condition procedure
    if len(data["state"]) == 0:
        game_is_running = False
        gameboard.calculate_time(time.time() - start_time + previous_time)
        gameboard.win_message()
        file_handler.reset(SAVE_LOCATION, TIME_LOCATION)


game_is_running = False
screen.mainloop()