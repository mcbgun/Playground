import random
from .boxer import Boxer

class Fight:
    """Simulates a fight between two boxers."""

    def __init__(self, boxer1: Boxer, boxer2: Boxer, rounds=12):
        self.boxer1 = boxer1
        self.boxer2 = boxer2
        self.rounds = rounds
        self.log = []
        self.boxer1_score = 0
        self.boxer2_score = 0

    def simulate(self):
        """Simulates the entire fight."""
        self.boxer1.prepare_for_fight()
        self.boxer2.prepare_for_fight()

        for i in range(1, self.rounds + 1):
            round_winner, knockout = self.simulate_round(i)

            if knockout:
                self.log.append(f"{round_winner.name} wins by knockout in round {i}!")
                return self.log, round_winner

            if round_winner == self.boxer1:
                self.boxer1_score += 10
                self.boxer2_score += 9
            elif round_winner == self.boxer2:
                self.boxer2_score += 10
                self.boxer1_score += 9
            else: # Draw
                self.boxer1_score += 10
                self.boxer2_score += 10

        winner = self.decision()
        self.log.append(f"The fight goes to a decision...")
        self.log.append(f"Final Score: {self.boxer1.name} {self.boxer1_score} - {self.boxer2_score} {self.boxer2.name}")
        self.log.append(f"{winner.name} wins by decision!")
        return self.log, winner

    def simulate_round(self, round_num):
        """Simulates a single round."""
        self.log.append(f"--- Round {round_num} ---")

        boxer1_hits = 0
        boxer2_hits = 0

        for _ in range(10): # 10 exchanges per round
            # Boxer 1 attacks
            if self.attempt_punch(self.boxer1, self.boxer2):
                boxer1_hits += 1
                if self.boxer2.health <= 0:
                    return self.boxer1, True # Knockout

            # Boxer 2 attacks
            if self.attempt_punch(self.boxer2, self.boxer1):
                boxer2_hits += 1
                if self.boxer1.health <= 0:
                    return self.boxer2, True # Knockout

        # Determine round winner
        if boxer1_hits > boxer2_hits:
            self.log.append(f"{self.boxer1.name} wins the round.")
            return self.boxer1, False
        elif boxer2_hits > boxer1_hits:
            self.log.append(f"{self.boxer2.name} wins the round.")
            return self.boxer2, False
        else:
            self.log.append("The round is a draw.")
            return None, False

    def attempt_punch(self, attacker: Boxer, defender: Boxer):
        """Simulates a single punch attempt."""
        # Stamina affects performance
        stamina_factor = max(0, attacker.current_stamina) / attacker.stamina

        chance_to_hit = 50 + (attacker.technique - defender.defence) * stamina_factor
        chance_to_hit = max(10, min(chance_to_hit, 90)) # Clamp between 10% and 90%

        attacker.current_stamina -= 2 # Cost of throwing a punch

        if random.randint(1, 100) < chance_to_hit:
            damage = (attacker.punching_power / 10) * random.uniform(0.8, 1.2) * stamina_factor
            defender.health -= damage
            self.log.append(f"{attacker.name} lands a punch on {defender.name}! (Health: {defender.health:.1f})")
            return True
        else:
            self.log.append(f"{attacker.name} misses.")
            return False

    def decision(self):
        """Determines the winner by decision."""
        if self.boxer1_score > self.boxer2_score:
            return self.boxer1
        elif self.boxer2_score > self.boxer1_score:
            return self.boxer2
        else:
            # Scores are level, it's a draw
            return None
