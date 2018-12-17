import difflib
import random
import json

players = {}
def new_player(username):
    players[username] = dict(points = 0, which_quest = 1)
    
def get_question(username):
    which_quest = players[username]['which_quest']
    with open("data/riddles.json") as riddle_json:
        riddles = json.load(riddle_json)
        question = riddles[str(which_quest)]['question']
    players[username]['which_quest'] += 1
    return question
