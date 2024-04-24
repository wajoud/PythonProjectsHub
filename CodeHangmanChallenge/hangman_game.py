import random

def hangman():
    words = ["tiger", "superman", "thor", "doraemon", "avenger", "water", "stream"]
    word = random.choice(words)
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guesses = ''

    def show_hangman(turns):
        stages = [  # final state: head, torso, both arms, and both legs
                    """
                       --------
                       |      |
                       |      O
                       |     \|/
                       |      |
                       |     / \\
                       -
                    """,
                    # head, torso, both arms, and one leg
                    """
                       --------
                       |      |
                       |      O
                       |     \|/
                       |      |
                       |     / 
                       -
                    """,
                    # head, torso, and both arms
                    """
                       --------
                       |      |
                       |      O
                       |     \|/
                       |      |
                       |      
                       -
                    """,
                    # head, torso, and one arm
                    """
                       --------
                       |      |
                       |      O
                       |     \|
                       |      |
                       |     
                       -
                    """,
                    # head and torso
                    """
                       --------
                       |      |
                       |      O
                       |      |
                       |      |
                       |     
                       -
                    """,
                    # head
                    """
                       --------
                       |      |
                       |      O
                       |    
                       |      
                       |     
                       -
                    """,
                    # initial empty state
                    """
                       --------
                       |      |
                       |      
                       |    
                       |      
                       |     
                       -
                    """
        ]
        print(stages[6 - turns])

    print(f"Welcome {name}! Let's play Hangman.")
    print("Try to guess the word in less than 10 attempts.")

    while len(word) > 0:
        main_word = ""
        missed = 0

        for letter in word:
            if letter in guesses:
                main_word += letter
            else:
                main_word += "_ "

        if main_word == word:
            print(main_word)
            print("You win!")
            break

        print("Guess the word:", main_word)
        guess = input("Enter a letter: ").lower()

        if guess in valid_letters:
            guesses += guess
        else:
            print("Enter a valid character.")
            continue

        if guess not in word:
            turns -= 1
            show_hangman(turns)
            if turns == 0:
                print("You lose")
                print(f"The word was: {word}")
                print("You let a kind man die.")
                break

name = input("Enter your name: ")
hangman()
