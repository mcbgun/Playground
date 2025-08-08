# Boxing Manager - Main Entry Point

from game.boxer_generator import BoxerGenerator
from game.fight import Fight

def main():
    """Main function to run the game."""
    print("Welcome to Boxing Manager!")
    print("="*30)

    # 1. Create a BoxerGenerator
    generator = BoxerGenerator()

    # 2. Create two boxers
    boxer1 = generator.create_boxer()
    boxer2 = generator.create_boxer()

    print("Two boxers have been generated:")
    print(f"Boxer 1: {boxer1}")
    print(f"Boxer 2: {boxer2}")
    print("="*30)
    print("Let's get ready to rumble!")
    print("="*30)


    # 3. Create a Fight
    fight = Fight(boxer1, boxer2)

    # 4. Simulate the fight
    log, winner = fight.simulate()

    # 5. Print the log
    for line in log:
        print(line)

    print("="*30)
    if winner:
        print(f"The winner is {winner.name}!")
    else:
        print("The fight is a draw!")


if __name__ == "__main__":
    main()
