# Vincent Wong
# A01051004

import random


class Player:

    def __init__(self, name: str, hp: int = 10, inventory: list = (), column_position: int = 0, row_position: int = 0):
        """initiate the player constructor,
        PARAM:
        name is a string,
        hp is an integer and by default is 10,
        inventory is a list and by default is a tuple,
        column position is an int, but 0 by default,
        row position is an int, but 0 by default

        PRECONDITION: Name is a string and must be specified for the creation of this object
        POST-CONDITION: creates class variables for the player object
        RETURN: None
        """

        self.name = name
        self.hp = hp
        self.inventory = list(inventory)
        self.column_position = column_position
        self.row_position = row_position
        self.move_phrases = ["You travelled ", "Heading ", "Onwards! to the ", "We must not lose time, we head "]
        self.number_of_phrases = len(self.move_phrases)

    def add_inventory(self, item: str) -> None:
        """Adds a specific item to the player's inventory,

        PARAM: Item is a string
        PRECONDITION: player object must be created and have an inventory
        POST-CONDITION: player
        RETURN: None

        >>> player = Player('name')
        >>> player.add_inventory('Potion')
        >>> print(player.inventory)
        ['Potion']
        >>> player.add_inventory('Sword')
        >>> print(player.inventory)
        ['Potion', 'Sword']
        """
        self.inventory.append(item)

    # movement functions
    def move_north(self) -> None:
        """moves the character North one space,

        PARAM: None
        PRECONDITION: player must have a y-coordinate or row position
        POST-CONDITION: the y-coordinate or row position is decreased by 1
        RETURN: None

        >>> player = Player('name')
        >>> print(player.row_position)
        0
        >>> random.seed(1)
        >>> player.move_north()
        Heading North
        >>> print(player.row_position)
        -1
        """

        self.row_position -= 1
        print(self.move_phrases[random.randint(1, self.number_of_phrases - 1)] + "North")

    def move_east(self) -> None:
        """moves the character East one space,

        PARAM: None
        PRECONDITION: player must have a x-coordinate or column position
        POST-CONDITION: the x-coordinate or column position is increased by 1
        RETURN: None

        >>> player = Player('name')
        >>> print(player.column_position)
        0
        >>> random.seed(1)
        >>> player.move_east()
        Heading East
        >>> print(player.column_position)
        1
        """

        self.column_position += 1
        print(self.move_phrases[random.randint(1, self.number_of_phrases - 1)] + "East")

    def move_south(self) -> None:
        """moves the character South one space,

        PARAM: None
        PRECONDITION: player must have a y-coordinate or row position
        POST-CONDITION: the y-coordinate or row position is increased by 1
        RETURN: None

        >>> player = Player('name')
        >>> print(player.row_position)
        0
        >>> random.seed(1)
        >>> player.move_south()
        Heading South
        >>> print(player.row_position)
        1
        """

        self.row_position += 1
        print(self.move_phrases[random.randint(1, self.number_of_phrases - 1)] + "South")

    def move_west(self) -> None:
        """moves the character West one space,

        PARAM: None
        PRECONDITION: player must have a x-coordinate or column position
        POST-CONDITION: the x-coordinate or column position is decreased by 1
        RETURN: None

        >>> player = Player('name')
        >>> print(player.column_position)
        0
        >>> random.seed(1)
        >>> player.move_west()
        Heading West
        >>> print(player.column_position)
        -1
        """

        self.column_position -= 1
        print(self.move_phrases[random.randint(1, self.number_of_phrases - 1)] + "West")

    # combat functions
    def roll_attack(self) -> int:
        """Rolls a d6 dice to indicate the player's attack and returns the value. If the player has a weapon
        in his inventory, modify the attack before returning,

        PARAM: None
        PRECONDITION: random module must be imported
        POST-CONDITION: None
        RETURN: Returns a random integer from 1 to 6 and modifies it based on equipment the player has

        >>> player = Player('name')
        >>> random.seed(1)
        >>> player.roll_attack()
        2
        >>> player.add_inventory('Mace')
        >>> player.roll_attack()  # this roll is usually 5
        6
        >>> player.add_inventory('Sword')
        >>> player.roll_attack()  # this roll is suppose to be 1
        3
        >>> player.add_inventory('Rubber Duck of Justice')
        >>> player.roll_attack()  # suppose to be 3
        6
        """

        attack = random.randint(1, 6)
        if "Rubber Duck of Justice" in self.inventory:
            attack *= 2
        elif "Sword" in self.inventory:
            attack += 2
        elif "Mace" in self.inventory:
            attack += 1
        else:
            attack += 0
        return attack

    def modify_health(self, number: int) -> None:
        """Modify the health of the player. Maximum health for the player is 10 hp,

        PARAM: Number is an integer
        PRECONDITION: player must have a health variable, number must be an integer
        POST-CONDITION: the player's health is modified to the sum of the health and number
        RETURN: None

        >>> player = Player('name')
        >>> print(player.hp)
        10
        >>> player.modify_health(-4)
        >>> print(player.hp)
        6
        >>> player.modify_health(2)
        >>> print(player.hp)
        8
        >>> player.modify_health(200)  # max hp is capped at 10
        >>> print(player.hp)
        10
        """

        # if need to subtract hp, must multiply number by * -1
        self.hp += number
        # check if hp is over 10, if so, alter the hp
        if self.hp > 10:
            self.hp = 10

    def use_potion(self) -> None:
        """Use a potion if the player has it in his inventory

        PARAM: None
        PRECONDITION: player must have an inventory
        POST-CONDITION: removes the potion from the player's inventory if used
        RETURN: None

        >>> player = Player('name')
        >>> player.modify_health(-5)
        >>> print(player.hp)
        5
        >>> player.use_potion()
        You do not have a potion in your inventory
        >>> player.add_inventory('Potion')
        >>> player.use_potion()
        You used a potion! Your health is now at 8
        >>> player.add_inventory('Potion')
        >>> player.use_potion()
        You used a potion! Your health is now at 10
        """

        if "Potion" in self.inventory:
            self.inventory.remove("Potion")
            self.modify_health(3)
            print("You used a potion! Your health is now at %d" % self.hp)
        else:
            print("You do not have a potion in your inventory")
