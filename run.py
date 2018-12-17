import os
import json
from flask import Flask, redirect, render_template, request
from game import *

app = Flask(__name__)

def write_to_file(filename):
    """Handle the process of writing data to a file"""
    with open(filename, "w") as file:
        file.write(json.dumps(players, indent=4))
        #file.writelines(data)

@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        new_player(request.form["username"])
        write_to_file("data/users.json")
        return redirect(request.form["username"])
    return render_template("index.html")


@app.route('/<username>', methods=["GET", "POST"])
def user(username):
    #if request.method == "POST":
        question = get_question(username)
        return render_template("game.html", question = question)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)