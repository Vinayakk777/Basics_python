import random
import os
import time
import sys

# ---------------- ASCII ART ----------------
STAGES = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

LOGO = '''
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
'''

WIN_LOGO = '''
█▀▀ █▀█ █▀█ █▀▄   █░█░█ █▀█ █▀█ █▄▀ █
█▄█ █▄█ █▄█ █▄▀   ▀▄▀▄▀ █▄█ █▀▄ █░█ ▄
'''

# ---------------- WORD LIST ----------------
WORD_LIST = [
    'awkward', 'buffalo', 'cycle', 'equip', 'fjord', 'galaxy', 'jigsaw', 'matrix', 'oxygen',
    'python', 'rhythm', 'strength', 'wizard', 'zombie', 'pneumonia', 'luxury', 'mystify'
]

# ---------------- UTILITY FUNCTIONS ----------------
def clear_console():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_effect(text, delay=0.03):
    """Displays text with a typing animation."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ---------------- MAIN GAME ----------------
def hangman_game():
    clear_console()
    print(LOGO)
    type_effect("\n🎯 Welcome to HANGMAN: Guess the hidden word before the man is hung!\n", 0.03)

    chosen_word = random.choice(WORD_LIST)
    word_length = len(chosen_word)
    display = ["_"] * word_length
    wrong_guesses = []
    lives = len(STAGES) - 1
    end_of_game = False

    while not end_of_game:
        guess = input("\n🔤 Guess a letter: ").lower()

        # Clear console for better visibility
        clear_console()

        # Handle repeated guesses
        if guess in wrong_guesses or guess in display:
            print(f"⚠️ You already guessed '{guess}'. Try a new letter.\n")
        else:
            if guess in chosen_word:
                for i in range(word_length):
                    if chosen_word[i] == guess:
                        display[i] = guess
                print("✅ Good guess!")
            else:
                wrong_guesses.append(guess)
                lives -= 1
                print(f"❌ '{guess}' is not in the word. You lost a life.\n")

        # Display progress
        print(" ".join(display))
        print(STAGES[lives])

        # Win condition
        if "_" not in display:
            end_of_game = True
            type_effect("\n🎉 Genius! You won! 🥳", 0.04)
            print(WIN_LOGO)

        # Lose condition
        if lives == 0:
            end_of_game = True
            type_effect("\n💀 The man has been hung. You lose.", 0.04)
            print(f"The word was: '{chosen_word}'\n")

# ---------------- RUN GAME ----------------
if __name__ == "__main__":
    hangman_game()
