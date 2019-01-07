import map
import random
from unittest import TestCase


class TestMap(TestCase):

    def setUp(self):
        # easy grid
        self.test_grid = map.Map('easy')

        # moderate grid
        self.test_grid_moderate = map.Map('moderate')

        # hard grid
        self.test_grid_hard = map.Map('hard')

    def test_set_goal(self):
        # initial goal placement
        self.assertEqual(self.test_grid.random_row_goal, 0)
        self.assertEqual(self.test_grid.random_column_goal, 0)

        # check if column coordinate is in test_grid boundary
        self.assertGreaterEqual(self.test_grid.random_column_goal, 0)
        self.assertLessEqual(self.test_grid.random_column_goal, self.test_grid.columns)

        # check if row coordinate is in test_grid boundary
        self.assertGreaterEqual(self.test_grid.random_row_goal, 0)
        self.assertLessEqual(self.test_grid.random_row_goal, self.test_grid.rows)

        # randomly generate goal location
        random.seed(1)
        self.test_grid.set_goal_location()
        self.assertEqual(self.test_grid.random_row_goal, 1)
        self.assertEqual(self.test_grid.random_column_goal, 4)

    def test_add_goal(self):
        # set coordinates for the goal
        random.seed(1)
        self.test_grid.set_goal_location()
        self.assertEqual(self.test_grid.random_row_goal, 1)
        self.assertEqual(self.test_grid.random_column_goal, 4)

        # add the goal to the map based on the randomly generated coordinate
        self.test_grid.add_goal()
        expected = 'GOAL'
        actual = self.test_grid.grid[1][4]
        self.assertEqual(expected, actual)

    def test_number_of_traps_chests_easy(self):
        # this function finds the number of chests and traps because they are both dependent on difficulty
        # easy grid traps
        self.test_grid.number_of_traps_chests()
        expected_traps = 1
        actual_traps = self.test_grid.traps
        self.assertEqual(expected_traps, actual_traps)

        # easy grid chests
        expected_chests = 2
        actual_chests = self.test_grid.chests
        self.assertEqual(expected_chests, actual_chests)

    def test_number_of_traps_chests_moderate(self):
        # this function finds the number of chests and traps because they are both dependent on difficulty
        # moderate grid traps
        self.test_grid_moderate.number_of_traps_chests()
        expected_traps = 5
        actual_traps = self.test_grid_moderate.traps
        self.assertEqual(expected_traps, actual_traps)

        # moderate grid chests
        expected_chests = 2
        actual_chests = self.test_grid_moderate.chests
        self.assertEqual(expected_chests, actual_chests)

    def test_number_of_traps_chests_hard(self):
        # this function finds the number of chests and traps because they are both dependent on difficulty
        # moderate grid traps
        self.test_grid_hard.number_of_traps_chests()
        expected_traps = 20
        actual_traps = self.test_grid_hard.traps
        self.assertEqual(expected_traps, actual_traps)

        # moderate grid chests
        expected_chests = 2
        actual_chests = self.test_grid_hard.chests
        self.assertEqual(expected_chests, actual_chests)

    def test_determine_trap_location_easy(self):
        random.seed(1)
        # determine the number of traps
        self.test_grid.number_of_traps_chests()

        # number of locations before determining locations
        self.assertEqual([], self.test_grid.trap_locations)

        # number of locations after determining location
        self.test_grid.determine_trap_location()
        expected = [(1, 4)]
        actual = self.test_grid.trap_locations
        self.assertEqual(expected, actual)

        # check correct number of coordinates
        self.assertEqual(len(actual), 1)

    def test_determine_trap_location_moderate(self):
        random.seed(1)
        # determine the number of traps
        self.test_grid_moderate.number_of_traps_chests()

        # number of locations before determining locations
        self.assertEqual([], self.test_grid_moderate.trap_locations)

        # number of locations after determining location
        self.test_grid_moderate.determine_trap_location()
        expected = [(1, 4), (6, 6), (6, 0), (2, 0), (3, 6)]
        actual = self.test_grid_moderate.trap_locations
        self.assertEqual(expected, actual)

        # check correct number of coordinates
        self.assertEqual(len(actual), 5)

    def test_determine_trap_location_hard(self):
        random.seed(1)
        # determine the number of traps
        self.test_grid_hard.number_of_traps_chests()

        # number of locations before determining locations
        self.assertEqual([], self.test_grid_hard.trap_locations)

        # number of locations after determining location
        self.test_grid_hard.determine_trap_location()
        expected = [(2, 9), (1, 4), (1, 7), (7, 7), (6, 3), (0, 6), (6, 9), (0, 7), (4, 3), (9, 1), (5, 0),
                    (8, 0), (6, 0), (8, 3), (5, 3), (3, 7), (4, 0), (6, 8), (1, 2), (4, 1)]
        actual = self.test_grid_hard.trap_locations
        self.assertEqual(expected, actual)

        # check correct number of coordinates
        self.assertEqual(len(actual), 20)

    def test_add_traps_easy(self):
        # set trap numbers
        self.test_grid.number_of_traps_chests()

        # find coordinates
        random.seed(1)
        self.test_grid.determine_trap_location()
        # coordinates are in x, y format; column, row format
        expected = [(1, 4)]
        actual = self.test_grid.trap_locations
        self.assertEqual(expected, actual)

        # check grid
        self.test_grid.add_traps()
        self.assertEqual(self.test_grid.grid[4][1], 'TRAP')

    def test_add_traps_moderate(self):
        # set trap numbers
        self.test_grid_moderate.number_of_traps_chests()

        # find coordinates
        random.seed(1)
        self.test_grid_moderate.determine_trap_location()
        # coordinates are in x, y format; column, row format
        expected = [(1, 4), (6, 6), (6, 0), (2, 0), (3, 6)]
        actual = self.test_grid_moderate.trap_locations
        self.assertEqual(expected, actual)

        # check grid
        self.test_grid_moderate.add_traps()
        self.assertEqual(self.test_grid_moderate.grid[6][6], 'TRAP')
        self.assertEqual(self.test_grid_moderate.grid[0][6], 'TRAP')
        self.assertEqual(self.test_grid_moderate.grid[0][2], 'TRAP')
        self.assertEqual(self.test_grid_moderate.grid[6][3], 'TRAP')

    def test_add_traps_hard(self):
        # set trap numbers
        self.test_grid_hard.number_of_traps_chests()

        # find coordinates
        random.seed(1)
        self.test_grid_hard.determine_trap_location()
        # coordinates are in x, y format; column, row format
        expected = [(2, 9), (1, 4), (1, 7), (7, 7), (6, 3), (0, 6), (6, 9), (0, 7), (4, 3), (9, 1), (5, 0),
                    (8, 0), (6, 0), (8, 3), (5, 3), (3, 7), (4, 0), (6, 8), (1, 2), (4, 1)]
        actual = self.test_grid_hard.trap_locations
        self.assertEqual(expected, actual)

        # check grid
        self.test_grid_hard.add_traps()
        self.assertEqual(self.test_grid_hard.grid[9][2], 'TRAP')
        self.assertEqual(self.test_grid_hard.grid[3][6], 'TRAP')
        self.assertEqual(self.test_grid_hard.grid[1][9], 'TRAP')
        self.assertEqual(self.test_grid_hard.grid[1][4], 'TRAP')
        self.assertEqual(self.test_grid_hard.grid[0][8], 'TRAP')
        self.assertEqual(self.test_grid_hard.grid[3][5], 'TRAP')
        self.assertEqual(self.test_grid_hard.grid[0][4], 'TRAP')
        self.assertEqual(self.test_grid_hard.grid[8][6], 'TRAP')
        self.assertEqual(self.test_grid_hard.grid[2][1], 'TRAP')

    def test_determine_chest_location_easy(self):
        random.seed(1)
        # determine the number of chests
        self.test_grid.number_of_traps_chests()

        # number of locations before determining locations
        self.assertEqual([], self.test_grid.chest_locations)

        # number of locations after determining location
        self.test_grid.determine_chest_location()
        expected = [(1, 4), (0, 2)]
        actual = self.test_grid.chest_locations
        self.assertEqual(expected, actual)

        # check correct number of coordinates
        self.assertEqual(len(actual), 2)

    def test_determine_chest_location_moderate(self):
        random.seed(1)
        # determine the number of chests
        self.test_grid_moderate.number_of_traps_chests()

        # number of locations before determining locations
        self.assertEqual([], self.test_grid_moderate.chest_locations)

        # number of locations after determining location
        self.test_grid_moderate.determine_chest_location()
        expected = [(1, 4), (6, 6)]
        actual = self.test_grid_moderate.chest_locations
        self.assertEqual(expected, actual)

        # check correct number of coordinates
        self.assertEqual(len(actual), 2)

    def test_determine_chest_location_hard(self):
        random.seed(1)
        # determine the number of chests
        self.test_grid_hard.number_of_traps_chests()

        # number of locations before determining locations
        self.assertEqual([], self.test_grid_hard.chest_locations)

        # number of locations after determining location
        self.test_grid_hard.determine_chest_location()
        expected = [(2, 9), (1, 4)]
        actual = self.test_grid_hard.chest_locations
        self.assertEqual(expected, actual)

        # check correct number of coordinates
        self.assertEqual(len(actual), 2)

    def test_add_chests_easy(self):
        # set trap numbers
        self.test_grid.number_of_traps_chests()

        # find coordinates
        # coordinates are in x, y format; column, row format
        random.seed(1)
        self.test_grid.determine_chest_location()
        expected = [(1, 4), (0, 2)]
        actual = self.test_grid.chest_locations
        self.assertEqual(expected, actual)

        # check grid
        self.test_grid.add_chests()
        self.assertEqual(self.test_grid.grid[4][1], 'CHEST')
        self.assertEqual(self.test_grid.grid[2][0], 'CHEST')

    def test_add_chests_moderate(self):
        # set trap numbers
        self.test_grid_moderate.number_of_traps_chests()

        # find coordinates
        # coordinates are in x, y format; column, row format
        random.seed(1)
        self.test_grid_moderate.determine_chest_location()
        expected = [(1, 4), (6, 6)]
        actual = self.test_grid_moderate.chest_locations
        self.assertEqual(expected, actual)

        # check grid
        self.test_grid_moderate.add_chests()
        self.assertEqual(self.test_grid_moderate.grid[4][1], 'CHEST')
        self.assertEqual(self.test_grid_moderate.grid[6][6], 'CHEST')

    def test_add_chests_hard(self):
        # set trap numbers
        self.test_grid_hard.number_of_traps_chests()

        # find coordinates
        # coordinates are in x, y format; column, row format
        random.seed(1)
        self.test_grid_hard.determine_chest_location()
        expected = [(2, 9), (1, 4)]
        actual = self.test_grid_hard.chest_locations
        self.assertEqual(expected, actual)

        # check grid
        self.test_grid_hard.add_chests()
        self.assertEqual(self.test_grid_hard.grid[9][2], 'CHEST')
        self.assertEqual(self.test_grid_hard.grid[4][1], 'CHEST')

    def test_add_player_to_grid(self):
        # check cell initially
        self.assertEqual(self.test_grid.grid[2][2], 'UNKNOWN ')
        # add player to the grid cell
        self.test_grid.add_player_to_grid(2, 2)
        self.assertEqual(self.test_grid.player_grid[2][2], ' PLAYER ')

    def test_get_cell(self):
        self.assertEqual(self.test_grid.get_cell(2, 2), 'UNKNOWN ')

        # add player to grid
        self.test_grid.add_player_to_grid(2, 2)

        # check cell again
        self.test_grid.get_cell(2, 2)

    def test_get_chest_item(self):
        random.seed(1)
        self.assertEqual('Rubber Duck of Justice', self.test_grid.get_chest_item())
        self.assertEqual('Sword', self.test_grid.get_chest_item())
        self.assertEqual('Sword', self.test_grid.get_chest_item())
        self.assertEqual('Potion', self.test_grid.get_chest_item())
