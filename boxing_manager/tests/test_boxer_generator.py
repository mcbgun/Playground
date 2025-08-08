import unittest
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.boxer import Boxer
from game.boxer_generator import BoxerGenerator

class TestBoxerGenerator(unittest.TestCase):
    """Tests for the BoxerGenerator class."""

    def test_create_boxer(self):
        """Test that create_boxer returns a valid Boxer object with attributes in range."""
        generator = BoxerGenerator()
        boxer = generator.create_boxer()

        self.assertIsInstance(boxer, Boxer)

        # Test name is a string with two parts
        self.assertIsInstance(boxer.name, str)
        self.assertEqual(len(boxer.name.split()), 2)

        # Test attribute ranges
        self.assertTrue(18 <= boxer.age <= 25)
        self.assertTrue(60 <= boxer.weight <= 100)
        self.assertTrue(30 <= boxer.strength <= 70)
        self.assertTrue(30 <= boxer.speed <= 70)
        self.assertTrue(30 <= boxer.stamina <= 70)
        self.assertTrue(30 <= boxer.chin <= 70)
        self.assertTrue(30 <= boxer.punching_power <= 70)
        self.assertTrue(30 <= boxer.technique <= 70)
        self.assertTrue(30 <= boxer.defence <= 70)
        self.assertTrue(30 <= boxer.jab <= 70)
        self.assertTrue(30 <= boxer.hook <= 70)
        self.assertTrue(30 <= boxer.uppercut <= 70)
        self.assertTrue(30 <= boxer.aggression <= 70)
        self.assertTrue(30 <= boxer.determination <= 70)

if __name__ == '__main__':
    unittest.main()
