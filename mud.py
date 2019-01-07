# Vincent Wong
# A01051004

# import modules
import json
import random
import sys
import time

# import files
import character
import combat
import game_info
import map
import monster


def main():
    """executes the program"""
    # doctest.testmod()
    print("Nephalem....")
    time.sleep(0.5)

    # check if user has a saved file or not
    returning_user = input("Have you been here before? y/N\n").lower().strip()

    # load character profile
    if returning_user == "y":
        file_name = "character_info.json"

        try:
            with open(file_name, 'r') as file:
                char_profile = json.load(file)
        except FileNotFoundError:
            print("File not found")
            sys.exit()

        # initialize player object with information stored in json file
        player = character.Player(char_profile['name'], char_profile['hp'], char_profile['inventory'],
                                  char_profile['column_position'], char_profile['row_position'])

        # initialize map object using difficulty stored in json file
        dungeon_map = map.Map(char_profile['difficulty'], char_profile['player_grid'], char_profile['map_grid'])

        # initialize game_information object using player object
        game_information = game_info.Game(player)

        print("Welcome back {}".format(player.name))

    # ask user for information to create a new player
    else:
        user_name = input("What is your name?\n").title()
        player = character.Player(user_name)

        game_information = game_info.Game(player)

        print("How much faith do you put in your strength?")
        difficulty = input("Enter 'Hard', 'Moderate', or 'Easy'\n")

        # create map object using difficulty that player chose, default is easy
        dungeon_map = map.Map(difficulty)

        # create the map, add goal, chests, traps
        dungeon_map.initiate_grid()

        # add the PLAYER marker on the map to indicate starting position
        dungeon_map.add_player_to_grid(player.row_position, player.column_position)

        # starting scenario
        print("{}, welcome to the dungeon ruled by the 7 evils of Hell: Diablo, Baal, Mephisto, Andariel, Duriel\n"
              "Belial, Azmodan, and Lilith. You are the last hope in saving this world. Traverse this dungeon\n"
              "and reach the black soul stone so you can seal the 7 evils. Be careful as they are lurking\n"
              "in these walls... it does not matter if you fight or flee from these battles, but if you perish\n"
              "so does the world. Good luck on your adventure\n".format(player.name))

    # CONSTANTS
    ending_message = "Congratulations! You have found the black soul stone and have sealed away all\n" \
                     "7 evils. The world thanks you for your bravery and courage"

    game_over_message = "It seems that the strength of the 7 evils were too strong even for you.... I respect\n" \
                        "your efforts, but it is time to sleep....your game is over..."

    # sentinel
    gatekeeper = True

    # initialize game loop
    while gatekeeper:
        time.sleep(0.25)
        # check if user has died. If so, end game loop
        if player.hp <= 0:
            gatekeeper = False
            print(game_over_message)

        # main loop
        else:
            user_input = input("Enter a MAP command. Enter 'help' for the command list\n").lower().strip()

            # Chance for monster to appear. Rolled every iteration of the loop
            monster_chance = random.randint(0, 10)

            # check for events

            if user_input == 'help':
                game_information.display_map_commands()

            elif user_input == 'grid':
                dungeon_map.display_grid()

            # save character profile
            elif user_input == 'save':
                character_profile = {
                    'name': player.name,
                    'hp': player.hp,
                    'inventory': player.inventory,
                    'column_position': player.column_position,
                    'row_position': player.row_position,
                    'difficulty': dungeon_map.difficulty,
                    'player_grid': dungeon_map.player_grid,
                    'map_grid': dungeon_map.grid,
                }

                file_name = "character_info.json"
                with open(file_name, 'w') as file:
                    json.dump(character_profile, file)

                print("Your file has been successfully saved")

            # display events

            elif user_input == 'coor':
                game_information.display_coordinates()

            elif user_input == 'map':
                dungeon_map.display_player_grid()

            elif user_input == 'hp':
                game_information.display_health()

            elif user_input == 'inventory':
                game_information.display_inventory()

            elif user_input == 'potion':
                player.use_potion()

            # quit event
            elif user_input == 'quit':
                choice = input("The wrath of the demons still continue! Are you sure you want to retire? y/N")
                if choice == 'y':
                    print('You will be remembered...')
                    gatekeeper = False

                    character_profile = {
                        'name': player.name,
                        'hp': player.hp,
                        'inventory': player.inventory,
                        'column_position': player.column_position,
                        'row_position': player.row_position,
                        'difficulty': dungeon_map.difficulty,
                        'player_grid': dungeon_map.player_grid,
                        'map_grid': dungeon_map.grid,
                    }

                    file_name = "character_info.json"
                    with open(file_name, 'w') as file:
                        json.dump(character_profile, file)
                else:
                    continue

            # direction events

            elif user_input == 'north' or user_input == 'w':
                # check for out of bounds
                # if out of bounds
                if player.row_position - 1 < 0:
                    print("You've reached the end of the world!")
                # if not out of bounds
                else:
                    # gets the information located at that test_grid and checks it
                    cell = dungeon_map.get_cell(player.row_position - 1, player.column_position)

                    # UNKNOWN means that the cell is unoccupied
                    if cell == 'UNKNOWN ':
                        # check for monster appearance - 20%
                        if monster_chance <= 1:
                            # create a monster object and battle object. Simulate battle
                            demon = monster.Monster()
                            fight = combat.Battle(player, demon, game_information)
                            fight.combat()
                        else:
                            # player health increases by 1
                            player.modify_health(1)
                            # grid updates to show previous location
                            dungeon_map.add_travelled_to_grid(player.row_position, player.column_position)
                            # player moves in specified direction
                            player.move_north()
                            # update the map
                            dungeon_map.add_player_to_grid(player.row_position, player.column_position)

                    # TRAP means that there is a trap at the location. Player takes a d2 roll amount of damage.
                    # Player moves after
                    elif cell == 'TRAP':
                        trap_damage = random.randint(0, 2)
                        player.modify_health(trap_damage * -1)
                        print("You have fallen into a trap! You took {} damage".format(trap_damage))
                        # grid updates to show previous location
                        dungeon_map.add_travelled_to_grid(player.row_position, player.column_position)
                        # player moves in specified direction
                        player.move_north()
                        dungeon_map.add_player_to_grid(player.row_position, player.column_position)

                    # CHEST means that the user encountered a chest.
                    # Player receives content and moves
                    elif cell == "CHEST":
                        player.modify_health(1)
                        item = dungeon_map.get_chest_item()
                        print("You have found a treasure chest! You added {} to your inventory".format(item))
                        player.add_inventory(item)
                        # grid updates to show previous location
                        dungeon_map.add_travelled_to_grid(player.row_position, player.column_position)
                        # player moves in specified direction
                        player.move_north()
                        dungeon_map.add_player_to_grid(player.row_position, player.column_position)

                    # GOAL is the destination for this game
                    # player finishes the game if it is reached
                    elif cell == "GOAL":
                        gatekeeper = False
                        print(ending_message)

            elif user_input == "east" or user_input == 'd':
                # check for out of bounds
                try:
                    cell = dungeon_map.get_cell(player.row_position, player.column_position + 1)

                except IndexError:
                    print("You've been blocked by a structure known as ... walls")

                else:

                    if cell == 'UNKNOWN ':
                        if monster_chance <= 1:
                            demon = monster.Monster()
                            fight = combat.Battle(player, demon, game_information)
                            fight.combat()
                        else:
                            player.modify_health(1)
                            # grid updates to show previous location
                            dungeon_map.add_travelled_to_grid(player.row_position, player.column_position)
                            # player moves in specified direction
                            player.move_east()
                            dungeon_map.add_player_to_grid(player.row_position, player.column_position)

                    elif cell == 'TRAP':
                        trap_damage = random.randint(0, 2)
                        player.modify_health(trap_damage * -1)
                        print("You have fallen into a trap! You took {} damage".format(trap_damage))
                        # grid updates to show previous location
                        dungeon_map.add_travelled_to_grid(player.row_position, player.column_position)
                        # player moves in specified direction
                        player.move_east()
                        dungeon_map.add_player_to_grid(player.row_position, player.column_position)

                    elif cell == "CHEST":
                        player.modify_health(1)
                        item = dungeon_map.get_chest_item()
                        print("You have found a treasure chest! You added {} to your inventory".format(item))
                        player.add_inventory(item)
                        # grid updates to show previous location
                        dungeon_map.add_travelled_to_grid(player.row_position, player.column_position)
                        # player moves in specified direction
                        player.move_east()
                        dungeon_map.add_player_to_grid(player.row_position, player.column_position)

                    elif cell == "GOAL":
                        gatekeeper = False
                        print(ending_message)

            elif user_input == "west" or user_input == "a":
                # check for out of bounds
                if player.column_position - 1 < 0:
                    print("Are you looking for a hidden door....because there isn't one. Move elsewhere")

                else:
                    cell = dungeon_map.get_cell(player.row_position, player.column_position - 1)

                    if cell == 'UNKNOWN ':
                        if monster_chance <= 1:
                            demon = monster.Monster()
                            fight = combat.Battle(player, demon, game_information)
                            fight.combat()
                        else:
                            player.modify_health(1)
                            # grid updates to show previous location
                            dungeon_map.add_travelled_to_grid(player.row_position, player.column_position)
                            # player moves in specified direction
                            player.move_west()
                            dungeon_map.add_player_to_grid(player.row_position, player.column_position)

                    elif cell == 'TRAP':
                        trap_damage = random.randint(0, 2)
                        player.modify_health(trap_damage * -1)
                        print("You have fallen into a trap! You took {} damage".format(trap_damage))
                        # grid updates to show previous location
                        dungeon_map.add_travelled_to_grid(player.row_position, player.column_position)
                        # player moves in specified direction
                        player.move_west()
                        dungeon_map.add_player_to_grid(player.row_position, player.column_position)

                    elif cell == "CHEST":
                        player.modify_health(1)
                        item = dungeon_map.get_chest_item()
                        print("You have found a treasure chest! You added {} to your inventory".format(item))
                        player.add_inventory(item)
                        # grid updates to show previous location
                        dungeon_map.add_travelled_to_grid(player.row_position, player.column_position)
                        # player moves in specified direction
                        player.move_west()
                        dungeon_map.add_player_to_grid(player.row_position, player.column_position)

                    elif cell == "GOAL":
                        gatekeeper = False
                        print(ending_message)

            elif user_input == "south" or user_input == "s":
                # check for out of bounds
                try:
                    cell = dungeon_map.get_cell(player.row_position + 1, player.column_position)

                except IndexError:
                    print("You've reached the end of the world!")

                else:
                    if cell == 'UNKNOWN ':
                        if monster_chance <= 1:
                            demon = monster.Monster()
                            fight = combat.Battle(player, demon, game_information)
                            fight.combat()
                        else:
                            player.modify_health(1)
                            # grid updates to show previous location
                            dungeon_map.add_travelled_to_grid(player.row_position, player.column_position)
                            # player moves in specified direction
                            player.move_south()
                            dungeon_map.add_player_to_grid(player.row_position, player.column_position)

                    elif cell == 'TRAP':
                        trap_damage = random.randint(0, 2)
                        player.modify_health(trap_damage * -1)
                        print("You have fallen into a trap! You took {} damage".format(trap_damage))
                        # grid updates to show previous location
                        dungeon_map.add_travelled_to_grid(player.row_position, player.column_position)
                        # player moves in specified direction
                        player.move_south()
                        dungeon_map.add_player_to_grid(player.row_position, player.column_position)

                    elif cell == "CHEST":
                        player.modify_health(1)
                        item = dungeon_map.get_chest_item()
                        print("You have found a treasure chest! You added {} to your inventory".format(item))
                        player.add_inventory(item)
                        # grid updates to show previous location
                        dungeon_map.add_travelled_to_grid(player.row_position, player.column_position)
                        # player moves in specified direction
                        player.move_south()
                        dungeon_map.add_player_to_grid(player.row_position, player.column_position)

                    elif cell == "GOAL":
                        gatekeeper = False
                        print(ending_message)

            else:
                print("That input is not valid, Enter 'help' for more information")


if __name__ == "__main__":
    main()
