import random
from .boxer import Boxer

class BoxerGenerator:
    """Generates new boxers."""

    FIRST_NAMES = ["John", "Mike", "Chris", "David", "James", "Robert", "William", "Joseph", "Charles", "Thomas"]
    LAST_NAMES = ["Smith", "Jones", "Williams", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson"]

    def create_boxer(self):
        """Creates a new boxer with randomized attributes."""
        name = f"{random.choice(self.FIRST_NAMES)} {random.choice(self.LAST_NAMES)}"
        age = random.randint(18, 25)
        weight = random.randint(60, 100)

        boxer = Boxer(name, age, weight)

        # Randomize attributes
        boxer.strength = random.randint(30, 70)
        boxer.speed = random.randint(30, 70)
        boxer.stamina = random.randint(30, 70)
        boxer.chin = random.randint(30, 70)
        boxer.punching_power = random.randint(30, 70)
        boxer.technique = random.randint(30, 70)
        boxer.defence = random.randint(30, 70)
        boxer.jab = random.randint(30, 70)
        boxer.hook = random.randint(30, 70)
        boxer.uppercut = random.randint(30, 70)
        boxer.aggression = random.randint(30, 70)
        boxer.determination = random.randint(30, 70)

        return boxer
