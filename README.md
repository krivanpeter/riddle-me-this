# The Simon Game

I'm a student at Code Institute and I've reached my third milestone project which was to create this webapplication.

## What does it do?

This website shows riddles and waits for answer from the user.
It checks if the answers are right or not, saves the user and his points.
It shows the points of all the users in a leaderboard.

## Features

Existing Features

    Username    - allows users to start a new game with unique username, by having them write it in a form and submit it
    Riddle      - allows users to see the riddle which they have to see, by save at which question they are
    Answer      - allows users to submit an answer to riddles, by write it to text input and submit it with button
                - allows users to see if the answer was not right, by having them see the wrong answers when it is submitted
    Points      - allows users to see how many points they earned by answering the last riddle
    Leaderboard - allows users to see the points of all the players, by go on 'Leaderboard' page
    Log Out     - allows users to log out and start a new game with a new account

## Features Left to Implement

    None

## Technologies Used

    HTML, CSS and Javascript
        Base languages used to create website
    Bootstrap
        Use Bootstrap to give this project a simple, responsive layout
    JQuery
        Use JQuery for boostrap and displaying modal
    Python/Flask
        Use Python language to create a Flask web application.
        It gives the page the logic
    Git/GitHub
        Use Git for version control.

## Testing

Automated tests was not written but all of the elements of the page has been tested manually on:
* Mozilla Firefox
* Internet Explorer
* Google Chrome

Scenerios:
1. Username form:
    1. Try to submit the empty form, an error message about the required field appears
    2. Try to submit an existing username, an error message appears
    3. Try to submit the form with valid input and you will be forwarded to the first riddle
2. Answer form:
    1. Try to submit the empty form, an error message about the required field appears
    2. Try to submit a worng answer, you stay at the same riddle and text with wrong answer appears
    3. Try to submit the form with good answer and you will be forwarded to the next riddle  
    4. If there is no more riddle you will get your score and can go to ,,Leaderboard"
3. Leaderboard:
    1. If there was no player before, you see a text says ,,You can be the first"
    2. If there was player before, you see a table shows them and their scores
4. Log Out:
    1. If you want to log out you will be forwarded to the "logout" page
    2. After logout the username will be popped from session so you can start a new game

## Deployment

This project was created on [C9.IO](https://c9.io/) and was deployed to [GitHub](https://github.com/) and [Heroku](https://www.heroku.com/).

### Getting the code up and running

1. Firstly you will need to clone this repository by running the git clone <project's Github URL> command
2. After you've that you'll need to make sure that you have npm installed
3. After those dependencies have been installed you'll need to make sure that you have http-server installed.
4. After that you will need to modify the ,,app.secret_key" to any string
5. Once these are done run the server
6. The project will now run on localhost

## Credits
### Content

- The riddles were used in this site were obtained from [Riddles & Answers](https://riddles.fyi/)

### Media

- The question mark was obtained from [FreeStockPhotos](http://www.freestockphotos.biz)

### Acknowledgements

I received inspiration for this project from [Code Institute](https://codeinstitute.net/).
