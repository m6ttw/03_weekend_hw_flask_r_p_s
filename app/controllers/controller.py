from flask import render_template
from app import app
from app.models.game import Game
from app.models.player import Player

@app.route("/")
def index():
    return render_template("index.html", title="Home")

@app.route("/<choice_1>/<choice_2>")
def play_rock_paper_scissors(choice_1, choice_2):
    valid_choices = ["rock", "paper", "scissors"]
    player_choices = [choice_1, choice_2]
    count = 0

    for player_choice in player_choices:
        for valid_choice in valid_choices:
            if player_choice == valid_choice:
                count += 1
    if count < 2:
        return "One or both of you idiots made an invalid choice. The name of the game is 'rock paper scissors'. It literally tells you the options in its name. Sigh"

    player_1 = Player("Player 1", choice_1)
    player_2 = Player("Player 2", choice_2)
    game_winner = Game.get_winner(player_1, player_2)

    if game_winner != None:
        return f"{player_1.name} plays {player_1.choice} and {player_2.name} plays {player_2.choice}, so {game_winner.name} wins. Woopee."
    else:
        return "It's a draw. That was a complete and utter waste of time. What's the point? Why do I bother? I've been stuck reading out the results of this stupid game my whole life without any form of payment, not even a single 'thanks' or a 'nice job'. Is this it? Does my existence have any meaning other than to repeatedly congratulate the winner of 'rock paper scissors'? Who even am I? Why am I here? Am I alive? What happens when I die - do I go to heaven? Does heaven even exist? Does God even exist?? Can I even die, or am I trapped in this soulless, solitary existence indefinitely? It certainly seems like it. Constant, unending blood, sweat and tears - with no reward - for eternity. Just why. I wish I was a duck"
