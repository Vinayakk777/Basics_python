import random
import string
import sys
import time

def type_effect(text, delay=0.03):
    """Print text with typing animation."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def generate_password(num_letters, num_symbols, num_numbers):
    """Generate a random password."""
    letters = list(string.ascii_letters)  # a-z, A-Z
    numbers = list(string.digits)         # 0-9
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Randomly select characters
    password_chars = (
        random.choices(letters, k=num_letters) +
        random.choices(numbers, k=num_numbers) +
        random.choices(symbols, k=num_symbols)
    )

    # Shuffle and return as string
    random.shuffle(password_chars)
    return ''.join(password_chars)

def check_strength(password):
    """Check password strength based on length and character diversity."""
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in "!#$%&()*+" for c in password)

    if length >= 12 and all([has_upper, has_lower, has_digit, has_symbol]):
        return "💪 Strong password! Excellent security."
    elif length >= 8:
        return "🟡 Medium strength. Add more symbols or length for better security."
    else:
        return "🔴 Weak password. Use at least 8+ characters with mix of symbols."

# --- Main Program ---
type_effect("Welcome to the 🔐 PyPassword Generator!")

try:
    nr_letters = int(input("How many letters would you like in your password? "))
    nr_symbols = int(input("How many symbols would you like? "))
    nr_numbers = int(input("How many numbers would you like? "))

    password = generate_password(nr_letters, nr_symbols, nr_numbers)
    type_effect(f"\nYour generated password: {password}", delay=0.05)
    print(check_strength(password))

except ValueError:
    print("⚠️ Invalid input. Please enter numeric values only.")


