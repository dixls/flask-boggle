from boggle import Boggle
from flask import Flask, redirect, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'my-secret-key'
app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


toolbar = DebugToolbarExtension(app)

boggle_game = Boggle()
game_board = boggle_game.make_board()
correct_guesses = []
title = "Let's Play Boggle!"

@app.route('/')
def board_render():

    global game_board

    return render_template('board.html', board=game_board, title=title)

@app.route('/guess', methods=["POST"])
def check_guess():
    """checks submitted guess and returns a dict with the updated list of correct guesses and a message and status if relevant"""
    global correct_guesses
    guess = request.get_json()['guess']
    result = boggle_game.check_valid_word(game_board, guess)
    response = {
        'answers': correct_guesses,
        'result': False,
        'message': ''
    }
    if result == 'ok':
        if guess.capitalize() in correct_guesses:
            response['message'] = "You already got that one."
        else:
            correct_guesses.append(guess.capitalize())
            response['result'] = True
            response['message'] = "Nice one!"
        return response
    elif result == 'not-on-board':
        response['message'] = "That's not here!"
        return response
    elif result == 'not-word':
        response['message'] = "That's not even a word!"
        return response

@app.route('/guess', methods=["GET"])
def get_guesses():
    """a route for the front end to retrieve correct guesses list without submitting a new guess"""
    response = {
        'answers': correct_guesses
    }
    return response

@app.route('/restart')
def restart_game():
    """creates a new board, and resets the list of correct guesses"""
    global game_board
    global correct_guesses
    global boggle_game

    boggle_game = Boggle()
    game_board = boggle_game.make_board()
    correct_guesses = []

    return redirect('/')