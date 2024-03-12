from base64 import b64decode
from my_tools import printer

class Question:

    def __init__(self, id, name, difficulty):
        self.qty = 1
        self.category_id = id
        self.category_name = name
        self.difficulty = difficulty
        self.type = "boolean"

    def get_question(self, api):
        question_data= api.get_question(self.qty, self.category_id, self.difficulty, self.type)
        question_bytes = b64decode(question_data["results"][0]["question"])
        answer_bytes = b64decode(question_data["results"][0]["correct_answer"])
        self.question = question_bytes.decode('ascii')
        self.answer = answer_bytes.decode('ascii')

    def ask_question(self):
        sleep_time = .02
        printer(f"The category is: {self.category_name}", sleep_time)
        printer("(T)rue of (F)alse:", sleep_time)
        printer(" ", 3)
        printer(self.question, sleep_time)