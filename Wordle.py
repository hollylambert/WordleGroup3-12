"""
Starter file
"""
import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import (
    WordleGWindow,
    N_ROWS,
    N_COLS,
    CORRECT_COLOR,
    PRESENT_COLOR,
    MISSING_COLOR,
)

"""
# Process through each letter in the guess and determine it's color
def processGuess(random_word, entered_word, gw):
    position = 0
    cell = ""
    for letter in entered_word:
        if letter == random_word[position]:
            cell = gw.set_square_color(gw.get_current_row, position, CORRECT_COLOR)
            # cell += "G"
        elif letter in random_word:
            cell = gw.set_square_color(gw.get_current_row, position, PRESENT_COLOR)
            # cell += "Y"
        else:
            cell = gw.set_square_color(gw.get_current_row, position, MISSING_COLOR)
            # cell += "-"
        position += 1
    # print(cell)
    return cell
"""


def wordle():
    # Generates a random index to choose a word from the FIVE_LETTER_WORDS array
    index = random.randint(0, len(FIVE_LETTER_WORDS) - 1)

    # randomly selects a letter from FIVE_LETTER_WORDS using the randomly selected index
    random_word = FIVE_LETTER_WORDS[index]

    def enter_action(s, N_ROWS, gw):
        # Allow user to continue guessing for all 6 guesses

        entered_word = s.lower()

        if entered_word in FIVE_LETTER_WORDS:
            gw.show_message("That word is valid!")
        else:
            gw.show_message("Not in word list")

        # processGuess(random_word, entered_word, gw)

        # iterate to the next row
        N_ROWS -= 1

    N_ROWS = 6
    gw = WordleGWindow()

    while N_ROWS > 0:
        gw.add_enter_listener(
            lambda s, N_ROWS=N_ROWS, gw=gw: enter_action(s, N_ROWS, gw)
        )

        """
        # Displays the random word after first guess is made for MILESTONE 1

        random_word_letters = []
        for letter in random_word:
            random_word_letters.append(letter)
        gw.set_square_letter(0, 0, random_word_letters[0])
        gw.set_square_letter(0, 1, random_word_letters[1])
        gw.set_square_letter(0, 2, random_word_letters[2])
        gw.set_square_letter(0, 3, random_word_letters[3])
        gw.set_square_letter(0, 4, random_word_letters[4])

        # gw.show_message("You have to implement this method.")
        """


# Startup code
if __name__ == "__main__":
    wordle()
