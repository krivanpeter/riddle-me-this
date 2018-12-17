import difflib
import random
import json

players = {}

def new_player(username):
    players[username] = dict(points = 0, which_quest = 1)

def write_to_file(filename):
    with open(filename, "w") as file:
        file.write(json.dumps(players, indent=4))

def open_riddles(username, what_to_check):
    which_quest = players[username]['which_quest']
    with open("data/riddles.json") as riddle_json:
        riddles = json.load(riddle_json)
    return riddles[str(which_quest)][what_to_check]
    
def get_question(username):
    question = open_riddles(username, "question")
    return question
    
def check_answer(username, got_answer):
    answer = open_riddles(username, "answer")
    print(answer)
    print(got_answer)
    if answer == got_answer:
        players[username]['which_quest'] += 1
        write_to_file("data/users.json")
        return True
    else:
        return False