"""
Starter file
"""
import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow

def wordle():
    def enter_action(s):
        gw.show_message("You have to implement this method.")
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
# Startup code
if __name__ == "__main__":
    wordle()
