"""Define the Character class."""
# coding: utf-8
# pylint: disable=E1101
import random


class Character:
    """Mother class with base characteristics of the different characters.

    Class attribute: actions
    Attribute: name, life, attack, defense, agility
    Methods: attacks, escape
    """

    actions = {"a": "attack", "e": "escape"}

    def __init__(self, **kwargs):
        """Construct the character."""
        valid_keys = ["life", "attack", "defense", "agility", "name"]
        for key in valid_keys:
            setattr(self, key, kwargs.get(key))

    def attacks(self, target):
        """Attack an other character.

        If the target can not avoid the attack, it looses life
        """
        print(f"{self.name} attack {target.name}")
        # Offer a chance to the target to avoid the attack
        # Example: a character with 50 in agility has 1/2 chances to avoid the attack
        if random.randrange(0, 100) <= target.agility:
            print(f"{target.name} dodged the attack. ")
            return False
        # Subtract to target's life the character's attack minus the target defens divided by 5
        target.life -= self.attack - (target.defense / 5)
        # Make sure characters can not have negative life
        target.life = max(target.life, 0)
        print(f"{target.name} has now {target.life} health points.")
        return None

    def escape(self):
        """Allow the character to try to escape and leave the fight."""
        # Lower the chance to escape according to the character's agility
        agi = round(self.agility / 5)
        if random.randrange(0, 100) <= agi:
            return True
        return False

    def make_action(self, action, ennemy):
        """Execute the corresponding method based on an action string."""
        if action not in self.actions:
            print("Impossible action.")
            return False
        if action == "a":
            self.attacks(ennemy)
        elif action == "f":
            if self.escape():
                # If the escape is a success we raise an exception because the fight comes to an end
                print("You escaped with agility.")
                raise ValueError("Character Escaping")
            print("Enemy is on you !")
        elif action == "s":
            self.heal()
        return True

    def __str__(self):
        """Show the Char."""
        return f"{self.name} : life = {self.life}"


class Warrior(Character):  # pylint: disable=too-few-public-methods
    """Class representing a warrior character."""

    def __init__(self, name=False):
        """Initiate the warrior."""
        super().__init__(life=500, attack=50, defense=80, agility=10, name=name)


class Orc(Character):  # pylint: disable=too-few-public-methods
    """Class representing an orc character."""

    def __init__(self, name=False):
        """Initiate the Orc."""
        super().__init__(life=400, attack=40, defense=70, agility=20, name=name)


class Archer(Character):  # pylint: disable=too-few-public-methods
    """Class representing an archer character."""

    def __init__(self, name=False):
        """Initiate the Archer."""
        super().__init__(life=300, attack=50, defense=70, agility=20, name=name)


class Wizard(Character):  # pylint: disable=too-few-public-methods
    """Class representing a wizard character.

    Attributes: mana
    Methods = heal, str
    """

    def __init__(self, name=False):
        """Initiate the magician."""
        super().__init__(life=600, attack=20, defense=50, agility=50, name=name)
        Character.actions.update({"h": "heal"})
        # Represents the magical power
        self.mana = 200

    def heal(self):
        """Increase the life of the wizard with the mana power."""
        # The spell requires at least 50 points of mana
        if self.mana >= 50:
            print(f"{self.name} cast a health spell.")
            self.mana -= 50
            self.life += 20
            print(
                f"""{self.name} gained 20 health points, actual health :
                {self.life}"""
            )
        else:
            print(
                f"""{self.name} tries to draw from himself the necessary strength to heal
                himself but his mana is not sufficient"""
            )

    def __str__(self):
        """Display the class."""
        return f"{self.name} : life = {self.life}, mana = {self.mana}"


class Zombie(Character):
    """Define the zombie."""

    def __init__(self, name=False):
        """Initiate the class."""
        super().__init__(life=600, attack=15, defense=15, agility=5, name=name)


class Wolf(Character):
    """Define the wolf."""

    def __init__(self, name=False):
        """Initiate the class."""
        super().__init__(life=300, attack=30, defense=15, agility=40, name=name)
