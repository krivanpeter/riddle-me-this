import difflib
import random

questions = []
answers = []
given_answers = []


def open_riddles():
    with open("data/riddles.txt", "r") as file:
        lines = file.read().splitlines()
    for i, text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)

def get_question():
    if len(questions) > 0:
        question = questions[len(questions)-1]
        return question
    else:
        question = "No more riddle"
        return question

def check_answer(answer):
    given_answers.append(answer)
    if answers[len(questions)-1] == answer.lower():
        return True
    else:
        return False