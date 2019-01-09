import difflib
import random
import json

players = {}

def new_player(username):
    if username in players:
        return False
    else:
        players[username] = dict(attempt = 0, which_quest = 1, points = 0)
        return True
    

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
        question = False
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

def calc_points(username):
    riddles = (players[username]['which_quest']) - 1
    attempts = players[username]['attempt']
    points = str(riddles) + " / " + str(attempts)
    players[username]['points'] = points
    write_to_file("data/users.json")
    return points
    
def create_leaderboard():
    try:
        with open("data/users.json") as users_json:
            users = json.load(users_json)
        list_back = []
        for name, point in users.items():
            list_back.append(name)
            list_back.append(point["points"])
        return list_back
    except ValueError, e:
        return False