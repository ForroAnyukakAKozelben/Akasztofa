import random
import os
import time
import platform

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


HANGMAN = [
    """
     -----
     |   |
         |
         |
         |
         |
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    """
]





def guessing_letter(word, guess):
    used_letters = set()
    wrong_letters = set()
    tries = 0
    MAX_TRIES = 5

    while "".join(guess).lower() != word.lower() and tries < MAX_TRIES:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

        print(HANGMAN[tries])
        print("Szó:", " ".join(guess))
        print("Hibás betűk:", ", ".join(sorted(wrong_letters)))
        print(f"Hátralévő próbálkozások: {MAX_TRIES - tries}")