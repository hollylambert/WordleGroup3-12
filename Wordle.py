"""
Starter file
"""
import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_ROWS, N_COLS


def wordle():
    def enter_action(s):
        entered_word = s.lower()

        if entered_word in FIVE_LETTER_WORDS:
            gw.show_message("That word is valid!")
        else:
            gw.show_message("Not in word list")

        # Generates a random index to choose a word from the FIVE_LETTER_WORDS array
        index = random.randint(0, len(FIVE_LETTER_WORDS) - 1)

        # randomly selects a letter from FIVE_LETTER_WORDS using the randomly selected index
        random_word = FIVE_LETTER_WORDS[index]

        # Displays the random word after first guess is made
        random_word_letters = []
        for letter in random_word:
            random_word_letters.append(letter)
        gw.set_square_letter(1, 0, random_word_letters[0])
        gw.set_square_letter(1, 1, random_word_letters[1])
        gw.set_square_letter(1, 2, random_word_letters[2])
        gw.set_square_letter(1, 3, random_word_letters[3])
        gw.set_square_letter(1, 4, random_word_letters[4])

        # gw.show_message("You have to implement this method.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)


# Startup code
if __name__ == "__main__":
    wordle()
