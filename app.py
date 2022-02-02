from boggle import Boggle
from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'my-secret-key'

toolbar = DebugToolbarExtension(app)

boggle_game = Boggle()


@app.route('/')
def boggle():

    game_board = boggle_game.make_board()

    return render_template('board.html', board=game_board)