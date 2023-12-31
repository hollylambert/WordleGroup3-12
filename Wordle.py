"""
Starter file
"""
import random
from WordleDictionary import (
    FIVE_LETTER_WORDS,
    FRENCH_FIVE_LETTER_WORDS,
    SPANISH_FIVE_LETTER_WORDS,
)
from WordleGraphics import (
    WordleGWindow,
    N_ROWS,
    N_COLS,
    CORRECT_COLOR,
    PRESENT_COLOR,
    MISSING_COLOR,
    DarkModeButton,
)


# Process through each letter in the guess and determine it's color
def processGuess(random_word, entered_word, gw):
    position = 0
    cell = ""
    if DarkModeButton.invert_colors == True:
        CORRECT_COLOR = "#1AFF1A"  # Light green for correct letters
        PRESENT_COLOR = "#994F00"  # Brownish yellow for misplaced letters
        MISSING_COLOR = "#999999"  # Gray for letters that don't appear

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


def en_wordle():
    # Generates a random index to choose a word from the FIVE_LETTER_WORDS array
    index = random.randint(0, len(FIVE_LETTER_WORDS) - 1)

    # randomly selects a letter from FIVE_LETTER_WORDS using the randomly selected index
    random_word = FIVE_LETTER_WORDS[index]

    def enter_action(s):
        # Allow user to continue guessing for all 6 guesses
        global N_ROWS

        entered_word = s.lower()

        if entered_word in FIVE_LETTER_WORDS:
            gw.show_message("That word is valid!")
        else:
            gw.show_message("Not in word list")

        # processGuess(random_word, entered_word, gw)

        # iterate to the next row
        N_ROWS -= 1

    gw = WordleGWindow()

    while N_ROWS > 0:
        gw.add_enter_listener(enter_action(s))

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


# this was included right before enter_action in the while loop: lambda s, N_ROWS=N_ROWS, gw=gw: -I'm trying to see if this is the issue

# Startup code
if __name__ == "__main__":
    en_wordle()


def fr_wordle():
    # Generates a random index to choose a word from the FIVE_LETTER_WORDS array
    index = random.randint(0, len(FRENCH_FIVE_LETTER_WORDS) - 1)

    # randomly selects a letter from FIVE_LETTER_WORDS using the randomly selected index
    random_word = FRENCH_FIVE_LETTER_WORDS[index]

    def enter_action(s):
        # Allow user to continue guessing for all 6 guesses
        global N_ROWS

        entered_word = s.lower()

        if entered_word in FRENCH_FIVE_LETTER_WORDS:
            gw.show_message("Ce mot est valable!")
        else:
            gw.show_message("Pas dans la liste de mots.")

        # processGuess(random_word, entered_word, gw)

        # iterate to the next row
        N_ROWS -= 1

    gw = WordleGWindow()

    while N_ROWS > 0:
        gw.add_enter_listener(enter_action(s))

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


# this was included right before enter_action in the while loop: lambda s, N_ROWS=N_ROWS, gw=gw: -I'm trying to see if this is the issue

# Startup code
if __name__ == "__main__":
    fr_wordle()


def sp_wordle():
    # Generates a random index to choose a word from the FIVE_LETTER_WORDS array
    index = random.randint(0, len(SPANISH_FIVE_LETTER_WORDS) - 1)

    # randomly selects a letter from FIVE_LETTER_WORDS using the randomly selected index
    random_word = SPANISH_FIVE_LETTER_WORDS[index]

    def enter_action(s):
        # Allow user to continue guessing for all 6 guesses
        global N_ROWS

        entered_word = s.lower()

        if entered_word in SPANISH_FIVE_LETTER_WORDS:
            gw.show_message("¡Esa palabra es válida!")
        else:
            gw.show_message("No en la lista de palabras.")

        # processGuess(random_word, entered_word, gw)

        # iterate to the next row
        N_ROWS -= 1

    gw = WordleGWindow()

    while N_ROWS > 0:
        gw.add_enter_listener(enter_action(s))

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


# this was included right before enter_action in the while loop: lambda s, N_ROWS=N_ROWS, gw=gw: -I'm trying to see if this is the issue

# Startup code
if __name__ == "__main__":
    sp_wordle()
