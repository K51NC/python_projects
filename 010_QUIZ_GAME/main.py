from art import title
from quiz_engine import QuizEngine
from my_tools import printer

# inits
quiz = QuizEngine()
quiz.update_categories()
game_running = True
round_running = True


while game_running:
    if quiz.api.token != None:
        # player selections
        quiz.set_category()
        quiz.set_difficulty()
        quiz.set_quantity()

        # start round
        while round_running:
            quiz.set_question()
            quiz.ask_question()
            quiz.check_answer()
            quiz.quantity -=1
            if quiz.quantity == 0:
                round_running = False
        
        while True:
            printer(f"Your got {quiz.player_score} out of {quiz.total_asked} "
                    "correct. Would you like to play again? (Y)es or (N)o?")
            another = str(input()).lower()
            if another == 'n' or another == 'no':
                round_running = False
                game_running = False
                break
            elif another == 'y' or another == 'yes':
                round_running = True
                game_running = True
                break
            else:
                printer("Invalid answer.")
    else:
        game_running = False