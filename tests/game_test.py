import unittest
from src.player import Player
from src.game import *

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Player 1", "Rock")
        self.player_2 = Player("Player 2", "Paper")
        self.player_3 = Player("Player 3", "Scissors")

    def test_rock_beats_scissors(self):
        result = get_winner(self.player_1, self.player_3)
        self.assertEqual(self.player_1, result)


    def test_scissors_loses_to_rock(self):
        result = get_winner(self.player_3, self.player_1)
        self.assertEqual(self.player_1, result)


    def test_scissors_beats_paper(self):
        result = get_winner(self.player_3, self.player_2)
        self.assertEqual(self.player_3, result)


    def test_paper_loses_to_scissors(self):
        result = get_winner(self.player_2, self.player_3)
        self.assertEqual(self.player_3, result)


    def test_paper_beats_rock(self):
        result = get_winner(self.player_2, self.player_1)
        self.assertEqual(self.player_2, result)

    def test_rock_loses_to_paper(self):
        result = get_winner(self.player_1, self.player_2)
        self.assertEqual(self.player_2, result)