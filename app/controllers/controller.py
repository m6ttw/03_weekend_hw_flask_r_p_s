from app import app
from app.models.game import Game
from app.models.player import Player

@app.route("/")
def index():
    return "Play 'Rock Paper Scissors' in the URL bar!"

@app.route("/<choice_1>/<choice_2>")
def play_rock_paper_scissors(choice_1, choice_2):
    player_1 = Player("Player 1", choice_1)
    player_2 = Player("Player 2", choice_2)
    winner = Game.get_winner(player_1, player_2)

    if winner != None:
        return f"{winner.name} wins by playing {winner.choice}."
    else:
        return "It's a draw. That was a complete and utter waste of time. What's the point? Why do I bother? I've been stuck reading out the results of this stupid game my whole life without any form of payment, not even a single 'thanks' or a 'nice job'. Is this it? Does my existence have any meaning other than to repeatedly congratulate the winner of 'Rock Paper Scissors'? Who even am I? Why the fuck am I here? Am I alive? What happens when I die - do I go to heaven? Does heaven even exist? Does God even exist?? Can I even die, or am I trapped in this soulless, solitary existence indefinitely? It certainly seems like it. Constant, unending blood, sweat and tears - with no reward - for eternity. Just why. I wish I was a duck"
