from boggle import Boggle
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'my-secret-key'

toolbar = DebugToolbarExtension(app)

boggle_game = Boggle()
