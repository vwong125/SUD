import character
import io
import random
from unittest import TestCase
from unittest.mock import patch


class TestPlayer(TestCase):

    def setUp(self):
        self.player = character.Player('name')

    def test_add_inventory(self):
        self.assertEqual(self.player.inventory, [])
        self.player.add_inventory('Sword')
        self.assertEqual(self.player.inventory, ['Sword'])
        self.player.add_inventory('Mace')
        self.assertEqual(self.player.inventory, ['Sword', 'Mace'])

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_north(self, mock_output):
        random.seed(1)
        self.assertEqual(self.player.row_position, 0)

        self.player.move_north()
        self.assertEqual(self.player.row_position, -1)
        self.assertEqual('Heading North\n', mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_east(self, mock_output):
        random.seed(1)
        self.assertEqual(self.player.column_position, 0)

        self.player.move_east()
        self.assertEqual(self.player.column_position, 1)
        self.assertEqual('Heading East\n', mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_south(self, mock_output):
        random.seed(1)
        self.assertEqual(self.player.row_position, 0)

        self.player.move_south()
        self.assertEqual(self.player.row_position, 1)
        self.assertEqual('Heading South\n', mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_west(self, mock_output):
        random.seed(1)
        self.assertEqual(self.player.column_position, 0)

        self.player.move_west()
        self.assertEqual(self.player.column_position, -1)
        self.assertEqual('Heading West\n', mock_output.getvalue())

    def test_roll_attack_no_modifier(self):
        self.assertGreaterEqual(self.player.roll_attack(), 1)
        self.assertLessEqual(self.player.roll_attack(), 6)

    def test_roll_attack_mace_modifier(self):
        # Mace modifier = + 1 to attack
        self.player.add_inventory('Mace')
        self.assertGreaterEqual(self.player.roll_attack(), 2)
        self.assertLessEqual(self.player.roll_attack(), 7)

    def test_roll_attack_sword_modifier(self):
        # Sword modifier = + 2 to attack
        self.player.add_inventory('Sword')
        self.assertGreaterEqual(self.player.roll_attack(), 3)
        self.assertLessEqual(self.player.roll_attack(), 8)

    def test_roll_attack_duck_modifier(self):
        # Rubber Duck of Justice Modifier = times 2 to attack
        self.player.add_inventory('Rubber Duck of Justice')
        self.assertGreaterEqual(self.player.roll_attack(), 2)
        self.assertLessEqual(self.player.roll_attack(), 12)

    def test_modify_health(self):
        # initial hp = 10
        self.assertEqual(self.player.hp, 10)

        # decrease health during combat
        self.player.modify_health(-5)
        self.assertEqual(self.player.hp, 5)

        # increase health during movement or using a potion
        self.player.modify_health(3)
        self.assertEqual(self.player.hp, 8)

        # max hp is 10
        self.player.modify_health(100000000)
        self.assertEqual(self.player.hp, 10)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_potion_no_potion(self, mock_output):
        expected_output = "You do not have a potion in your inventory\n"
        self.player.use_potion()
        self.assertEqual(expected_output, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_potion(self, mock_output):
        self.player.modify_health(-5)
        expected_output = "You used a potion! Your health is now at 8\n"
        self.player.add_inventory('Potion')
        self.player.use_potion()
        self.assertEqual(expected_output, mock_output.getvalue())
