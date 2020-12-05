import unittest
from app.models.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("player_1", "rock")

    def test_player_has_name(self):
        self.assertEqual("player_1", self.player.name)

    def test_player_has_choice(self):
        self.assertEqual("rock", self.player.choice)