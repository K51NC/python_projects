# change these two file locations according to your setup
LOGO_FILE = "./019_PASSWORD_MANAGER/input/logo.png"
DATA_FILE = "./019_PASSWORD_MANAGER/output/data.json"
LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
SYMBOLS = ["#", "@", "$", "%", "^", "&", "(", ")"]

JSON_DECODE_ERROR_MSG = """
"An error occurred while reading your database. You have the following options:\n
1) (Easy) Delete your current database ('data.json') and restart the program. \
This will cause you to lose all your previous entries.\n
2) (Difficult) Find the error in your database ('data.json') and correct it. \
This option allows you to keep your previous entries.
"""