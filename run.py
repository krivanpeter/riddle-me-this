import os
from flask import Flask, redirect, render_template, request
from game import *

app = Flask(__name__)
answers = []

def write_to_file(filename, data):
    """Handle the process of writing data to a file"""
    with open(filename, "a") as file:
        file.writelines(data)
        
def add_answer(username, answer):
    """Add answers to the `answers` text file"""
    write_to_file("data/answers.txt", "{0}".format(answer))

@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        write_to_file("data/users.txt", request.form["username"] + "\n")
        return redirect(request.form["username"])
    return render_template("index.html")


@app.route('/<username>', methods=["GET", "POST"])
def user(username):
    if request.method == "POST":
        add_answer(username, request.form["answer"] + "\n")
    question = get_question()
    return render_template("game.html", question=question)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)