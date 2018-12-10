import difflib
import random

questions = []

def get_question():
    with open("data/riddles.txt", "r") as file:
        lines = file.read().splitlines()
        
    for i, text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
    
    #question = questions[random.randint(0,(len(questions)-1))]
    question = random.choice(questions)
    return question