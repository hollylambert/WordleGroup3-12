"""
Starter file
"""
import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_ROWS, N_COLS

def wordle():
    def enter_action(s):
        #Generates a random index to choose a word from the FIVE_LETTER_WORDS array
        index = random.randint(0, len(FIVE_LETTER_WORDS) - 1)
        
        #randomly selects a letter from FIVE_LETTER_WORDS using the randomly selected index
        random_word = FIVE_LETTER_WORDS[index]

        #Displays the random 
        for i, letter in enumerate(random_word):
            if i < N_COLS:
                gw.set_square_letter(0, i, letter)

        gw.show_message("You have to implement this method.")
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
# Startup code
if __name__ == "__main__":
    wordle()
