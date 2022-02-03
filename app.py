from boggle import Boggle
from flask import Flask, render_template
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
def check_guess(guess):
    result = boggle_game.check_valid_word(game_board, guess)
    if result == 'ok':
        print('ok')
    elif result == 'not-on-board':
        print('that word is not on the board')
    elif result == 'not-word':
        print("that's not even a word")
    