# Boxer Class

class Boxer:
    """Represents a boxer in the game."""

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        # Physical Attributes
        self.strength = 50
        self.speed = 50
        self.stamina = 50
        self.chin = 50

        # Technical Attributes
        self.punching_power = 50
        self.technique = 50
        self.defence = 50
        self.jab = 50
        self.hook = 50
        self.uppercut = 50

        # Mental Attributes
        self.aggression = 50
        self.determination = 50

        # In-fight stats
        self.health = 100
        self.current_stamina = 100

    def prepare_for_fight(self):
        """Resets health and stamina for a new fight."""
        self.health = 100
        self.current_stamina = self.stamina

    def __str__(self):
        return f"{self.name} ({self.age} y/o, {self.weight} kg)"
