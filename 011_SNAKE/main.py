from gameboard import Gameboard
from scoreboard import scoreboard
from snake import Snake
from food import Food
import time

snake_width = 20
game_board = Gameboard()
snake = Snake(snake_width)
scoreboard = scoreboard(game_board.board_size_y)
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

while is_running:
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
        
    scoreboard.game_over()
    break











game_board.exit()