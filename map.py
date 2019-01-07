# Vincent Wong
# A01051004

import random


class Map:
    def __init__(self, difficulty: str="easy", player_grid: list = None, map_grid: list = None) -> None:
        """initialize constructor,

        PARAM: difficulty is a string easy, medium, or hard. By default, it is easy
        player_grid is a 2-D list representing the map. By default it is either a 5x5, 7x7, or 10x10 test_grid
        depending on difficulty
        map_grid is a 2-D list representing the map. By default it is either a 5x5, 7x7, or 10x10 test_grid
        depending on difficulty
        PRECONDITION: None
        POST-CONDITION: creates a map for the game
        RETURN: None
        """

        # determine difficulty - hard, medium, easy
        self.difficulty = difficulty.lower().strip()

        # determine size of test_grid
        self.rows = 10 if self.difficulty == "hard" else 7 if self.difficulty == "moderate" else 5
        self.columns = 10 if self.difficulty == "hard" else 7 if self.difficulty == "moderate" else 5

        # create basic test_grid
        self.grid = [["UNKNOWN "] * self.columns for x in range(self.rows)] if map_grid is None else map_grid

        # create the player test_grid
        self.player_grid = [["UNKNOWN "] * self.columns for x in range(self.rows)] if player_grid is None else \
            player_grid

        # contains the location of all items on the board, player always starts at 0, 0
        self.all_locations = [(0, 0)]

        # goal variables
        self.goal = "GOAL"
        # determine the location for the goal
        self.random_row_goal = 0
        self.random_column_goal = 0

        # trap variables
        # number of traps. To be changed depending on difficulty
        self.traps = 0
        self.trap = "TRAP"
        # determine the location of traps
        self.trap_locations = []

        # chest variables
        # number of chests. To be changed depending on difficulty
        self.chests = 0
        self.chest = "CHEST"
        # determine the location of the chests
        self.chest_locations = []
        # what can be found in the chests
        self.chest_inventory = ["Sword", "Mace", "Rubber Duck of Justice", "Potion", "Potion", "Sword", "Mace", "Mace"]

    def set_goal_location(self) -> None:
        """Calculate the coordinate for the goal,

        PARAM: None
        PRECONDITION: Map must be initialized
        POST-CONDITION: Modifies random_row_goal and random_column_goal
        RETURN: None

        >>> test_grid = Map()
        >>> random.seed(1)
        >>> test_grid.set_goal_location()
        >>> print(test_grid.random_column_goal)
        4
        >>> print(test_grid.random_row_goal)
        1
        >>> test_grid.set_goal_location()
        >>> print(test_grid.random_column_goal)
        2
        >>> print(test_grid.random_row_goal)
        0
        """

        self.random_row_goal = random.randint(0, self.rows - 1)
        self.random_column_goal = random.randint(0, self.columns - 1)

    def add_goal(self) -> None:
        """Adds a goal to the map,

        PARAM: No parameter
        PRECONDITION: Map must be initialized
        POST-CONDITION: Modifies the randomly generate map cell to the goal symbol, append coordinate to the list
        all_locations
        RETURN: None

        >>> test_grid = Map()
        >>> random.seed(1)
        >>> test_grid.set_goal_location()
        >>> print(test_grid.random_column_goal)
        4
        >>> print(test_grid.random_row_goal)
        1
        >>> test_grid.add_goal()
        >>> print(test_grid.grid[1][4])
        GOAL
        >>> print(test_grid.all_locations)
        [(0, 0), (4, 1)]
        """

        self.grid[self.random_row_goal][self.random_column_goal] = self.goal
        self.all_locations.append((self.random_column_goal, self.random_row_goal))

    def number_of_traps_chests(self) -> None:
        """calculate the number of traps and chests based on the difficulty of the test_grid,

        PARAM: None
        PRECONDITION: Map must be initialized
        POST-CONDITION: Calculate the number of traps and chests based on the difficulty setting
        RETURN: None

        >>> test_grid = Map('easy')
        >>> test_grid.number_of_traps_chests()
        >>> print(test_grid.traps)
        1
        >>> print(test_grid.chests)
        2
        >>> test_grid = Map('moderate')
        >>> test_grid.number_of_traps_chests()
        >>> print(test_grid.traps)
        5
        >>> print(test_grid.chests)
        2
        >>> test_grid = Map('hard')
        >>> test_grid.number_of_traps_chests()
        >>> print(test_grid.traps)
        20
        >>> print(test_grid.chests)
        2
        """
        if self.difficulty.lower().strip() == "hard" or self.difficulty.lower().strip() == "h":
            self.traps = round((self.rows * self.columns) * 0.2)
            self.chests = round((self.rows * self.columns) * 0.025)

        elif self.difficulty.lower().strip() == "moderate" or self.difficulty.lower().strip() == "m":
            self.traps = round((self.rows * self.columns) * 0.1)
            self.chests = round((self.rows * self.columns) * 0.05)
        else:
            self.traps = round((self.rows * self.columns) * 0.05)
            self.chests = round((self.rows * self.columns) * 0.1)

    def determine_trap_location(self) -> None:
        """find the coordinates for all the traps,

        PARAM: None
        PRECONDITION: Number of traps must be determined
        POST-CONDITION: Randomly generate a coordinate for every trap and append the location to all_locations and
        trap_locations list
        RETURN: None

        >>> test_grid = Map('easy')
        >>> random.seed(1)
        >>> test_grid.number_of_traps_chests()
        >>> test_grid.determine_trap_location()
        >>> print(test_grid.trap_locations)
        [(1, 4)]
        >>> print(test_grid.all_locations)
        [(0, 0), (1, 4)]
        >>> test_grid = Map('moderate')
        >>> test_grid.number_of_traps_chests()
        >>> test_grid.determine_trap_location()
        >>> print(test_grid.trap_locations)
        [(6, 6), (6, 0), (2, 0), (3, 6), (3, 3)]
        >>> print(test_grid.all_locations)
        [(0, 0), (6, 6), (6, 0), (2, 0), (3, 6), (3, 3)]
        >>> test_grid = Map('hard')
        >>> test_grid.number_of_traps_chests()
        >>> test_grid.determine_trap_location()
        >>> print(test_grid.trap_locations)
        [(6, 3), (1, 7), (0, 6), (6, 9), (0, 7), (4, 3), (9, 1), (5, 0), (8, 0), (6, 0), (8, 3), (7, 7), (5, 3)\
, (3, 7), (4, 0), (6, 8), (1, 2), (4, 1), (5, 8), (3, 4)]
        >>> print(test_grid.all_locations)
        [(0, 0), (6, 3), (1, 7), (0, 6), (6, 9), (0, 7), (4, 3), (9, 1), (5, 0), (8, 0), (6, 0), (8, 3), (7, 7), (5, 3)\
, (3, 7), (4, 0), (6, 8), (1, 2), (4, 1), (5, 8), (3, 4)]
        """

        # counter based on the number of traps calculated
        counter = self.traps
        while counter != 0:
            x_coor = random.randint(0, self.columns - 1)
            y_coor = random.randint(0, self.columns - 1)
            # check if there is currently an item on the test_grid in that randomly generated location
            # if there is then restart the loop
            if (x_coor, y_coor) in self.all_locations:
                continue
            else:
                # else decrement the counter and add it to the list of trap locations
                self.all_locations.append((x_coor, y_coor))
                self.trap_locations.append((x_coor, y_coor))
                counter -= 1

    def add_traps(self) -> None:
        """add the traps to the test_grid using the random coordinates generated with determine_trap_location,

        PARAM: None
        PRECONDITION: trap locations must be determined
        POST-CONDITION: for each trap location, place a trap on that corresponding map location
        RETURN: None

        >>> test_grid = Map()
        >>> random.seed(1)
        >>> test_grid.number_of_traps_chests()
        >>> test_grid.determine_trap_location()
        >>> print(test_grid.trap_locations)
        [(1, 4)]
        >>> test_grid.add_traps()
        >>> print(test_grid.grid[4][1])
        TRAP
        """

        for coordinate in self.trap_locations:
            self.grid[coordinate[1]][coordinate[0]] = self.trap

    def determine_chest_location(self) -> None:
        """find the coordinates for all the chests,

        PARAM: None
        PRECONDITION: Number of chests must be determined
        POST-CONDITION: Randomly generate a coordinate for every chest and append the location to all_locations and
        chest_locations
        RETURN: None

        >>> test_grid = Map('easy')
        >>> random.seed(1)
        >>> test_grid.number_of_traps_chests()
        >>> test_grid.determine_chest_location()
        >>> print(test_grid.chest_locations)
        [(1, 4), (0, 2)]
        >>> print(test_grid.all_locations)
        [(0, 0), (1, 4), (0, 2)]

        >>> test_grid = Map('moderate')
        >>> test_grid.number_of_traps_chests()
        >>> test_grid.determine_chest_location()
        >>> print(test_grid.chest_locations)
        [(0, 3), (6, 3)]
        >>> print(test_grid.all_locations)
        [(0, 0), (0, 3), (6, 3)]

        >>> test_grid = Map('hard')
        >>> test_grid.number_of_traps_chests()
        >>> test_grid.determine_chest_location()
        >>> print(test_grid.chest_locations)
        [(7, 6), (3, 1)]
        >>> print(test_grid.chest_locations)
        [(7, 6), (3, 1)]
        """

        # counter based on the number of chests calculated
        counter = self.chests
        while counter != 0:
            x_coor = random.randint(0, self.columns - 1)
            y_coor = random.randint(0, self.columns - 1)
            # check if there is currently an item on the test_grid in that randomly generated location
            # if there is then restart the loop
            if (x_coor, y_coor) in self.all_locations:
                continue
            else:
                # else decrement the counter and add it to the list of trap locations
                self.all_locations.append((x_coor, y_coor))
                self.chest_locations.append((x_coor, y_coor))
                counter -= 1

    def add_chests(self) -> None:
        """add the chests to the test_grid using the random coordinates generated with determine_chest_location,

        PARAM: None
        PRECONDITION: chest locations must be determined
        POST-CONDITION: for each chest location, place a trap on that corresponding map location
        RETURN: None

        >>> test_grid = Map('easy')
        >>> random.seed(1)
        >>> test_grid.number_of_traps_chests()
        >>> test_grid.determine_chest_location()
        >>> print(test_grid.chest_locations)
        [(1, 4), (0, 2)]
        >>> test_grid.add_chests()
        >>> print(test_grid.grid[4][1])
        CHEST
        >>> print(test_grid.grid[2][0])
        CHEST

        >>> test_grid = Map('moderate')
        >>> test_grid.number_of_traps_chests()
        >>> test_grid.determine_chest_location()
        >>> print(test_grid.chest_locations)
        [(0, 3), (6, 3)]
        >>> test_grid.add_chests()
        >>> print(test_grid.grid[3][0])
        CHEST
        >>> print(test_grid.grid[3][6])
        CHEST

        >>> test_grid = Map('hard')
        >>> test_grid.number_of_traps_chests()
        >>> test_grid.determine_chest_location()
        >>> print(test_grid.chest_locations)
        [(7, 6), (3, 1)]
        >>> test_grid.add_chests()
        >>> print(test_grid.grid[6][7])
        CHEST
        >>> print(test_grid.grid[1][3])
        CHEST
        """

        for coordinate in self.chest_locations:
            self.grid[coordinate[1]][coordinate[0]] = self.chest

    def display_player_grid(self) -> None:
        """display the current grid for the user,

        PARAM: None
        PRECONDITION: Map must be instantiated
        POST-CONDITION: None
        RETURN: None

        >>> test_grid = Map('easy')
        >>> test_grid.display_player_grid()
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']

        >>> test_grid = Map('moderate')
        >>> test_grid.display_player_grid()
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']

        >>> test_grid = Map('hard')
        >>> test_grid.display_player_grid()
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', \
'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', \
'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', \
'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', \
'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', \
'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', \
'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', \
'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', \
'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', \
'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', \
'UNKNOWN ']
        """

        for row in self.player_grid:
            print(row)

    def display_grid(self):
        for row in self.grid:
            print(row)

    def add_travelled_to_grid(self, row: int, column: int) -> None:
        """Add the Previous symbol to the grid,

        PARAM: row and column must be an integer within the bounds of the map
        PRECONDITION: row and column must be an integer within the bounds of the map
        POST-CONDITION: Adds a 'PREVIOUS' symbol to the grid with the corresponding row and column coordinate
        RETURN: None

        >>> test_grid = Map('easy')
        >>> test_grid.add_travelled_to_grid(0, 0)
        >>> test_grid.display_player_grid()
        ['PREVIOUS', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        >>> test_grid.add_travelled_to_grid(1, 1)
        >>> test_grid.display_player_grid()
        ['PREVIOUS', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'PREVIOUS', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        """
        travel = 'PREVIOUS'
        self.player_grid[row][column] = travel

    def add_player_to_grid(self, row: int, column: int) -> None:
        """Add the Player symbol to the grid,

        PARAM: row and column must be an integer within the bounds of the map
        PRECONDITION: row and column must be an integer within the bounds of the map
        POST-CONDITION: Adds a 'PLAYER' symbol to the grid with the corresponding row and column coordinate
        RETURN: None

        >>> test_grid = Map('easy')
        >>> test_grid.add_player_to_grid(0, 0)
        >>> test_grid.display_player_grid()
        [' PLAYER ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']

        >>> test_grid.add_player_to_grid(1, 1)
        >>> test_grid.display_player_grid()
        [' PLAYER ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', ' PLAYER ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']
        """

        player = " PLAYER "
        self.player_grid[row][column] = player

    def get_cell(self, row: int, column: int) -> str:
        """Return the symbol for a specific cell of the test_grid,

        PARAM: row and column must be an integer within the bounds of the map
        PRECONDITION: row and column must be an integer within the bounds of the map
        POST-CONDITION: None
        RETURN: The symbol located at the row and column coordinate of the map

        >>> test_grid = Map('easy')
        >>> random.seed(1)
        >>> test_grid.initiate_grid()
        >>> print(test_grid.grid)
        [['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN '], ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ',\
 'GOAL'], ['TRAP', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN '], ['CHEST', 'UNKNOWN ', 'UNKNOWN ', 'CHEST', 'UNKNOWN\
 '], ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']]
        >>> print(test_grid.get_cell(1, 4))
        GOAL
        >>> print(test_grid.get_cell(2, 0))
        TRAP
        """

        return self.grid[row][column]

    def get_chest_item(self) -> str:
        """Returns a chest item at random and removes that item from the list,

        PARAM: None
        PRECONDITION: None
        POST-CONDITION: returned item is removed from the chest_inventory
        RETURN: random item from the chest_inventory list

        >>> test_grid = Map('easy')
        >>> random.seed(1)
        >>> print(test_grid.get_chest_item())
        Rubber Duck of Justice
        >>> print(test_grid.get_chest_item())
        Sword
        >>> print(test_grid.get_chest_item())
        Sword
        >>> print(test_grid.get_chest_item())
        Potion
        >>> print(test_grid.get_chest_item())
        Mace
        >>> print(test_grid.get_chest_item())
        Mace
        >>> print(test_grid.get_chest_item())
        Mace
        >>> print(test_grid.get_chest_item())
        Potion
        >>> print(test_grid.get_chest_item())
        There are no more chest items
        Nothing
        """

        length = len(self.chest_inventory)

        if length == 0:
            print("There are no more chest items")
            return "Nothing"
        return self.chest_inventory.pop(random.randint(0, length - 1))

    def initiate_grid(self):
        """creates the test_grid and adds the goal, traps, and chests,

        PARAM: None
        PRECONDITION: no errors in the Map class methods
        POST-CONDITION: Creates a map during initialization. Find trap and chest locations and place them on the map
        RETURN: None

        >>> test_grid = Map('easy')
        >>> random.seed(1)
        >>> print(test_grid.grid)
        [['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN '], ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ',\
 'UNKNOWN '], ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN '], ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKN\
OWN ', 'UNKNOWN '], ['UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ', 'UNKNOWN ']]
        """

        self.set_goal_location()  # determine the location of the goal
        self.add_goal()  # adds the goal to the grid
        self.number_of_traps_chests()  # determine the number of traps
        self.determine_trap_location()  # determine the location of the traps
        self.determine_chest_location()  # determine the location of the chests
        self.add_traps()  # add traps to the map
        self.add_chests()  # add chests to the map
