# Vincent Wong
# A01051004

import doctest
import character


class Game:

    def __init__(self, player):
        self.player = player

    def display_map_commands(self) -> None:
        """Display possible MAP commands for the user,

        PARAM: None
        PRECONDITION: None
        POST-CONDITION: None
        RETURN: None

        >>> player = character.Player("Name")
        >>> game = Game(player)
        >>> game.display_battle_commands()
        ***** Can only be used during combat (BATTLE commands) *****
        'attack' - Initiate combat
        'flee' - attempt to run away from the enemy
        'hp' - Display your hp
        'monster hp' - Display the monster's hp
        'potion' - Use a potion if available. Potions heal 3 HP, but your max health cannot be over 10
        **************************************************
        <BLANKLINE>
        """

        print("*" * 5, "Can only be used when wandering the dungeon (MAP commands)", "*" * 5)
        print("'help' - displays all possible inputs\n"
              "'north' or 'w' - moves the character North one space\n"
              "'east' or 'd' - moves the character East one space\n"
              "'south' or 's' - moves the character South one space\n"
              "'west' or 'a' - moves the character West one space\n"
              "'map' - displays the current map. 'PLAYER' indicates where you have been and currently located\n"
              "'inventory' - display your inventory\n"
              "'quit' - save your character profile and leave the game\n"
              "'hp' - Display your hp\n"
              "'coor' - Display your current coordinates\n"
              "'potion' - Use a potion if available. Potions heal 3 HP, but your max health cannot be over 10\n"
              "'save' - Save the game\n")
        print("*" * 50 + "\n")

    def display_battle_commands(self) -> None:
        """Display possible BATTLE commands for the user,

        PARAM: None
        PRECONDITION: None
        POST-CONDITION: None
        RETURN: None

        >>> player = character.Player("Name")
        >>> game = Game(player)
        >>> game.display_battle_commands()
        ***** Can only be used during combat (BATTLE commands) *****
        'attack' - Initiate combat
        'flee' - attempt to run away from the enemy
        'hp' - Display your hp
        'monster hp' - Display the monster's hp
        'potion' - Use a potion if available. Potions heal 3 HP, but your max health cannot be over 10
        **************************************************
        <BLANKLINE>
        """

        print("*" * 5, "Can only be used during combat (BATTLE commands)", "*" * 5)
        print("'attack' - Initiate combat\n"
              "'flee' - attempt to run away from the enemy\n"
              "'hp' - Display your hp\n"
              "'monster hp' - Display the monster's hp\n"
              "'potion' - Use a potion if available. Potions heal 3 HP, but your max health cannot be over 10")
        print("*" * 50 + "\n")

        # display functions

    def display_health(self) -> None:
        """Display the health of the user,

        PARAM: None
        PRECONDITION: player object must be initialized
        POST-CONDITION: None
        RETURN: None

        >>> player = character.Player("Name")
        >>> game = Game(player)
        >>> game.display_health()
        10
        >>> player.modify_health(-2)
        >>> game.display_health()
        8
        >>> player.modify_health(200)
        >>> game.display_health()  # max hp is capped at 10
        10
        """

        print(self.player.hp)

    def display_inventory(self) -> None:
        """Display the player's current inventory,

        PARAM: None
        PRECONDITION: player object must be initialized
        POST-CONDITION: None
        RETURN: None

        >>> player = character.Player("Name")
        >>> game = Game(player)
        >>> game.display_inventory()
        Your current inventory includes:
        <BLANKLINE>
        """

        print("Your current inventory includes:\n" + " | ".join(self.player.inventory))

    def display_coordinates(self) -> None:
        """Display the player's current coordinate on the map,

        PARAM: None
        PRECONDITION: player object must be initialized
        POST-CONDITION: None
        RETURN: None

        >>> player = character.Player("Name")
        >>> game = Game(player)
        >>> game.display_coordinates()
        Y coordinate:  1
        X coordinate:  1
        """

        print('Y coordinate: ', self.player.row_position + 1)
        print('X coordinate: ', self.player.column_position + 1)


if __name__ == "__main__":
    doctest.testmod()
