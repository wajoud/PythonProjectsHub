import random

def roll_dice():
    """Simulate rolling a dice and print the result with ASCII art."""
    number = random.randint(1, 6)
    dice_faces = {
        1: (
            "===========",
            "|         |",
            "|    O    |",  # One dot in the middle
            "|         |",
            "==========="
        ),
        2: (
            "===========",
            "| O       |",
            "|         |",  # Two dots, one in each corner
            "|       O |",
            "==========="
        ),
        3: (
            "===========",
            "| O       |",
            "|    O    |",  # Three dots in a diagonal
            "|       O |",
            "==========="
        ),
        4: (
            "===========",
            "| O     O |",
            "|         |",  # Four dots, each corner
            "| O     O |",
            "==========="
        ),
        5: (
            "===========",
            "| O     O |",
            "|    O    |",  # Five dots, center and all corners
            "| O     O |",
            "==========="
        ),
        6: (
            "===========",
            "| O  O  O |",
            "|         |",  # Six dots, three on top and bottom
            "| O  O  O |",
            "==========="
        ),
    }

    for line in dice_faces[number]:
        print(line)

def main():
    """Run the main program loop."""
    print("This is a dice simulator")
    while input("Press 'y' to roll again, any other key to exit: ").lower() == 'y':
        roll_dice()

if __name__ == "__main__":
    main()
