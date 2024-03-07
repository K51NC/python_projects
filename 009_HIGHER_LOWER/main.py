import json
import os
from imdb import IMDb
from datetime import datetime
from art import title
from random import randint
from time import sleep

def clear():
    if os.name == 'nt':
        os.system("clr")
    else:
        os.system("clear")

def updateRatings():
    """This updates the "ratings" database."""

    def updateTitles():
        """Sets the titles from the "movies" file. This "movies" file can be altered to change which movies are used in the "ratings" database."""
        with open(movies_file, "r") as file:
            movieTitles = file.read()
            moviesList = movieTitles.split("\n")
        
        data["movies"] = []

        while len(data["movies"]) < len(moviesList):
            data["movies"].append({})

        for _ in range(0, len(moviesList)):
            data["movies"][_]["title"] = moviesList[_]

    def setMetaData(movie):
        """Sets the metadata of the movie."""
        try:
            movTitle = movie["title"]
            search_results = imdbDB.search_movie(movTitle)
            movID = search_results[0].getID()
            mov = imdbDB.get_movie(movID)

            # if movID:
            movie["year"] = mov["year"]
            movie["movieID"] = movID
            movie["rating"] = mov["rating"]
            print(f"{movTitle} ({movie["year"]})")
            return False
        except:
            print(f"No search results for {movTitle}.")
            return True

    data = {}
    print("Please wait. This may take a few minutes.")
    # progress bar here?

    # update ratings file with titles from the movie list file
    updateTitles()

    # get metadata for each movie in movie list
    for movie in data["movies"]:
        remove = setMetaData(movie)
        if remove:
            data["movies"].remove(movie)
    
    data["last_update"] = currentDate

    return data

def loadScoresFile():
    """Loads the "scores" database or creates a new one if it does not exist."""
    try:
        with open(scores_file, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open(scores_file, "w") as file:
            data = {"last_update": currentDate, "players": [{"name": "Nobody", "highscore": 0, "date_of_highscore": currentDate}], "current_highscore": {"name": "Nobody", "highscore": 0, "date_of_highscore": currentDate}}
            json.dump(data, file)
    return data

def loadRatingsFile():
    """Loads the "ratings" database or creates a new one if it does not exist."""
    try:
        with open(ratings_file, "r") as file:
            data = json.load(file)
            manualUpdate(data)
    except FileNotFoundError:
        print("Database setting up for the first time.")
        with open(ratings_file, "w") as file:
            data = updateRatings()
            json.dump(data, file)

    return data

def manualUpdate(data):
    """Allows the user to manually update the "ratings" database."""
    while True:
        print(f"Ratings database was last updated on {data["last_update"]}.")
        # print("Update 'ratings' database? WARNING: Process takes 5-10 minutes if you choose and cannot be interrupted.")
        update = input("Update 'ratings' database? 'y' or 'n'?\n").lower()
        if update == 'n' or update == 'no':
            break
        elif update == 'y' or update == 'yes':
            verifyUpdate = input("Are you sure? WARNING: If you choose 'y', this process takes 5-10 minutes and cannot be interrupted.\n").lower()
            if verifyUpdate != 'y' and verifyUpdate != 'yes':
                break
            else:
                data = updateRatings()
                with open(ratings_file, "w") as file:
                    json.dump(data, file)
                break
        else:
            print("Invalid input. Please type 'y' or 'n'.")

def chooseMovie(data):
    selection = data["movies"][randint(0, len(data["movies"]) - 1)]
    movTitle = selection["title"]
    movYear = selection["year"]
    movRating = selection["rating"]
    return [movTitle, movYear, movRating]

def correctAnswer(opt1: int, opt2: int, answer: str):
    if answer == 'l' or answer == 'lower':
        if opt1 > opt2:
            return True
        else:
            return False
    elif answer == 'h' or answer == 'higher':
        if opt1 < opt2:
            return True
        else:
            return False
        
def getUserName():
    while True:
        # clear()
        name = str(input("What is your name? (15 characters max)\n")).capitalize()
        if len(name) < 15 and name.isalpha():
            return name
        else:
            print("Invalid name. Only letters are accepted.")
    
def updateScores(data, index, name, score):
    clear()
    print(f"Your score this time: {score}")
    if score > data["players"][index]["highscore"]:
        new = {
            "name": name,
            "highscore": score,
            "date_of_highscore": currentDate
        }
        data["players"][index] = new

    # update highest score name, score, date
    if data["players"][index]["highscore"] > data["current_highscore"]["highscore"]:
        data["current_highscore"] = data["players"][index]
    data["last_update"] = currentDate
    return data

def newScoresUser(data, name):
    user = {
        "name": name,
        "highscore": 0,
        "date_of_highscore": currentDate
    }
    data["players"].append(user)
    return data

# inits
# currentDate = datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + " UTC"
currentDate = datetime.now().strftime("%m/%d/%Y")
imdbDB = IMDb()
sleepTime = 2
print(title)

# file paths
current_directory = os.path.dirname(os.path.abspath(__file__))
data_subfolder = os.path.join(current_directory, "data")
scores_file = os.path.join(data_subfolder, "scores.json")
ratings_file = os.path.join(data_subfolder, "ratings.json")
movies_file = os.path.join(current_directory, "movies")

# check if file scores.json exists. if it doesn't, create one
os.makedirs(data_subfolder, exist_ok=True)


# load scores file or create one if it doesn't exist
scores = loadScoresFile()

# Load ratings file or create one if it doesn't exist
ratings = loadRatingsFile()


currentHighName = scores["current_highscore"]["name"]
currentHighScore = scores["current_highscore"]["highscore"]
currentHighDate = scores["current_highscore"]["date_of_highscore"]

userName = getUserName()
userScore = 0
userAnswer = ""
clear()
print(f"Hello {userName}!")

userExist = False
for player in scores["players"]:
    if userName == player["name"]:
        userExist = True
        print(f"Welcome back!\n")
        sleep(sleepTime)

if userExist == False:
    scores = newScoresUser(scores, userName)
    print("Welcome!\n")
    sleep(sleepTime)

for index, name in enumerate(scores["players"]):
    if name["name"] == userName:
        user = name
        userIndex = index

optionOne = chooseMovie(ratings)
optionTwo = chooseMovie(ratings)

while True:
    while optionOne == optionTwo:
        optionTwo = chooseMovie(ratings)
    clear()
    print(f"Score to beat: {currentHighName} - {currentHighScore}")
    print(f"Personal best: {scores["players"][userIndex]["highscore"]}")
    print(f"Current score: {userScore}\n")
    print(f"{optionOne[0]} ({optionOne[1]})\nRating of {optionOne[2]}/10\n")
    print(f"{optionTwo[0]} ({optionTwo[1]})")
    userAnswer = input(f"Does this have a higher or lower rating than {optionOne[0]}? 'H' or 'L'\n").lower()
    if userAnswer != 'h' and userAnswer != 'l':
        print("Invalid input.")
        sleep(sleepTime)
    else:
        if correctAnswer(optionOne[2], optionTwo[2], userAnswer):
            userAnswer = ""
            optionOne = optionTwo
            userScore += 1
        else:
            newScores = updateScores(scores, userIndex, userName, userScore)
            break

with open(scores_file, "w") as file:
    json.dump(newScores, file)