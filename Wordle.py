
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
    BLUE_COLOR, 
    ROSE_COLOR,
    DarkModeButton,
)


def wordle():
    # Create a WordleGWindow for the game graphics
    gw = WordleGWindow()
    #choose language
    lang = input("Choose a language: English, French , Spanish : ").upper()
     # Allow the user to choose a color scheme
    color_scheme = DarkModeButton()
    if lang == "ENGLISH":
        wordlist= FIVE_LETTER_WORDS
    elif lang == "FRENCH":
        wordlist = FRENCH_FIVE_LETTER_WORDS
    elif lang == "SPANISH":
        wordlist = SPANISH_FIVE_LETTER_WORDS
    else:
        print("Invalid Language")
        return
    
    randomword = random.choice(wordlist)
    NumGuesses = 6
    
    def enter_action(s):
        nonlocal NumGuesses
        guessedWord = s.strip().lower()
       # Check if the guessed word has 5 letters
        if len(guessedWord) != 5:
            gw.show_message("Invalid input: Must be 5 letters.")
            return

        # Check if the guessed word is in the selected word list
        if guessedWord in wordlist:
            NumGuesses -= 1  # Only decrement guess count for legitimate guesses

            if guessedWord == randomword:
                # Correct guess: color the row and display a win message
                row = gw.get_current_row()
                if color_scheme == "BLUE":
                    for col in range(N_COLS):
                        gw.set_square_color(row, col, BLUE_COLOR)
                    gw.show_message("Hooray! You win.")
                else:
                    for col in range(N_COLS):
                        gw.set_square_color(row, col, CORRECT_COLOR)
                    gw.show_message("Hooray! You win.")
                return
            else:
                # Incorrect guess: determine correct and present positions
                correct_positions = []
                present_columns = []

                # Check for correct letters in correct positions
                for i in range(5):
                    if guessedWord[i] == randomword[i]:
                        correct_positions.append(i)

                # Check correct letters in wrong positions
                for i in range(5):
                    if i not in correct_positions and guessedWord[i] in randomword:
                        present_columns.append(guessedWord.index(guessedWord[i]))

                # Color the boxes accordingly
                row = gw.get_current_row()

                if color_scheme == "BLUE":
                    for col in range(N_COLS):
                        letter = randomword[col]
                        if col in correct_positions:
                            gw.set_square_color(row, col, BLUE_COLOR)
                        elif col in present_columns:
                            gw.set_square_color(row, col, ROSE_COLOR)
                        else:
                            gw.set_square_color(row, col, MISSING_COLOR)
                else:
                    for col in range(N_COLS):
                        letter = randomword[col]
                        if col in correct_positions:
                            gw.set_square_color(row, col, CORRECT_COLOR)
                        elif col in present_columns:
                            gw.set_square_color(row, col, PRESENT_COLOR)
                        else:
                            gw.set_square_color(row, col, MISSING_COLOR)

                # Check if the player has run out of guesses
                if NumGuesses == 0:
                    gw.show_message(f"You lose. The word was {randomword}.")
                    gw.add_enter_listener(lambda x: None)  # Disable further input
                # Move on to the next row
                else :
                    gw.set_current_row(gw.get_current_row() + 1)
                    gw.show_message(f"Nope. Try again. Guesses left: {NumGuesses}")

                # Check if the player has run out of guesses
                if NumGuesses == 0:
                    gw.show_message(f"You lose. The word was {randomword}.")
                    gw.add_enter_listener(lambda x: None)  # Disable further input

        else:
            gw.show_message("Invalid input: Word not in dictionary.")

    # Add the enter_action function as an input listener
    gw.add_enter_listener(enter_action) 
    
if __name__ == "__main__":
    wordle()