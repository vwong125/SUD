# Vincent Wong
# A01051004

import character  # for doctests
import game_info  # for doctests
import monster  # for doctests
import random


class Battle:
    def __init__(self, player_obj: character.Player, monster_obj: monster.Monster, game_obj: game_info.Game) -> None:
        """initialize the Battle constructor,

        PARAM: Player must be a player object initiated using the P{layer class, Monster_obj must be a monster object
        initiated using the Monster class
        PRECONDITION: Player and Monster class must be used to create the player_obj and monster_obj
        POST-CONDITION: None
        RETURN: None
        """

        self.player = player_obj
        self.monster = monster_obj
        self.game_obj = game_obj

    def combat(self) -> None:
        """simulate combat between the Monster and the Player,

        PARAM: None
        PRECONDITION: Battle class must be initialized
        POST-CONDITION: Player and Monster hp is modified
        RETURN: False - ends the game loop
        """

        # display message to indicate that the player is in battle
        print("{} has appeared! You are now in combat".format(self.monster.name))

        # sentinel
        battle_condition = True

        # battle loop
        while battle_condition:
            # check if user has died. If so, end battle loop
            if self.player.hp <= 0:
                battle_condition = False

            # if player alive, enter loop
            else:
                player_input = input("Enter a BATTLE command. Type in 'help' to show commands\n")

                # attack event - player always goes first
                if player_input == "attack":
                    player_attack = self.player.roll_attack()
                    self.monster.modify_health(player_attack * -1)
                    print("You have inflicted {} damage to {}".format(player_attack, self.monster.name))
                    # if monster died, end game loop
                    if self.monster.hp <= 0:
                        print("You have slain the enemy!")
                        battle_condition = False
                    else:
                        # if monster alive, it attacks
                        monster_attack = self.monster.roll_attack()
                        self.player.modify_health(monster_attack * -1)
                        print("{} inflicted {} damage to you".format(self.monster.name, monster_attack))
                        # if player died, end battle loop else continue with for loop
                        if self.player.hp <= 0:
                            print("you have been slain by {}".format(self.monster.name))
                            battle_condition = False

                # flee event
                elif player_input == "flee":
                    # calculate a random chance to hit the user
                    monster_chance_to_hit = random.randint(1, 10)
                    # 30% chance for the monster to hit. If monster hits, player fails to flee
                    if monster_chance_to_hit <= 3:
                        monster_attack = self.monster.roll_flee_attack()
                        self.player.modify_health(monster_attack * -1)
                        print("{} inflicted {} damage to you while you fled...try again".format
                              (self.monster.name, monster_attack))
                    # player successfully flees if monster fails to hit
                    else:
                        print("You have successfully fled from battle")
                        battle_condition = False

                elif player_input == 'hp':
                    self.game_obj.display_health()

                elif player_input == 'monster hp':
                    self.monster.display_health()

                elif player_input == 'help':
                    self.game_obj.display_battle_commands()

                elif player_input == 'potion':
                    self.player.use_potion()

                else:
                    print("That input is not valid. Type 'help' for valid commands")
