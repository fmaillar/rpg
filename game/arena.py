"""Define the arena."""
# coding: utf-8

from .storyAgent import storyAgent


class Arena(storyAgent):
    """Class to represent a battle during the story and manage the fights.

    Attributes : player, enemy
    methods: fighters_enter, fighters_leave, battle
    """

    def __init__(self):
        """Innit the arena."""
        # Both attribute expect characters objects
        self.player = False
        self.ennemy = False

    def fighters_enter(self, player, ennemy):
        """Store characters objects in player and enemy attribute."""
        self.player = player
        self.ennemy = ennemy

    def fighters_leave(self):
        """Clear player and enemy attribute."""
        self.player = False
        self.ennemy = False

    def battle(self):
        """Ask player for an action and do it while both are alive."""
        self.transition(1)
        init_life = self.player.life
        # As long both characters are alive
        while self.player.life > 0 and self.ennemy.life > 0:
            try:
                action_is_allowed = False
                # check if the character can make the action and execute it
                while not action_is_allowed:
                    print(f"{self.player} || {self.ennemy}")
                    action = input(
                        f"What are you doing {self.player.actions} ? : ".lower())
                    action_is_allowed = self.player.make_action(action, self.ennemy)
            # If the character succeed to escape
            except ValueError:
                break
            # Ennemie's turn, if not dead
            if self.ennemy.life > 0:
                self.ennemy.attacks(self.player)
            self.transition(1)
        # End of the fight
        print("Fight is done.")
        self.player.life = init_life
        self.fighters_leave()
