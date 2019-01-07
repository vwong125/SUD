from unittest import TestCase
from unittest.mock import patch

import combat
import character
import monster
import game_info
import random

random.seed(1)


class TestBattle(TestCase):

    def setUp(self):
        self.player = character.Player('name')
        self.demon = monster.Monster()
        self.game_obj = game_info.Game(self.player)
        self.battle = combat.Battle(player_obj=self.player, monster_obj=self.demon, game_obj=self.game_obj)

    @patch('builtins.input', side_effect=['attack', 'attack', 'attack', 'attack', 'attack'])
    def test_combat(self, mock_input):
        random.seed(1)
        self.assertIsNone(self.battle.combat())

    @patch('builtins.input', side_effect=['flee', 'flee', 'flee', 'flee'])
    def test_combat_flee(self, mock_input):
        random.seed(1)
        self.assertIsNone(self.battle.combat())



