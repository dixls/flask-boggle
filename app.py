from boggle import Boggle
from flask import Flask, render_template, request
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
    global correct_guesses
    guess = request.get_json()['guess']
    result = boggle_game.check_valid_word(game_board, guess)
    response = {
        'answers': correct_guesses,
        'result': False
    }
    if result == 'ok':
        if guess in correct_guesses:
            response.message = "You already got that one."
        else:
            correct_guesses.append(guess)
            response[result] = True
        return response
    elif result == 'not-on-board':
        return response
    elif result == 'not-word':
        return response

@app.route('/guess', methods=["GET"])
def get_guesses():
    response = {
        'answers': correct_guesses
    }
    return response