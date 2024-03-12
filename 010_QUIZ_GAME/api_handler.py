import requests
from my_tools import printer

class APIHandler:

    def __init__(self):
        self.token_call = "https://opentdb.com/api_token.php?command=request"
        self.categories = "https://opentdb.com/api_category.php"
        self.token = self.get_token()
        self.encode_type = "base64"

    def get_token(self):
        response = requests.get(self.token_call)
        if response.status_code == 200:
            try:
                return response.json()["token"]
            except:
                printer("Error: Session token not set.")
                return None

    def get_categories(self):
        response = requests.get(self.categories)
        category_list = []
        if response.status_code == 200:
            for each in response.json()["trivia_categories"]:
                category_list.append(each)
        return category_list
    
    def get_question(self, qty, category_id, difficulty, type):
        response = requests.get(f"https://opentdb.com/api.php?amount={qty}&category={category_id}&difficulty={difficulty}&type={type}&encode={self.encode_type}&token={self.token}")
        if response.status_code == 200:
            try:
                return response.json()
            except:
                printer("Error retrieving question.")