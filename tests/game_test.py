import unittest
from app.models.player import Player
from app.models.game import *

class TestGame(unittest.TestCase):

    def setUp(self):
        self.dwayne_johnson = Player("Dwayne", "rock")
        self.paper_mario = Player("Mario", "paper")
        self.edward_scissorhands = Player("Edward", "scissors")
        self.geodude = Player("Geodude", "rock")

    def test_rock_beats_scissors(self):
        result = get_winner(self.dwayne_johnson, self.edward_scissorhands)
        self.assertEqual(self.dwayne_johnson, result)


    def test_scissors_loses_to_rock(self):
        result = get_winner(self.edward_scissorhands, self.dwayne_johnson)
        self.assertEqual(self.dwayne_johnson, result)


    def test_scissors_beats_paper(self):
        result = get_winner(self.edward_scissorhands, self.paper_mario)
        self.assertEqual(self.edward_scissorhands, result)


    def test_paper_loses_to_scissors(self):
        result = get_winner(self.paper_mario, self.edward_scissorhands)
        self.assertEqual(self.edward_scissorhands, result)


    def test_paper_beats_rock(self):
        result = get_winner(self.paper_mario, self.dwayne_johnson)
        self.assertEqual(self.paper_mario, result)

    def test_rock_loses_to_paper(self):
        result = get_winner(self.dwayne_johnson, self.paper_mario)
        self.assertEqual(self.paper_mario, result)

    def test_draw_returns_none(self):
        result = get_winner(self.dwayne_johnson, self.geodude)
        self.assertEqual(None, result)