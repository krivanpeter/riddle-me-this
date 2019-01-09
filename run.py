import os
import json
from flask import Flask, redirect, render_template, url_for, request
from game import *

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        username = request.form["username"].title()
        if (new_player(username)) == True:
            write_to_file("data/users.json")
        else:
            exist = True
            return render_template("index.html", exist = exist)
        return redirect(url_for("user", username = username, which_quest = players[username]['which_quest']))
    return render_template("index.html")

@app.route('/<username>/<which_quest>', methods=["GET", "POST"])
def user(username, which_quest):
    points = calc_points(username)
    if request.method == "POST":
        answer = request.form["answer"].lower()
        if check_answer(username, answer):
            question = get_question(username)
            if which_quest == 11:
                return render_template("game.html", question = question, points = points)
            else:
                return redirect(url_for("user", username = username, which_quest = players[username]['which_quest']))
        else:
            question = get_question(username)
            return render_template("game.html", question = question, answer = answer)
    else:
        question = get_question(username)
        return render_template("game.html", question = question, points = points)
        

@app.route('/leaderboard')
def leaderboard():
    if (create_leaderboard()) == False:
        return render_template("leaderboard.html")
    else:
        users = create_leaderboard()
        return render_template("leaderboard.html", users = users)
    
 

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)