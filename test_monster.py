import io
import monster
import random
from unittest import TestCase
from unittest.mock import patch


class TestMonster(TestCase):
    def setUp(self):
        self.demon = monster.Monster()

    def test_roll_attack(self):
        self.assertGreaterEqual(self.demon.roll_attack(), 1)
        self.assertLessEqual(self.demon.roll_attack(), 6)

        random.seed(1)
        self.assertEqual(2, self.demon.roll_attack())

    def test_roll_flee_attack(self):
        # used for when the player is fleeing
        self.assertGreaterEqual(self.demon.roll_attack(), 1)
        self.assertLessEqual(self.demon.roll_attack(), 4)

        random.seed(1)
        self.assertEqual(2, self.demon.roll_attack())

    def test_modify_health(self):
        # used to decrease the monster's health
        self.assertEqual(self.demon.hp, 8)
        self.demon.modify_health(-4)
        self.assertEqual(self.demon.hp, 4)

        # Note,if a positive parameter is positive, monster hp will increase and there is no max hp set for monster
        # However, for the sake of this game, the parameter will always be negative in the combat function
        # Can be used if we want to upgrade the game to allow monsters to heal for extra difficulty

        self.demon.modify_health(996)
        self.assertEqual(self.demon.hp, 1000)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_health(self, mock_output):
        expected_output = '8\n'
        self.demon.display_health()
        self.assertEqual(expected_output, mock_output.getvalue())
