from question import Question
from api_handler import APIHandler
from my_tools import printer

class QuizEngine:

    def __init__(self):
        self.api = APIHandler()
        self.quantity = 0
        self.categories = []
        self.category_id = 0
        self.category_name = ""
        self.difficulty = ""
        self.player_score = 0
        self.total_asked = 0
    
    def update_categories(self):
        self.categories = self.api.get_categories()

    def set_category(self):
        if self.categories:
            for index in range(0, len(self.categories)):
                printer(f"{index + 1}: {self.categories[index]["name"]}")
            while True:
                try:
                    printer("Type the number of the category:")
                    player_selection = int(input())
                    break
                except:
                    printer("Please use a numeric value.")
            player_selection_index = player_selection - 1
            self.category_id = self.categories[player_selection_index]["id"]
            self.category_name = self.categories[player_selection_index]["name"]
        else:
            printer("No categories exist.")
    
    def set_difficulty(self):
        while True:
            printer("(E)asy, (M)edium, or (H)ard?")
            q_difficulty = str(input()).lower()
            if q_difficulty == "e" or q_difficulty == "easy":
                self.difficulty = "easy"
                break
            elif q_difficulty == "m" or q_difficulty == "medium":
                self.difficulty = "medium"
                break
            elif q_difficulty == "h" or q_difficulty == "hard":
                self.difficulty = "hard"
                break
            else:
                printer("Invalid selection.")

    def set_quantity(self):
        while True:
            try:
                printer("How many questions would you like to be asked? ")
                self.quantity = int(input())
                break
            except:
                printer("Please us a numeric value.")
    
    def set_question(self):
        self.question_handler = Question(self.category_id, self.category_name, self.difficulty)
        self.question_handler.get_question(self.api)

    def ask_question(self):
        self.question_handler.ask_question()

    def check_answer(self):
        while True:
            player_answer = str(input()).lower()
            if player_answer == 't' or player_answer == 'true':
                answer = "True"
                break
            elif player_answer == 'f' or player_answer == 'false':
                answer = "False"
                break
            else:
                printer("Invalid answer. (T)rue or (F)alse?")
        if answer == self.question_handler.answer:
            self.player_score += 1
            self.total_asked += 1
            printer("That's correct!")
        else:
            self.total_asked += 1
            printer("Incorrect.")