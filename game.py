import difflib
import random

questions = []
answers = []

def open_riddles():
    with open("data/riddles.txt", "r") as file:
        lines = file.read().splitlines()
    for i, text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)

def get_question():
    question = questions[len(questions)-1]
    return question

def check_answer(answer):
    points = 0
    answers.append(answer)
    if answers[len(questions)-1] == answer.lower():
        points += 1
        return True
    else:
        return False