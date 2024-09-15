from flask import Flask
import random


app = Flask(__name__)


@app.route("/")
def home():
    return '<h1>Guess a number between 0 and 9</h1><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


def compare_numbers(function):
    def wrapper_function(**kwargs):
        rnd_int = random.randint(0, 9)
        user_no = function(**kwargs)
        if user_no < rnd_int:
            return ('<h1 style="color: red">Guess is too low!</h1>'
                    '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
        elif user_no > rnd_int:
            return ('<h1 style="color: purple">Guess is too high!</h1>'
                    '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
        elif user_no == rnd_int:
            return ('<h1 style="color: green">You are correct!</h1>'
                    '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')

    return wrapper_function


@app.route("/<int:number>")
@compare_numbers
def get_number(number):
    return number


if __name__ == "__main__":
    app.run(debug=True)
