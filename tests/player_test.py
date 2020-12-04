import unittest
from src.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Player_1", "Rock")

    def test_player_1_has_name(self):
        self.assertEqual("Player_1", self.player_1.name)

    def test_player_1_has_choice(self):
        self.assertEqual("Rock", self.player_1.choice)