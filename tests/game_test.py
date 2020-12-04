import unittest
from src.player import Player
from src.game import *

class TestGame(unittest.TestCase):

    def setUp(self):
        self.rob_roberts = Player("Rob", "rock")
        self.peter_peters = Player("Peter", "paper")
        self.sid_sydney = Player("Sid", "scissors")
        self.engelbert_humperdinck = Player("Engelbert Humperdinck", "rock")

    def test_rock_beats_scissors(self):
        result = get_winner(self.rob_roberts, self.sid_sydney)
        self.assertEqual(self.rob_roberts, result)


    def test_scissors_loses_to_rock(self):
        result = get_winner(self.sid_sydney, self.rob_roberts)
        self.assertEqual(self.rob_roberts, result)


    def test_scissors_beats_paper(self):
        result = get_winner(self.sid_sydney, self.peter_peters)
        self.assertEqual(self.sid_sydney, result)


    def test_paper_loses_to_scissors(self):
        result = get_winner(self.peter_peters, self.sid_sydney)
        self.assertEqual(self.sid_sydney, result)


    def test_paper_beats_rock(self):
        result = get_winner(self.peter_peters, self.rob_roberts)
        self.assertEqual(self.peter_peters, result)

    def test_rock_loses_to_paper(self):
        result = get_winner(self.rob_roberts, self.peter_peters)
        self.assertEqual(self.peter_peters, result)

    def test_draw_returns_none(self):
        result = get_winner(self.rob_roberts, self.engelbert_humperdinck)
        self.assertEqual(None, result)