from app import app
# from src.game import *

@app.route("/")
def index():
    return "Hello, World!"