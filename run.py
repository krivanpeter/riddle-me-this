import os
from flask import Flask, redirect, render_template, request
from game import *

app = Flask(__name__)
question = get_question()
answers = []


def add_answers(username, answer):
    """Add answer to the `answers` list"""
    answers_dict = {"from": username, "answer": answer}
    answers.append(answers_dict)

@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        with open("data/users.txt", "a") as user_list:
            user_list.writelines(request.form["username"] + "\n")
        return redirect(request.form["username"])
    return render_template("index.html")


@app.route('/<username>')
def user(username):
    get_question()
    return render_template("game.html", question=question)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)