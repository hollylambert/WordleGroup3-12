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
    CHOSEN_COLOR,
    CHOSEN_LANGUAGE,
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
    # choose language
    # this is where we need to recieve correct code from toggle, my thoughts are to set a variable in wordleGraphics.py and then send it here similar to as follows
    lang = CHOSEN_LANGUAGE
    color_scheme = CHOSEN_COLOR

    # lang = input("Choose a language: English, French , Spanish : ").upper()
    # color_scheme - input("Choose a color scheme: Blue or Normal : ").upper()

    # Allow the user to choose a color scheme
    color_scheme = DarkModeButton()
    if lang == "ENGLISH":
        wordlist = FIVE_LETTER_WORDS
        invalidInput = "Invalid input: Must be 5 letters."
        wintext = "You win."
        losetext = "You lose. Correct word was: "
        incorrecttext = "Incorrect. Try again. Guesses Remaining: "
        notindicttext = "Invalid input: Word not in dictionary."
    elif lang == "FRENCH":
        wordlist = FRENCH_FIVE_LETTER_WORDS
        invalidInput = "Saisie invalide: Doit contenir 5 lettres."
        wintext = "Tu As Gagné."
        losetext = "Tú pierdes. La palabra correcta era: "
        incorrecttext = "Incorrect. Essaie encore. Suppositions restantes:"
        notindicttext = "Entrée non valide: Mot ne figurant pas dans le dictionnaire."
    elif lang == "SPANISH":
        wordlist = SPANISH_FIVE_LETTER_WORDS
        invalidInput = "Entrada inválida: Debe ser de 5 letras."
        wintext = "Tú Ganas."
        losetext = "Tu perds. Le mot correct était: "
        incorrecttext = "Incorrecto . Inténtalo de nuevo. Conjeturas Restantes:"
        notindicttext = "Entrada inválida: Palabra no en el diccionario."
    else:
        print("Invalid Language")
        return

    randomword = random.choice(wordlist)
    print(randomword)
    NumGuesses = 6

    def enter_action(s):
        nonlocal NumGuesses
        guessedWord = s.strip().lower()
        # Check if the guessed word has 5 letters
        if len(guessedWord) != 5:
            gw.show_message({invalidInput})
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
                    gw.show_message({wintext})
                else:
                    for col in range(N_COLS):
                        gw.set_square_color(row, col, CORRECT_COLOR)
                    gw.show_message({wintext})
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
                    gw.show_message(f"{losetext}{randomword}.")
                    gw.add_enter_listener(lambda x: None)  # Disable further input
                # Move on to the next row
                else:
                    gw.set_current_row(gw.get_current_row() + 1)
                    gw.show_message(f"{incorrecttext}{NumGuesses}")

                # Check if the player has run out of guesses
                if NumGuesses == 0:
                    gw.show_message(f"{losetext}{randomword}.")
                    gw.add_enter_listener(lambda x: None)  # Disable further input

        else:
            gw.show_message({notindicttext})

    # Add the enter_action function as an input listener
    gw.add_enter_listener(enter_action)


if __name__ == "__main__":
    wordle()
