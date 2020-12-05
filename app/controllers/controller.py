from app import app
# from app.models.game import Game
# from app.models.player import Player

@app.route("/")
def index():
    return "Play 'Rock Paper Scissors' in the URL bar!"
