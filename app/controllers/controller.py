from app import app
# from src.game import *

@app.route("/")
def index():
    return "Play 'Rock Paper Scissors' in the URL bar!"
