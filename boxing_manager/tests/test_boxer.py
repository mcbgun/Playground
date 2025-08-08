import unittest
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.boxer import Boxer

class TestBoxer(unittest.TestCase):
    """Tests for the Boxer class."""

    def test_initialization(self):
        """Test that a Boxer is initialized with the correct attributes."""
        boxer = Boxer("Test Fighter", 25, 70)
        self.assertEqual(boxer.name, "Test Fighter")
        self.assertEqual(boxer.age, 25)
        self.assertEqual(boxer.weight, 70)

        # Test default skill values
        self.assertEqual(boxer.strength, 50)
        self.assertEqual(boxer.speed, 50)
        self.assertEqual(boxer.stamina, 50)
        self.assertEqual(boxer.chin, 50)
        self.assertEqual(boxer.punching_power, 50)
        self.assertEqual(boxer.technique, 50)
        self.assertEqual(boxer.defence, 50)
        self.assertEqual(boxer.jab, 50)
        self.assertEqual(boxer.hook, 50)
        self.assertEqual(boxer.uppercut, 50)
        self.assertEqual(boxer.aggression, 50)
        self.assertEqual(boxer.determination, 50)

        # Test default in-fight stats
        self.assertEqual(boxer.health, 100)
        self.assertEqual(boxer.current_stamina, 100)

    def test_prepare_for_fight(self):
        """Test that prepare_for_fight resets health and stamina."""
        boxer = Boxer("Test Fighter", 25, 70)
        boxer.stamina = 80 # Set a custom stamina value
        boxer.health = 50
        boxer.current_stamina = 20

        boxer.prepare_for_fight()

        self.assertEqual(boxer.health, 100)
        self.assertEqual(boxer.current_stamina, 80)

if __name__ == '__main__':
    unittest.main()
