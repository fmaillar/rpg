class Factory:
    """Class factory to product characters based on string class name."""

    # Dictionary mapping class names to their corresponding classes
    character_classes = {
        "warrior": "Warrior",
        "archer": "Archer",
        "wizard": "Wizard",
        "orc": "Orc",
        "wolf": "Wolf",
        "zombie": "Zombie",
    }

    @classmethod
    def get_character(cls, class_name):
        """Return a specific character object based on a class name."""
        if class_name in cls.character_classes:
            # Dynamically import the corresponding class
            character_class = cls.character_classes[class_name]
            character_module = __import__(
                "characters." + character_class.lower(), fromlist=[character_class]
            )
            character_class = getattr(character_module, character_class)
            return character_class()
        return None
