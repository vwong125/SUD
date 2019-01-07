import character
import game_info
import io
import random
from unittest import TestCase
from unittest.mock import patch


class TestGame(TestCase):

    def setUp(self):
        self.player = character.Player('name')
        self.game_obj = game_info.Game(self.player)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_health(self, mock_output):
        expected = '10\n'
        self.game_obj.display_health()
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_health_modified(self, mock_output):
        # modify health
        self.player.modify_health(-5)

        expected = '5\n'
        self.game_obj.display_health()
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_inventory(self, mock_output):
        expected = "Your current inventory includes:\n\n"
        self.game_obj.display_inventory()
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_inventory_with_items(self, mock_output):
        self.player.add_inventory('Sword')
        self.player.add_inventory('Mace')
        self.game_obj.display_inventory()
        expected = 'Your current inventory includes:\nSword | Mace\n'
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_coordinates(self, mock_output):
        expected = 'Y coordinate:  1\nX coordinate:  1\n'
        self.game_obj.display_coordinates()
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_coordinates_moved(self, mock_output):
        random.seed(1)
        # move character
        self.player.move_south()
        self.player.move_east()

        # the direction text is a by-product of the moving function
        expected = 'Heading South\nWe must not lose time, we head East\nY coordinate:  2\nX coordinate:  2\n'
        self.game_obj.display_coordinates()
        self.assertEqual(expected, mock_output.getvalue())
