# coding: utf-8
"""Main of thr rpg."""

import random
from game.narrator import Narrator
from game.factory import Factory
from game.arena import Arena

if __name__ == "__main__":
    # Start a narrator to tell the story
    narrator = Narrator()
    # Start an arena where battles are going to take place
    arena = Arena()

    introduction = [
        "Welcome adventurer to the gates of a new world of magic and legends.",
        "Here begins your story, let yourself be guided by the narrator of this world.",
        "Your legend will resonate for centuries and centuries",
    ]
    narrator.tell(introduction)
    # Allow the user to choose his type of character and retrieve it from the factory
    choice = narrator.choose_character()
    player = Factory.get_character(choice)
    narrator.player_customization(player)

    # Exemple story to be told by the narrator
    story = [
        "Your journey begins. You walk along the edge of the towering mountains of Moria",
        "The sun is warm on your face and the snow is fresh at your feet",
        "You then hear a dull rustling, you turn around",
        "You then come face to face with an orc who attacks you",
    ]

    list_enemy_kind = ["bear", "orc", "wolf", "zombie"]
    list_enemy = random.sample(list_enemy_kind, 3)
    # Start fights
    for i, enem in enumerate(list_enemy):
        ennemy = Factory.get_character(enem)
        ennemy.name = enem + str(i + 1)
        # narrator.tell(story)
        arena.fighters_enter(player, ennemy)
        arena.battle()
