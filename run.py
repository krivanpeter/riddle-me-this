import os
import json
from flask import Flask, redirect, render_template, url_for, request
from game import *

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        if (new_player(request.form["username"].title())) == True:
            write_to_file("data/users.json")
        else:
            exist = True
            return render_template("index.html", exist = exist)
        return redirect(request.form["username"].title())
    return render_template("index.html")

@app.route('/<username>', methods=["GET", "POST"])
def user(username):
    if request.method == "POST":
        answer = request.form["answer"].lower()
        if check_answer(username, answer):
            question = get_question(username)
            points = get_points(username)
            return render_template("game.html", question = question, points = points)
        else:
            question = get_question(username)
            return render_template("game.html", question = question, answer = answer)
    else:
        question = get_question(username)
        return render_template("game.html", question = question)

@app.route('/leaderboard', methods=["GET", "POST"])
def leaderboard():
    users = create_leaderboard()
    return render_template("leaderboard.html", users = users)
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)