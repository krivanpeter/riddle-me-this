import os
import json
from flask import Flask, redirect, render_template, url_for, request, session
from game import *

app = Flask(__name__, static_url_path='/static')
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/', methods=["GET", "POST"])
def index():
    """MAIN PAGE"""
    if request.method == "POST":
        session["username"] = request.form["username"].title()
        username = session["username"]
        # If name is not occupied then this function writes it to users.json
        if (new_player(username)) is True:
            write_to_file("data/users.json")
        # If name is occupied then this function renders
        # template with 'it already exists' message
        else:
            session.pop("username")
            exist = True
            return render_template("index.html", exist=exist)
        return redirect(url_for("game", username=username, which_quest=players[username]['which_quest']))
        # If name is in session(cookie) then game can be continued
        # by forwarding to riddle where user was
    if "username" in session:
        return redirect(url_for("game", username=session["username"], which_quest=players[session["username"]]['which_quest']))
    return render_template("index.html")


@app.route('/<username>/<which_quest>', methods=["GET", "POST"])
def game(username, which_quest):
    """GAME PAGE"""
    # Everytime this page renders point are calculated for player
    # and written to users.json
    points = calc_points(username)
    # POST happens then answer and if there is more riddles are checked
    if request.method == "POST":
        answer = request.form["answer"].lower()
        if check_answer(username, answer):
            question = get_question(username)
            if which_quest == 11:
                return render_template("game.html", username=username, question=question, points=points)
            else:
                return redirect(url_for("game", username=username, which_quest=players[username]['which_quest']))
        else:
            return redirect(url_for("bad_answer", username=username, which_quest=players[username]['which_quest'], answer=answer))
    else:
        question = get_question(username)
        return render_template("game.html", username=username, question=question, points=points)


@app.route('/<username>/<which_quest>/<answer>', methods=["GET", "POST"])
def bad_answer(username, which_quest, answer):
    """GAME PAGE when answer is bad"""
    # View is created to be able to avoid a POST when page is refreshed
    points = calc_points(username)
    if request.method == "POST":
        answer = request.form["answer"].lower()
        if check_answer(username, answer):
            return redirect(url_for("game", username=username, which_quest=players[username]['which_quest']))
        else:
            question = get_question(username)
            return redirect(url_for("bad_answer", username=username, which_quest=players[username]['which_quest'], answer=answer))
    else:
        question = get_question(username)
        return render_template("game.html", username=username, question=question, answer=answer)


@app.route('/leaderboard')
def leaderboard():
    """LEADERBOARD PAGE"""
    if (create_leaderboard()) is False:
        return render_template("leaderboard.html")
    else:
        users = create_leaderboard()
        if "username" in session:
            return render_template("leaderboard.html", username=session["username"], users=users)
        else:
            return render_template("leaderboard.html", users=users)


@app.route('/logout', methods=["GET", "POST"])
def logout():
    if request.method == "POST":
        session.pop("username")
        return redirect(url_for("index"))
    else:
        return render_template("logout.html")

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=False)
