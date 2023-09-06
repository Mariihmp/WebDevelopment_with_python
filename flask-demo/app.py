import random
from flask import Flask

goal = random.randint(0, 10)
app = Flask(__name__)

home_page = '<h1>Guess a number between 0 and 9</h1>' \
            '<img src="https://media2.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width="480" height="480" /> '
low_number = '<h1>It\'s too low, try again!</h1>' \
             '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width="480" height="480" />'
high_number = '<h1>It\'s too high, try again!</h1>' \
             '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width="480" height="480" />'
correct_number = '<h1>GOT ITTT!</h1>' \
             '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width="480" height="480" />'


@app.route("/")
def hello_world():
    return home_page


@app.route("/<int:guess>")
def guess_page(guess):
    global goal
    if guess < goal:
        return low_number
    elif guess > goal:
        return high_number
    else:
        goal = random.randint(0, 10)  # Refresh the number each time the user found the answer
        return correct_number


if __name__ == "__main__":
    app.run(debug=True)