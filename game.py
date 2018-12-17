import difflib
import random
import json

players = {}

def new_player(username):
    players[username] = dict(attempt = 0, which_quest = 1)

def write_to_file(filename):
    with open(filename, "w") as file:
        file.write(json.dumps(players, indent=4))

def open_riddles(username, what_to_check):
    which_quest = players[username]['which_quest']
    with open("data/riddles.json") as riddle_json:
        riddles = json.load(riddle_json)
    return riddles[str(which_quest)][what_to_check]
    
def get_question(username):
    with open("data/riddles.json") as riddle_json:
        riddles = json.load(riddle_json)
    if players[username]['which_quest'] > len(riddles):
        question = "No more riddle"
    else:
        question = open_riddles(username, "question")
    return question
    
def check_answer(username, got_answer):
    answer = open_riddles(username, "answer")
    if answer == got_answer:
        players[username]['which_quest'] += 1
        players[username]['attempt'] += 1
        write_to_file("data/users.json")
        return True
    else:
        players[username]['attempt'] += 1
        return False