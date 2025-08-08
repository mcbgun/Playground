import unittest
from unittest.mock import patch
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.boxer import Boxer
from game.fight import Fight

class TestFight(unittest.TestCase):
    """Tests for the Fight class."""

    def setUp(self):
        """Set up two boxers for the tests."""
        self.boxer1 = Boxer("Fighter One", 30, 80)
        self.boxer2 = Boxer("Fighter Two", 30, 80)

    def test_fight_simulation_runs(self):
        """Test that a fight simulation runs to completion."""
        fight = Fight(self.boxer1, self.boxer2)
        log, winner = fight.simulate()
        self.assertIsInstance(log, list)
        self.assertTrue(isinstance(winner, Boxer) or winner is None)

    @patch('random.randint', return_value=1) # Always hits
    @patch('random.uniform', return_value=1.2) # Max damage
    def test_knockout_scenario(self, mock_uniform, mock_randint):
        """Test a fight that ends in a knockout."""
        strong_boxer = Boxer("KO King", 30, 80)
        strong_boxer.punching_power = 100
        strong_boxer.technique = 100
        strong_boxer.stamina = 100

        weak_boxer = Boxer("Glass Joe", 30, 80)
        weak_boxer.chin = 10
        weak_boxer.defence = 10

        fight = Fight(strong_boxer, weak_boxer, rounds=1)
        log, winner = fight.simulate()

        self.assertEqual(winner, strong_boxer)
        self.assertIn("wins by knockout", log[-1])

    @patch('game.fight.Fight.simulate_round')
    def test_decision_win(self, mock_simulate_round):
        """Test a fight that ends in a decision win."""
        # Make boxer1 win every round
        mock_simulate_round.return_value = (self.boxer1, False)

        fight = Fight(self.boxer1, self.boxer2)
        log, winner = fight.simulate()

        self.assertEqual(winner, self.boxer1)
        self.assertIn("wins by decision", log[-1])
        # Check the score: 12 rounds * 10 points for winner, 9 for loser
        self.assertEqual(fight.boxer1_score, 120)
        self.assertEqual(fight.boxer2_score, 108)

    @patch('game.fight.Fight.simulate_round')
    def test_draw_scenario(self, mock_simulate_round):
        """Test a fight that ends in a draw."""
        # Make every round a draw
        mock_simulate_round.return_value = (None, False)

        fight = Fight(self.boxer1, self.boxer2)
        log, winner = fight.simulate()

        self.assertIsNone(winner)
        self.assertIn("The fight is a draw!", log[-1])

    def test_health_and_stamina_decrease(self):
        """Test that health and stamina decrease during a fight."""
        self.boxer1.prepare_for_fight()
        self.boxer2.prepare_for_fight()
        boxer1_initial_health = self.boxer1.health
        boxer2_initial_health = self.boxer2.health
        boxer1_initial_stamina = self.boxer1.current_stamina
        boxer2_initial_stamina = self.boxer2.current_stamina

        # Give one boxer a high technique and the other a low defence to increase the chance of hits.
        self.boxer1.technique = 100
        self.boxer2.defence = 0

        fight = Fight(self.boxer1, self.boxer2, rounds=1)
        fight.simulate()

        # Check that stamina has decreased for both boxers
        self.assertTrue(self.boxer1.current_stamina < boxer1_initial_stamina)
        self.assertTrue(self.boxer2.current_stamina < boxer2_initial_stamina)

        # Check that health has decreased for at least one boxer (it's possible one boxer misses all punches)
        self.assertTrue(self.boxer1.health < boxer1_initial_health or self.boxer2.health < boxer2_initial_health)

if __name__ == '__main__':
    unittest.main()
