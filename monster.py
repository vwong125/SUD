# Vincent Wong
# A01051004

import doctest
import random


class Monster:
    def __init__(self):
        """Initialize the Monster constructor,

        PARAM: None
        PRECONDITION: None
        POST-CONDITION: None
        RETURN: None
        """

        self.name = random.choice(["Diablo", "Baal", "Mephisto", "Andariel", "Belial", "Azmodan", "Lilth"])
        self.hp = 8

    def roll_attack(self) -> int:
        """Roll a d6 dice to indicate the monster's attack,

        PARAM: None
        PRECONDITION: Random module must be imported
        POST-CONDITION: None
        RETURN: Return a random integer from 1 - 6

        >>> monster = Monster()
        >>> random.seed(1)
        >>> monster.roll_attack()
        2
        """

        attack = random.randint(1, 6)
        return attack

    def roll_flee_attack(self) -> int:
        """Roll a d4 to indicate the monster's attack when the player flees,

        PARAM: None
        PRECONDITION: Random Module must be imported
        POST-CONDITION: None
        RETURN: Return a random integer from 1 - 4

        >>> monster = Monster()
        >>> random.seed(1)
        >>> monster.roll_flee_attack()
        2
        """

        attack = random.randint(1, 4)
        return attack

    def modify_health(self, number: int) -> None:
        """Modify the monster's hp,

        PARAM: Number, a negative integer
        PRECONDITION: Number must be an integer, player must be instantiated
        POST-CONDITION: User's hp is modified through the addition of the number
        RETURN: None

        >>> monster = Monster()
        >>> print(monster.hp)
        8
        >>> monster.modify_health(2)
        >>> print(monster.hp)
        10
        >>> monster.modify_health(-4)
        >>> print(monster.hp)
        6
        """

        self.hp += number

    def display_health(self) -> None:
        """Display the monster's hp,

        PARAM: None
        PRECONDITION: Monster class must be initialized
        POST-CONDITION: None
        RETURN: None

        >>> monster = Monster()
        >>> monster.display_health()
        8
        >>> monster.modify_health(2)
        >>> monster.display_health()
        10
        >>> monster.modify_health(-4)
        >>> monster.display_health()
        6
        """

        print(self.hp)


if __name__ == "__main__":
    doctest.testmod()
