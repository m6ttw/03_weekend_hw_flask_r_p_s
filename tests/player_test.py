import unittest
from src.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Player", "Rock")

    def test_player_has_name(self):
        self.assertEqual("Player", self.player.name)

    def test_player_has_choice(self):
        self.assertEqual("Rock", self.player.choice)