"""Define the story agent."""
# coding: utf-8

# import os
import time


class storyAgent:  # pylint: disable=too-few-public-methods
    """Mother class to all the objects that make the story (narrator, arena).

    attributs : none
    methods : transition
    """

    def __init__(self):
        """Init th class."""

    def transition(self, waiting_time):
        """Make a break and clear the screen."""
        time.sleep(waiting_time)
        # os.system("cls||clear")
