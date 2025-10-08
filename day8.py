import sys
import time

# ---------------- ASCII LOGO (Option 3) ----------------
LOGOEN = """           
░█████╗░░█████╗░███████╗░██████╗░█████╗░██████╗░  ░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗  ██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░╚█████╗░███████║██████╔╝  ██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══██║██╔══██╗  ██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗██████╔╝██║░░██║██║░░██║  ╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝        
"""

# ---------------- UTILITIES ----------------
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def type_effect(text, delay=0.02):
    """Print text with typing animation."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def caesar_cipher(text, shift, direction):
    """Encode or decode a text using Caesar Cipher."""
    result = ""
    if direction == "decode":
        shift *= -1
    shift = shift % 26  # handle shift > 26

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            lower_char = char.lower()
            idx = alphabet.index(lower_char)
            new_idx = (idx + shift) % 26
            new_char = alphabet[new_idx]
            if is_upper:
                new_char = new_char.upper()
            result += new_char
        else:
            result += char
    return result

# ---------------- MAIN PROGRAM ----------------
def run_caesar():
    type_effect(LOGO, 0.001)
    type_effect("\n🔐 Welcome to Caesar Cipher!\n", 0.01)
    run = True
    while run:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction not in ['encode', 'decode']:
            type_effect("⚠️ Invalid option. Please choose 'encode' or 'decode'.\n", 0.01)
            continue

        text = input("Type your message:\n")
        try:
            shift = int(input("Type the shift number:\n"))
        except ValueError:
            type_effect("⚠️ Invalid shift number. Enter an integer.\n", 0.01)
            continue

        encrypted_text = caesar_cipher(text, shift, direction)
        type_effect(f"Here's the {direction}d result: {encrypted_text}\n", 0.01)

        choice = input("Do you want to run this program again? Type 'yes' or 'no': ").lower()
        if choice != 'yes':
            run = False
            type_effect("Goodbye!", 0.01)

# ---------------- RUN ----------------
if __name__ == "__main__":
    run_caesar()