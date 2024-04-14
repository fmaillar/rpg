"""Define the narrator."""
# coding: utf-8

from .storyAgent import storyAgent


class Narrator(storyAgent):
    """Class to tell the story and interact with the player.

    Class attribute: allowed roles with their translation
    Attribute: none
    Methods: tell, choose_character, player_customization
    """

    roles = {"warrior": "warrior", "archer": "archer", "magician": "wizard"}

    def __init__(self):
        """Init."""

    def tell(self, story):
        """Display with a transition each sentence of a given list."""
        if not isinstance(story, list):
            raise ValueError("Method tell of narrator class expects a list as argument")
        for sentence in story:
            self.transition(3)
            print(sentence)

    def choose_character(self):
        """To allow the player to choose a character type from the roles.

        While the player does not choose an existant role the function runs a
        while loop.
        """
        self.transition(7)
        print(
            """Before starting your adventure, who do you want to play as?
- A warrior strong and solid as stone
- An archer who is agile and flexible like the wind
- An intelligent and cunning magician like the crow"""
        )
        while True:
            try:
                player_choice = input("I'd like to be : ").lower()
                # Check if player_choice is in the roles class attribut
                player_class = Narrator.roles[player_choice]
                break
            except KeyError:
                print("I don't know this character.")
        return player_class

    def player_customization(self, player):
        """Allow the player to choose a character name."""
        self.transition(2)
        name = input("What's your name adventurer ? : ")
        player.name = name
