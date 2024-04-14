"""Define the class factory."""


class Factory:
    """Product characters based on string class name."""

    character_classes = {
        "warrior": "Warrior",
        "archer": "Archer",
        "wizard": "Wizard",
        "orc": "Orc",
        "wolf": "Wolf",
        "zombie": "Zombie"
    }

    @classmethod
    def get_character(cls, class_name):
        """Return a specific character object based on a class name."""
        character_class_name = cls.character_classes.get(class_name)
        if character_class_name:
            character_class = getattr(
                __import__("characters.character",
                           fromlist=[character_class_name]),
                character_class_name)
            return character_class()
        raise ValueError(f"Unknown character class: {class_name}")

    @classmethod
    def get_available_characters(cls):
        """Return a list of available character classes."""
        return list(cls.character_classes.keys())
