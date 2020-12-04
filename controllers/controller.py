from app import app
from src.game import *

@app.route("/")
def index():
    return "Play 'Rock Paper Scissors' in the URL bar!"

@app.route("/rock")
def rock_only():
    return "You can't play with only one player! Duhhh!!!"

@app.route("/paper")
def paper_only():
    return "Don't you have a friend to play with? That's a bit sad"

@app.route("/scissors")
def scissors_only():
    return "Pretend you have friends and you're playing against one of them - put their choice in the URL bar"

@app.route("/rock/scissors")
def rock_beats_scissors_browser():
    return "Player 1 wins because rock beats scissors!"

@app.route("/scissors/rock")
def scissors_loses_to_rock_browser():
    return "Player 2 wins because rock beats scissors!"

@app.route("/scissors/paper")
def scissors_beats_paper_browser():
    return "Player 1 wins because scissors beats paper!"

@app.route("/paper/scissors")
def paper_loses_to_scissors_browser():
    return "Player 2 wins because scissors beats paper!"

@app.route("/paper/rock")
def paper_beats_rock_browser():
    return "Player 1 wins because paper beats rock!"

@app.route("/rock/paper")
def rock_loses_to_paper_browser():
    return "Player 2 wins because paper beats rock!"

@app.route("/rock/rock")
def rock_and_rock_draw():
    return "It's a draw! Both players lose"

@app.route("/paper/paper")
def paper_and_paper_draw():
    return "It's a draw... how boring"

@app.route("/scissors/scissors")
def scissors_and_scissors_draw():
    return "It's a draw. That was a complete and utter waste of time. What's the point? Why do I even bother? I've been stuck reading out the results of this stupid game my whole life without any form of payment, not a single 'thanks' or a 'nice job'. Is this it? Does my existence have any meaning other than to repeatedly congratulate the winner of 'Rock Paper Scissors'? Who even am I? Why the fuck am I here? Am I alive? What happens when I die - do I go to heaven? Does heaven even exist? Does God even exist?? Can I even die, or am I trapped in this soulless, solitary existence indefinitely? It certainly seems like it. Constant, unending blood, sweat and tears - with no reward - for eternity. Just why. I wish I was a duck"
