from gameboard import Gameboard
from scoreboard import scoreboard
from snake import Snake
from food import Food
import time

file_location = "./011_SNAKE/high_score.txt"
with open(file_location) as file:
    try:
        high_score = int(file.read())
    except:
        high_score = 0

snake_width = 20
game_board = Gameboard()
snake = Snake(snake_width)
scoreboard = scoreboard(game_board.board_size_y, high_score=high_score)
food_piece = Food(
    x_neg=game_board.border_neg_x,
    x_pos=game_board.border_pos_x,
    y_neg=game_board.border_neg_y,
    y_pos=game_board.border_pos_y,
    size=snake_width
    )


game_board.screen.onkeypress(key="w", fun=snake.go_up)
game_board.screen.onkeypress(key="a", fun=snake.go_left)
game_board.screen.onkeypress(key="s", fun=snake.go_down)
game_board.screen.onkeypress(key="d", fun=snake.go_right)
game_board.screen.onkeypress(key="c", fun=snake.color_change)


is_running = True
wall_collision = False
self_collision = False
food_change = False
food_piece.get_new_location(snake.whole_snake)
lives = 3

while is_running and lives > 0:
    lives -= 1
    while wall_collision == False and self_collision == False:
        snake.move()
        game_board.screen.update()
        time.sleep(.1)
        food_change = food_piece.check_food_collision(
            snake.whole_snake[0].position()
            )
        if food_change:
            scoreboard.increase_score()
            food_piece.get_new_location(snake.whole_snake)
            snake.add_snake_piece()
            food_change = False
        else:
            wall_collision = game_board.check_border_collision(
                snake.whole_snake[0].position()
                )
            self_collision = snake.check_snake_collision()
        
    # scoreboard.game_over()
    scoreboard.check_high_score()
    end_pieces = snake.whole_snake[3:]
    for each in end_pieces:
        each.teleport(1000, 0)
        each.hideturtle()
    snake.whole_snake = snake.whole_snake[:3]
    snake.whole_snake[0].setposition(0, 0)
    scoreboard.current_score = 0
    scoreboard.update_score()
    wall_collision = False
    self_collision = False










game_board.exit()
with open(file_location, "w" ) as file:
    file.write(str(scoreboard.high_score))