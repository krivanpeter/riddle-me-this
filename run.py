import os
import json
from flask import Flask, redirect, render_template, request
from game import *

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        if (new_player(request.form["username"])) == True:
            write_to_file("data/users.json")
        else:
            exist = "Username is already in use. Please select another one!"
            return render_template("index.html", exist = exist)
        return redirect(request.form["username"])
    return render_template("index.html")

@app.route('/<username>', methods=["GET", "POST"])
def user(username):
    if request.method == "POST":
        answer = request.form["answer"]
        if check_answer(username, answer):
            question = get_question(username)
        else:
            question = get_question(username)
            return render_template("game.html",question = question, answer=answer)
    else:
        question = get_question(username)
    return render_template("game.html", question = question)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)